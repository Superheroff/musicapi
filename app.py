import json
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import codecs
import execjs


def kugou_music_sign(url):
    uri = url.split('?')[1]
    uri_list = uri.split('&')
    ordered_list = sorted(uri_list)
    uri = 'OIlwieks28dk2k092lksi2UIkp' + "".join(ordered_list) + 'OIlwieks28dk2k092lksi2UIkp'
    return hashlib.md5(uri.encode(encoding='utf-8')).hexdigest()


def QQMusicSign(param):
    param = json.dumps(param, separators=(',', ':'))
    return execjs.compile(open("node/QQSign.js", "r", encoding="utf-8").read()).call("get_sign", param)


def QQMusicSignOld(param):
    k1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
          "D": 13, "E": 14, "F": 15}
    l1 = [212, 45, 80, 68, 195, 163, 163, 203, 157, 220, 254, 91, 204, 79, 104, 6]
    t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    text = json.dumps(param, separators=(',', ':'))
    md5 = hashlib.md5(text.encode()).hexdigest().upper()
    t1 = ''.join([md5[i] for i in [21, 4, 9, 26, 16, 20, 27, 30]])
    t3 = ''.join([md5[i] for i in [18, 11, 3, 2, 1, 7, 6, 25]])
    ls2 = []
    for i in range(16):
        x1 = k1[md5[i * 2]]
        x2 = k1[md5[i * 2 + 1]]
        x3 = ((x1 * 16) ^ x2) ^ l1[i]
        ls2.append(x3)

    ls3 = []
    for i in range(6):
        if i == 5:
            ls3.append(t[ls2[-1] >> 2])
            ls3.append(t[(ls2[-1] & 3) << 4])
        else:
            x4 = ls2[i * 3] >> 2
            x5 = (ls2[i * 3 + 1] >> 4) ^ ((ls2[i * 3] & 3) << 4)
            x6 = (ls2[i * 3 + 2] >> 6) ^ ((ls2[i * 3 + 1] & 15) << 2)
            x7 = 63 & ls2[i * 3 + 2]
            ls3.extend(t[x4] + t[x5] + t[x6] + t[x7])

    t2 = ''.join(ls3).replace('[\\/+]', '')
    sign = 'zzb' + (t1 + t2 + t3).lower()
    return sign


class MusicApi_wyy_sign:
    def __init__(self, param):
        self.param = param

    def to_16(self, key):
        while len(key) % 16 != 0:
            key += '\0'
        return str.encode(key)

    @property
    def AES_encrypt(self):
        key = '0CoJUm6Qyw8W8jud'
        iv = "0102030405060708"
        bs = AES.block_size
        pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        encryptor = AES.new(self.to_16(key), AES.MODE_CBC, self.to_16(iv))
        pd2 = pad(str.encode(pad2(self.param)), 16)
        encrypt_aes = encryptor.encrypt(pd2)
        encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
        return encrypt_text

    @property
    def RSA_encrypt(self):
        get_i = execjs.compile(r"""
            function a(a) {
                var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
                for (d = 0; a > d; d += 1)
                    e = Math.random() * b.length,
                    e = Math.floor(e),
                    c += b.charAt(e);
                return c
            }
        """)
        i = get_i.call('a', 16)
        i = i[::-1]
        c = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        rs = int(codecs.encode(i.encode('utf-8'), 'hex_codec'), 16) ** int("010001", 16) % int(c, 16)
        return format(rs, 'x').zfill(256)


class MusicApi_kuwo_sign:
    def __init__(self):
        with open('node/kuwo.js', 'r', encoding='utf-8') as f:
            js = f.read()
        self.kuwojs = execjs.compile(js)

    @property
    def get_ReqId(self):
        return self.kuwojs.call('getReqId')

    def get_Secret(self, cookie):
        return self.kuwojs.call('get_Secret', cookie)

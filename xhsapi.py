import base64
import hashlib
from lxml import etree
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import execjs
import codecs
import requests
import json
import random

def kugou_url(hash):
    mid = '239526275778893399526700786998289824956'
    has = hash + '57ae12eb6890223e355ccfcb74edf70d1005' + mid + '0'
    str_md5 = hashlib.md5(has.encode(encoding='utf-8')).hexdigest()
    url = f'https://gateway.kugou.com/i/v2/?dfid=&pid=2&mid={mid}&cmd=26&token=&hash={hash}&area_code=1&behavior=play&appid=1005&module=&vipType=6&ptype=1&userid=0&mtype=1&album_id=&pidversion=3001&key={str_md5}&version=10209&album_audio_id=&with_res_tag=1'
    header = {
        'Host': 'gateway.kugou.com',
        'x-router': 'tracker.kugou.com',
        'User-Agent': 'Android511-AndroidPhone-10209-14-0-NetMusic-wifi'
    }
    ret = requests.get(url, headers=header).text
    # print(ret)
    ret = ret.replace('<!--KG_TAG_RES_START-->', '')
    ret = ret.replace('<!--KG_TAG_RES_END-->', '')
    json_data = json.loads(ret)
    return json_data['url'][0]

def str_right(str, new_str):
    if str.rfind(new_str) != -1:
        return str[str.rfind(new_str) + len(new_str):len(str)]
    else:
        return ""

def kugou_lrc(hash):
    url = f'http://krcs.kugou.com/search?ver=1&man=yes&client=mobi&keyword=&duration=&hash={hash}&album_audio_id='
    res = requests.get(url)
    ret = 'null'
    if res.status_code == 200:
        json_data = res.json()
        url = f'https://lyrics.kugou.com/download?ver=1&client=pc&id={json_data["candidates"][0]["id"]}&accesskey={json_data["candidates"][0]["accesskey"]}&fmt=lrc&charset=utf8'
        res = requests.get(url).json()
        ret = base64.b64decode(res['content']).decode("utf-8")
    #     if ret.find('[offset:0]') != -1:
    #         ret = str_right(ret, '[offset:0]')
    # print(ret)
    return ret

def kugou_signature(url):
    uri = url.split('?')[1]
    uri_list = uri.split('&')
    ordered_list = sorted(uri_list)
    uri = 'OIlwieks28dk2k092lksi2UIkp' + "".join(ordered_list) + 'OIlwieks28dk2k092lksi2UIkp'
    return hashlib.md5(uri.encode(encoding='utf-8')).hexdigest()

def kugou(ids):
    url = f'http://gatewayretry.kugou.com/v2/get_other_list_file?specialid={ids}&need_sort=1&module=CloudMusic' \
          '&clientver=11239&pagesize=300&specalidpgc' \
          f'={ids}&userid=0&page=1&type=0&area_code=1&appid=1005'

    header = {
        'User-Agent': 'Android9-AndroidPhone-11239-18-0-playlist-wifi',
        'Host': 'gatewayretry.kugou.com',
        'x-router': 'pubsongscdn.kugou.com',
        'mid': '239526275778893399526700786998289824956',  # 设备id
        'dfid': '-',
        'clienttime': str(time.time()).split('.')[0]
    }
    signature = kugou_signature(url)
    url = url + '&signature=' + signature
    ret = requests.get(url, headers=header)
    data_list = []
    if ret.status_code == 200:
        json_data = ret.json()
        for i in json_data['data']['info']:
            name = i['name'].split(' - ')
            song_id = i['hash']
            data_list.append({'title': name[1], 'author': name[0], 'url': 'http://api2.52jan.com/kugou/%s' % song_id, 'pic': i['cover'].replace('/{size}', ''), 'lrc': 'http://api2.52jan.com/kugou/lrc/%s.lrc' % song_id})
    else:
        pass
    # print(data_list)
    return data_list



def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)


def AES_encrypt(text, key, iv):
    bs = AES.block_size
    pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encryptor = AES.new(to_16(key), AES.MODE_CBC, to_16(iv))

    pd2 = pad(str.encode(pad2(text)), 16)

    encrypt_aes = encryptor.encrypt(pd2)
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypt_text


def RSA_encrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)

# 获取i值的函数，即随机生成长度为16的字符串
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


class WangYiYun():
    def __init__(self):
      # csrf_token、cookie和MUSIC_U需要抓包获取，如果你的账号开通了会员将支持会员歌曲
        self.csrf_token = ''
        self.data_list = []
        self.cookie = {}
        self.MUSIC_U = ''
        self.g = '0CoJUm6Qyw8W8jud'
        self.b = "010001"
        self.c = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.i = get_i.call('a', 16)
        self.iv = "0102030405060708"
        self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'

    def get_encSecKey(self):
        return RSA_encrypt(self.i, self.b, self.c)

    def get_wyy_discover(self, list_id):
        """
        获取歌单详情
        :param list_id: 列表id
        :return:
        """
        # 这里要添加自己的cookie
        ret = requests.get("https://music.163.com/playlist?id=" + list_id, headers={"User-Agent": self.ua}, cookies=self.cookie).text
        soup = etree.HTML(ret)
        m_id = soup.xpath('//ul[@class="f-hide"]/li/a/@href')
        ids = ''
        for i in m_id:
            ids += i.replace('/song?id=', '') + ','
        self.get_music_info(ids[:-1])
        # print(ids[:-1])
        # print(json.dumps(self.data_list))
        return self.data_list
        # song_id = m_id[random.randint(0, len(m_id) - 1)][9:]
        # return song_id

    def get_music_info(self, song_ids):
        url = f'http://music.163.com/api/song/detail/?id={song_ids}&ids=%5B{song_ids}%5D'
        ret = requests.get(url).json()
        for i in ret['songs']:
            song_id = i['id']
            author = ''
            for n in i['artists']:
                author += n['name'] + '/'
            self.data_list.append({'title': i['name'], 'author': author[:-1],
                                    'url': 'http://api2.52jan.com/wyy/%s' % song_id,
                                    'pic': i['album']['picUrl'],
                                    'lrc': 'http://api2.52jan.com/wyy/lrc/%s.lrc' % song_id})

    def get_wyy_playurl(self, music_id):
        url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token=' + self.csrf_token
        encText = str({'ids': "[" + str(music_id) + "]", 'br': 128000, 'csrf_token': self.csrf_token,
                       'MUSIC_U': self.MUSIC_U})
        params = AES_encrypt(AES_encrypt(encText, self.g, self.iv), self.i, self.iv)
        data = {
            'params': params,
            'encSecKey': self.get_encSecKey()
        }
        headeer = {
            'User-Agent': self.ua,
            'Referer': 'https://music.163.com/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        ret = requests.post(url, headers=headeer, data=data).json()
        try:
            download_url = ret['data'][0]['url']
        except:
            download_url = self.get_wyy_playurl2(music_id)
        if len(download_url) > 20:
            msg = download_url
        else:
            msg = {'msg': '出现了错误，错误位置：获取音乐源'}
        return msg

    def get_wyy_playurl2(self, music_id):
        url = f'https://music.163.com/api/song/enhance/player/url?id={music_id}&ids=%5B{music_id}%5D&br=3200000'
        ret = requests.get(url).json()
        try:
            download_url = ret['data'][0]['url']
        except:
            download_url = ''
        if len(download_url) > 20:
            msg = download_url
        else:
            msg = {'msg': '出现了错误，错误位置：获取音乐源2'}
        return msg

    def get_lrc(self, song_id):
        url = f'https://music.163.com/api/song/lyric?id={song_id}&lv=1&kv=1&tv=-1'
        ret = requests.get(url).json()
        lrc = ret['lrc']['lyric']
        if lrc == '':
            lrc = ret['klyric']['lyric']
        return lrc


if __name__ == '__main__':
    wyy = WangYiYun()
    # print(wyy.get_lrc('1413464902'))
    # wyy.get_wyy_discover('7480897649')
    # wyy.get_wyy_playurl('1413464902')
    # wyy.get_wyy_playurl2('1413464902')
    # kugou_lrc('90517066E6D63B05F96F2B7261A3CB13')
    # kugou_url('F49DE363462721C3F4B1AB3575D6153E')

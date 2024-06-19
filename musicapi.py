# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/25 18:52
@Author  : superhero
@Email   : 838210720@qq.com
@File    : musicapi.py
@IDE: PyCharm
"""
import base64
import hashlib
import json
import math
import random
import time
import requests
import http.cookies
from app import kugou_music_sign, MusicApi_wyy_sign, qq_music_sign, MusicApi_kuwo_sign


class MusicApi_kugou:
    def __init__(self, song_ids, HOST=None):
        """
        初始化
        """
        self.HOST = HOST if HOST else 'http://127.0.0.1:5050'
        self.cookie = None
        self.mid = '239526275778893399526700786998289824956'
        self.userid = '0'
        self.song_ids = song_ids
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }

    def MusicApi_set_cookie(self, cookie):
        self.cookie = cookie
        self.headers["Cookie"] = self.cookie

    @property
    def cookie_to_dict(self):
        cookie_dict = {}
        if self.cookie:
            cookies = http.cookies.SimpleCookie()
            cookies.load(self.cookie)
            for key, morsel in cookies.items():
                cookie_dict[key] = morsel.value
        return cookie_dict

    def get_kugou_url(self, music_id):
        """
        获取酷狗音乐源地址
        :param music_id:
        :return:
        """
        hax = music_id + '57ae12eb6890223e355ccfcb74edf70d1005' + self.mid + self.userid
        str_md5 = hashlib.md5(hax.encode(encoding='utf-8')).hexdigest()
        url = f'https://gateway.kugou.com/i/v2/?dfid=&pid=2&mid={self.mid}&cmd=26&token=&hash={music_id}&area_code=1&behavior=play&appid=1005&module=&vipType=6&ptype=1&userid=0&mtype=1&album_id=&pidversion=3001&key={str_md5}&version=10209&album_audio_id=&with_res_tag=1'
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

    def get_kugou_lrc(self, music_id):
        """
        获取酷狗歌词
        :param music_id:
        :return:
        """
        url = f'http://krcs.kugou.com/search?ver=1&man=yes&client=mobi&keyword=&duration=&hash={music_id}&album_audio_id='
        res = requests.get(url)
        if res.status_code == 200:
            json_data = res.json()
            url = f'https://lyrics.kugou.com/download?ver=1&client=pc&id={json_data["candidates"][0]["id"]}&accesskey={json_data["candidates"][0]["accesskey"]}&fmt=lrc&charset=utf8'
            res = requests.get(url).json()
            res = base64.b64decode(res['content']).decode("utf-8")
        else:
            res = "error:get_kugou_lrc"
        return res

    @property
    def get_kugou_list(self) -> list:
        """
        获取酷狗歌单列表
        :return:
        """
        url = f'http://gatewayretry.kugou.com/v2/get_other_list_file?specialid={self.song_ids}&need_sort=1&module=CloudMusic' \
              '&clientver=11239&pagesize=300&specalidpgc' \
              f'={self.song_ids}&userid=0&page=1&type=0&area_code=1&appid=1005'

        header = {
            'User-Agent': 'Android9-AndroidPhone-11239-18-0-playlist-wifi',
            'Host': 'gatewayretry.kugou.com',
            'x-router': 'pubsongscdn.kugou.com',
            'mid': self.mid,  # 设备id
            'dfid': '-',
            'clienttime': str(time.time()).split('.')[0]
        }
        signature = kugou_music_sign(url)
        url = url + '&signature=' + signature
        ret = requests.get(url, headers=header)
        kugou_music_list = []
        if ret.status_code == 200:
            json_data = ret.json()
            for i in json_data['data']['info']:
                name = i['name'].split(' - ')
                song_id = i['hash']
                kugou_music_list.append(
                    {'title': name[1], 'author': name[0], 'url': f'{self.HOST}/kugou/{song_id}',
                     'pic': i['cover'].replace('/{size}', ''),
                     'lrc': f'{self.HOST}/kugou/lrc/{song_id}.lrc',
                     'music_id': song_id})

        # print(kugou_music_list)
        return kugou_music_list


class MusicApi_wyy(MusicApi_kugou):
    def __init__(self, song_ids):
        super(MusicApi_wyy, self).__init__(song_ids)
        # csrf_token、cookie和MUSIC_U需要抓包获取，如果你的账号开通了会员将支持会员歌曲
        self.csrf_token = self.cookie_to_dict.get('csrf_token', '')

    @property
    def get_wyy_list(self) -> list:
        """
        获取网易云歌单列表
        :return:
        """
        # 这里要添加自己的cookie
        url = "http://music.163.com/api/v6/playlist/detail"
        self.headers["Cookie"] = self.cookie
        ret = requests.post(url, data={"s": "0", "id": self.song_ids, "n": "1000", "t": "0"},
                            headers=self.headers).json()
        ids = ''
        for i in ret['playlist']['trackIds']:
            ids += str(i['id']) + ','

        url = f'http://music.163.com/api/song/detail/?id={ids[:-1]}&ids=%5B{ids[:-1]}%5D'
        ret = requests.get(url, headers=self.headers).json()
        wyy_music_list = []
        for i in ret['songs']:
            song_id = i['id']
            author = ''
            for n in i['artists']:
                author += n['name'] + '/'
            pic = list(i['album']['picUrl'])
            pic.insert(4, 's')
            wyy_music_list.append({'title': i['name'], 'author': author[:-1],
                                   'url': f'{self.HOST}/wyy/{song_id}',
                                   'pic': ''.join(pic),
                                   'lrc': f'{self.HOST}/wyy/lrc/{song_id}.lrc',
                                   'music_id': str(song_id)})
        return wyy_music_list

    def get_wyy_url(self, music_id):
        """
        获取网易音乐源地址
        :param music_id: 音乐id
        :return:
        """
        url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=' + self.csrf_token
        encText = json.dumps(
            {'ids': "[" + str(music_id) + "]", 'encodeType': 'aac', 'csrf_token': self.csrf_token, 'level': 'standard'},
            separators=(',', ':'))
        params = MusicApi_wyy_sign(encText).AES_encrypt
        params = MusicApi_wyy_sign(params).AES_encrypt
        data = {
            'params': params,
            'encSecKey': MusicApi_wyy_sign(encText).RSA_encrypt
        }
        headers = {
            'User-Agent': self.headers['User-Agent'],
            'Referer': 'https://music.163.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': self.cookie
        }
        try:
            ret = requests.post(url, headers=headers, data=data).json()
            download_url = ret['data'][0]['url']
        except Exception as e:
            download_url = self.__get_wyy_url(music_id)
        return download_url

    def __get_wyy_url(self, music_id):
        """
        获取网易音乐源地址2
        :param music_id: 音乐id
        :return:
        """
        url = f'https://music.163.com/api/song/enhance/player/url?id={music_id}&ids=%5B{music_id}%5D&br=3200000'
        self.headers["Cookie"] = self.cookie
        ret = requests.get(url, headers=self.headers).json()
        download_url = ret['data'][0]['url']
        msg = download_url if download_url else {'msg': '出现了错误，错误位置：获取音乐源'}
        return msg

    def get_wyy_lrc(self, music_id):
        """
        获取歌词
        :param music_id: 音乐id
        :return:
        """
        url = f'https://music.163.com/api/song/lyric?id={music_id}&lv=1&kv=1&tv=-1'
        ret = requests.get(url).json()
        lrc = ret['lrc']['lyric']
        if lrc == '':
            lrc = ret['klyric']['lyric']
        return lrc


class MusicApi_qq(MusicApi_wyy):
    def __init__(self, song_ids):
        super(MusicApi_qq, self).__init__(song_ids)
        self.headers["Referer"] = "https://y.qq.com/"

    def get_qq_lrc(self, music_id):
        """
        QQ音乐歌词接口
        :param music_id: 音乐id
        """
        url = "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg"
        params = dict(format="json", songmid=f"{music_id}")
        res = requests.get(url, params=params, headers=self.headers).json()
        data = base64.b64decode(res["lyric"]).decode("utf-8")
        # print(data)
        if data == '':
            data = '纯音乐，请欣赏'
        return data

    @property
    def get_qq_list(self) -> list:
        """
        获取歌单列表
        :return:
        """
        url = f'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0' \
              f'&disstid={self.song_ids}&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&inCharset' \
              f'=utf8&outCharset=utf-8?ice=0&platform=yqq&needNewCode=0'
        ret = requests.get(url=url, headers=self.headers).text
        res = json.loads(ret[21:-1])
        qq_music_list = []
        for i in res['cdlist'][0]['songlist']:
            author = ''
            song_id = i['songmid']
            pic = 'https://y.qq.com/music/photo_new/T002R300x300M000%s.jpg' % i['albummid']
            for x in i['singer']:
                author += x['name'] + '/'
            qq_music_list.append({'title': i['songname'], 'author': author[:-1],
                                  'url': f'{self.HOST}/qqmusic/{song_id}',
                                  'pic': ''.join(pic),
                                  'lrc': f'{self.HOST}/qqmusic/lrc/{song_id}.lrc',
                                  'music_id': song_id})
        # print(json.dumps(qq_music_list, ensure_ascii=False))
        return qq_music_list

    @property
    def get_random(self):
        return ''.join(str(random.choice(range(10))) for _ in range(7))

    def get_qq_url(self, music_id):
        """
        获取歌曲播放地址
        :param music_id: 001GLG5B45uLhI
        :return:
        """
        i = 1
        req = 'req_' + str(i)
        # guid会影响成功率，所以要随机
        while True:
            param = {"comm": {"cv": 4747474, "ct": 24, "format": "json", "inCharset": "utf-8", "outCharset": "utf-8",
                              "notice": 0, "platform": "yqq.json", "needNewCode": 1, "uin": 838210,
                              "g_tk_new_20200303": 744448821, "g_tk": 744448821},
                     req: {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey",
                           "param": {"guid": "794" + self.get_random, "songmid": [music_id], "songtype": [0],
                                     "uin": "838210720",
                                     "loginflag": 1, "platform": "20"}}}
            url = f'https://u.y.qq.com/cgi-bin/musics.fcg?_={round(time.time() * 1000)}&sign={qq_music_sign(param)}'
            self.headers['cookie'] = self.cookie
            ret = requests.post(url=url, data=json.dumps(param, separators=(',', ':')), headers=self.headers).json()
            code = ret['code']
            if code == 2000:
                i += 1
                req = 'req_' + str(i)
                if i > 7:
                    break
            else:
                break

        purl = ret[req]['data']['midurlinfo'][0]['purl']
        uri = random.choice(ret[req]['data']['sip']) + purl if code == 0 and purl != '' else 'vip歌曲'
        return uri


class MusicApi_kuwo(MusicApi_qq):
    def __init__(self, song_ids):
        super(MusicApi_kuwo, self).__init__(song_ids)
        self.session = requests.session()
        cookie = "_ga=GA1.2.526731243.1718705002; _gid=GA1.2.1543973888.1718705002; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1718705002; h5Uuid=08d98230548b48f7a92b7bd084ba45-f7; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1718713693; _ga_ETPBRPM9ML=GS1.2.1718713677.2.1.1718713693.44.0.0; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=JXbannkz4r3pXFRW8YNjxzxmSkdxSPRX"
        self.MusicApi_set_cookie(cookie)
        self.headers["Secret"] = MusicApi_kuwo_sign().get_Secret(self.cookie)

    @property
    def get_kuwo_list(self):
        url = (f"https://bd.kuwo.cn/api/www/playlist/playListInfo?pid={self.song_ids}&pn=1&rn=20&httpsStatus=1&reqId"
               f"={MusicApi_kuwo_sign().get_ReqId}&plat=web_www&from=")
        self.headers["Referer"] = "https://bd.kuwo.cn/playlist_detail/" + self.song_ids
        kuwo_music_list = []
        ret = self.session.get(url, headers=self.headers).json()
        for i in ret['data']['musicList']:
            song_id = i['musicrid'][6:]
            kuwo_music_list.append({'title': i['album'], 'author': i['artist'],
                                    'url': f'{self.HOST}/kuwo/{song_id}',
                                    'pic': i['pic'],
                                    'lrc': f'{self.HOST}/kuwo/lrc/{song_id}.lrc',
                                    'music_id': song_id})
        return kuwo_music_list

    @property
    def random_music_list(self):
        """
        每日歌单推荐
        :return:
        """
        url = f"https://bd.kuwo.cn/api/www/rcm/index/playlist?id=rcm&pn=1&rn=5&httpsStatus=1&reqId={MusicApi_kuwo_sign().get_ReqId}&plat=web_www&from="
        self.headers["Referer"] = "https://bd.kuwo.cn/"
        ret = self.session.get(url, headers=self.headers).text
        print("酷我每日歌单推荐", ret)
        return ret

    def get_kuwo_url(self, music_id):
        url = f"https://bd.kuwo.cn/api/v1/www/music/playUrl?mid={music_id}&type=music&httpsStatus=1&reqId={MusicApi_kuwo_sign().get_ReqId}&plat=web_www&from="
        self.headers["Referer"] = "https://bd.kuwo.cn/playlist_detail/" + music_id
        try:
            ret = self.session.get(url, headers=self.headers).json()
            uri = ret['data']['url']
        except Exception as e:
            # 2000kflac
            url = f"https://mobi.kuwo.cn/mobi.s?f=web&source=jiakong&type=convert_url_with_sign&rid={music_id}&br=320kmp3"
            ret = requests.get(url, headers=self.headers).json()
            uri = ret['data']['url']
        return uri

    def get_kuwo_lrc(self, music_id):
        url = f"https://www.kuwo.cn/openapi/v1/www/lyric/getlyric?musicId={music_id}&httpsStatus=1&reqId={MusicApi_kuwo_sign().get_ReqId}&plat=web_www&from=lrc"
        self.headers["Referer"] = "https://www.kuwo.cn/play_detail/" + music_id
        ret = self.session.get(url, headers=self.headers).json()
        # print("酷我音乐歌词", ret)
        return self.__to_lrc(ret['data']['lrclist'])

    def __to_lrc(self, data):
        lrc = ''
        for i in data:
            start = float(i['time'])
            hour = math.floor(start) // 3600
            minute1 = (math.floor(start) - hour * 3600) // 60  # 分
            minute = (math.floor(start)) // 60  # 分 整数相除自动舍弃秒
            sec = math.floor(start) - hour * 3600 - minute1 * 60  # 秒
            minisec = int(math.modf(start)[0] * 100)  # 毫秒
            lrc += '[' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ':' + str(minisec).zfill(2) + ']' + i[
                "lineLyric"]
        return lrc


if __name__ == '__main__':

    song_ids = "6222311"
    MusicApi = MusicApi_kuwo(song_ids)
    music_list = MusicApi.get_kugou_list
    print("酷狗歌单信息：" + json.dumps(music_list, ensure_ascii=False))

    # 获取酷狗歌单第一个歌曲的源地址
    print("酷狗音乐源地址", MusicApi.get_kugou_url(music_list[0]['music_id']))

    MusicApi.song_ids = "7480897649"
    music_list = MusicApi.get_wyy_list
    print("网易云歌单信息：" + json.dumps(music_list, ensure_ascii=False))

    # 获取网易云歌单第一个歌曲的源地址
    print("网易云音乐源地址", MusicApi.get_wyy_url(music_list[0]['music_id']))

    MusicApi.song_ids = "8672698451"
    music_list = MusicApi.get_qq_list
    print("QQ歌单信息：" + json.dumps(music_list, ensure_ascii=False))

    # 获取QQ歌单第一个歌曲的源地址
    print("QQ音乐源地址", MusicApi.get_qq_url(music_list[0]['music_id']))

    MusicApi.song_ids = "3563672431"
    music_list = MusicApi.get_kuwo_list
    print("酷我歌单信息：" + json.dumps(music_list, ensure_ascii=False))

    # 获取酷我歌单第一个歌曲的源地址
    print("酷我音乐源地址", MusicApi.get_kuwo_url(music_list[0]['music_id']))

    # 酷我每日歌单推荐
    # music_list = MusicApi.random_music_list

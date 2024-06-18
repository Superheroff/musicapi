# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/25 19:47
@Author  : superhero
@Email   : 838210720@qq.com
@File    : main.py
@IDE: PyCharm
"""
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import musicapi

application = Flask(__name__, static_folder='templates/static')
application.config['JSON_AS_ASCII'] = False
CORS(application, resources=r'/*')


@application.route(rule="/kugou/<song_id>")
def kugou_url(song_id):
    kugou = musicapi.MusicApi_kugou(song_id)
    ret = kugou.get_kugou_url(song_id)
    return redirect(ret, code=301)


@application.route(rule="/kugou/lrc/<song_id>.lrc")
def kugou_lrc(song_id):
    kugou = musicapi.MusicApi_kugou(song_id)
    ret = kugou.get_kugou_lrc(song_id)
    return ret


@application.route(rule="/wyy/<song_id>")
def wyy_url(song_id):
    wyy = musicapi.MusicApi_wyy('')
    ret = wyy.get_wyy_url(song_id)
    return redirect(ret, code=301)


@application.route(rule="/wyy/lrc/<song_id>.lrc")
def wyy_lrc(song_id):
    wyy = musicapi.MusicApi_wyy('')
    ret = wyy.get_wyy_lrc(song_id)
    return ret


@application.route(rule="/qqmusic/<song_id>")
def qqmusic_url(song_id):
    qqmusic = musicapi.MusicApi_qq('')
    ret = qqmusic.get_qq_url(song_id)
    return redirect(ret, code=301)


@application.route(rule="/qqmusic/lrc/<song_id>.lrc")
def qqmusic_lrc(song_id):
    qqmusic = musicapi.MusicApi_qq('')
    ret = qqmusic.get_qq_lrc(song_id)
    return ret


@application.route('/music/songlist', methods=['POST', 'GET'])
def music_songlist():
    server = request.values.get('server', '')
    t_id = request.values.get('id', '')
    music_info = musicapi.MusicApi_kuwo(t_id)
    if server and t_id:
        if server == 'kugou':
            resp = music_info.get_kugou_list
        elif server == 'wyy':
            resp = music_info.get_wyy_list
        elif server == 'qqmusic':
            resp = music_info.get_qq_list
        elif server == 'kuwo':
            resp = music_info.get_kuwo_list
        else:
            resp = {'msg': '暂不支持此平台'}
    else:
        resp = {'msg': '缺少必要参数'}
    return jsonify(resp)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5050)

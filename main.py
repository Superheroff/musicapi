# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/25 19:47
@Author  : superhero
@Email   : 838210720@qq.com
@File    : main.py
@IDE: PyCharm
"""
import json

from gevent import monkey

monkey.patch_all()
from flask import Flask, jsonify, request, redirect, make_response
from flask_cors import CORS
import musicapi
from gevent.pywsgi import WSGIServer
from gevent.pool import Pool

application = Flask(__name__, static_folder='templates/static')
application.json.ensure_ascii = False
CORS(application, resources=r'/*')


def __set_no_cache(res):
    response = make_response(redirect(res, code=301))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
    return response


@application.route(rule="/kugou/<song_id>", methods=["GET", "POST"])
def kugou_url(song_id):
    MusicApi = musicapi.MusicApi_kugou(song_id)
    ret = MusicApi.get_kugou_url(song_id)
    return __set_no_cache(ret)


@application.route(rule="/kugou/lrc/<song_id>.lrc", methods=["GET", "POST"])
def kugou_lrc(song_id):
    MusicApi = musicapi.MusicApi_kugou(song_id)
    ret = MusicApi.get_kugou_lrc(song_id)
    return ret


@application.route(rule="/wyy/<song_id>", methods=["GET", "POST"])
def wyy_url(song_id):
    MusicApi = musicapi.MusicApi_wyy('')
    ret = MusicApi.get_wyy_url(song_id)
    return __set_no_cache(ret)


@application.route(rule="/wyy/lrc/<song_id>.lrc", methods=["GET", "POST"])
def wyy_lrc(song_id):
    MusicApi = musicapi.MusicApi_wyy('')
    ret = MusicApi.get_wyy_lrc(song_id)
    return ret


@application.route(rule="/qqmusic/<song_id>", methods=["GET", "POST"])
def qqmusic_url(song_id):
    MusicApi = musicapi.MusicApi_qq('')
    ret = MusicApi.get_qq_url(song_id)
    return __set_no_cache(ret)


@application.route(rule="/qqmusic/lrc/<song_id>.lrc")
def qqmusic_lrc(song_id):
    MusicApi = musicapi.MusicApi_qq('')
    ret = MusicApi.get_qq_lrc(song_id)
    return ret


@application.route(rule="/kuwo/<song_id>", methods=["GET", "POST"])
def kuwo_url(song_id):
    MusicApi = musicapi.MusicApi_kuwo('')
    ret = MusicApi.get_kuwo_url(song_id)
    return __set_no_cache(ret)


@application.route(rule="/kuwo/lrc/<song_id>.lrc", methods=["GET", "POST"])
def kuwo_lrc(song_id):
    MusicApi = musicapi.MusicApi_kuwo('')
    return MusicApi.get_kuwo_lrc(song_id)


@application.route(rule="/kuwo/random_music_list", methods=["GET", "POST"])
def kuwo_random_list():
    MusicApi = musicapi.MusicApi_kuwo('')
    return MusicApi.random_music_list


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
    response = make_response(json.dumps(resp, ensure_ascii=False, separators=(",", ":")))
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == "__main__":
    print("MusicApi start run")
    http_server = WSGIServer(('0.0.0.0', 7878), application, spawn=Pool(50))
    http_server.serve_forever()

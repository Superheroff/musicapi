from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import musicapi

application = Flask(__name__, static_folder='templates/static')
bootstrap = Bootstrap(application)
application.config['JSON_AS_ASCII'] = False
CORS(application, resources=r'/*')

@application.route(rule="/kugou/<song_id>")
def kugou_url(song_id):
    ret = musicapi.kugou_url(song_id)
    return redirect(ret, code=301)

@application.route(rule="/kugou/lrc/<song_id>.lrc")
def kugou_lrc(song_id):
    ret = musicapi.kugou_lrc(song_id)
    return ret


@application.route(rule="/wyy/<song_id>")
def wyy_url(song_id):
    wyy = musicapi.WangYiYun()
    ret = wyy.get_wyy_playurl(song_id)
    return redirect(ret, code=301)

@application.route(rule="/wyy/lrc/<song_id>.lrc")
def wyy_lrc(song_id):
    wyy = musicapi.WangYiYun()
    ret = wyy.get_lrc(song_id)
    return ret

@application.route(rule="/qqmusic/<song_id>")
def qqmusic_url(song_id):
    qqmusic = musicapi.qqmusic()
    ret = qqmusic.get_music_vkey(song_id)
    return redirect(ret, code=301)

@application.route(rule="/qqmusic/lrc/<song_id>.lrc")
def qqmusic_lrc(song_id):
    qqmusic = musicapi.qqmusic()
    ret = qqmusic.get_lyric(song_id)
    return ret

@application.route('/music/songlist', methods=['POST', 'GET'])
def music_songlist():
    server = request.values.get('server', '')
    songs_id = request.values.get('id', '')
    if server and songs_id:
        if server == 'kugou':
            resp = musicapi.kugou(songs_id)
        elif server == 'wyy':
            wyy = musicapi.WangYiYun()
            resp = wyy.get_wyy_discover(songs_id)
        elif server == 'qqmusic':
            qqmusic = musicapi.qqmusic()
            resp = qqmusic.get_music_list(songs_id)
        else:
            resp = {'msg': '暂不支持此平台'}
    else:
        resp = {'msg': '缺少必要参数'}
    return jsonify(resp)
  
  
  if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5050)

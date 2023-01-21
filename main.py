from flask import Flask, jsonify, request, redirect
from flask_cors import CORS

application = Flask(__name__, static_folder='templates/static')
bootstrap = Bootstrap(application)
application.config['JSON_AS_ASCII'] = False
CORS(application, resources=r'/*')

@application.route(rule="/kugou/<song_id>")
def kugou_url(song_id):
    xhsapi.red_updata_music()
    ret = xhsapi.kugou_url(song_id)
    return redirect(ret, code=301)

@application.route(rule="/kugou/lrc/<song_id>.lrc")
def kugou_lrc(song_id):
    xhsapi.red_updata_music()
    ret = xhsapi.kugou_lrc(song_id)
    return ret


@application.route(rule="/wyy/<song_id>")
def wyy_url(song_id):
    xhsapi.red_updata_music()
    wyy = xhsapi.WangYiYun()
    ret = wyy.get_wyy_playurl(song_id)
    return redirect(ret, code=301)

@application.route(rule="/wyy/lrc/<song_id>.lrc")
def wyy_lrc(song_id):
    xhsapi.red_updata_music()
    wyy = xhsapi.WangYiYun()
    ret = wyy.get_lrc(song_id)
    return ret

@application.route('/music/songlist', methods=['POST', 'GET'])
def music_songlist():
    server = request.values.get('server', '')
    songs_id = request.values.get('id', '')
    if server and songs_id:
        if server == 'kugou':
            xhsapi.red_updata_music()
            resp = xhsapi.kugou(songs_id)
        elif server == 'wyy':
            xhsapi.red_updata_music()
            wyy = xhsapi.WangYiYun()
            resp = wyy.get_wyy_discover(songs_id)
        else:
            resp = {'msg': '暂不支持此平台'}
    else:
        resp = {'msg': '缺少必要参数'}
    return jsonify(resp)
  
  
  if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5050)

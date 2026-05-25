# -*- coding: utf-8 -*-
"""
@Time    : 2026/05/25 21:47
"""

import json

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response
import uvicorn
import musicapi

app = FastAPI(title="Music API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _no_cache_redirect(url: str) -> RedirectResponse:
    response = RedirectResponse(url=url, status_code=301)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
    return response


@app.api_route("/kugou/{song_id}", methods=["GET", "POST"], tags=["酷狗API"])
async def kugou_url(song_id: str):
    MusicApi = musicapi.MusicApi_kugou(song_id)
    ret = MusicApi.get_kugou_url(song_id)
    return _no_cache_redirect(ret)


@app.api_route("/kugou/lrc/{song_id}.lrc", methods=["GET", "POST"], tags=["酷狗API"])
async def kugou_lrc(song_id: str):
    MusicApi = musicapi.MusicApi_kugou(song_id)
    ret = MusicApi.get_kugou_lrc(song_id)
    return Response(content=ret, media_type="text/plain; charset=utf-8")


@app.api_route("/wyy/{song_id}", methods=["GET", "POST"], tags=["网易音乐API"])
async def wyy_url(song_id: str):
    MusicApi = musicapi.MusicApi_wyy('')
    ret = MusicApi.get_wyy_url(song_id)
    return _no_cache_redirect(ret)


@app.api_route("/wyy/lrc/{song_id}.lrc", methods=["GET", "POST"], tags=["网易音乐API"])
async def wyy_lrc(song_id: str):
    MusicApi = musicapi.MusicApi_wyy('')
    ret = MusicApi.get_wyy_lrc(song_id)
    return Response(content=ret, media_type="text/plain; charset=utf-8")


@app.api_route("/qqmusic/{song_id}", methods=["GET", "POST"], tags=["QQ音乐API"])
async def qqmusic_url(song_id: str):
    MusicApi = musicapi.MusicApi_qq('')
    ret = MusicApi.get_qq_url(song_id)
    return _no_cache_redirect(ret)


@app.api_route("/qqmusic/lrc/{song_id}.lrc", methods=["GET", "POST"], tags=["QQ音乐API"])
async def qqmusic_lrc(song_id: str):
    MusicApi = musicapi.MusicApi_qq('')
    ret = MusicApi.get_qq_lrc(song_id)
    return Response(content=ret, media_type="text/plain; charset=utf-8")


@app.api_route("/kuwo/{song_id}", methods=["GET", "POST"], tags=["酷我音乐API"])
async def kuwo_url(song_id: str):
    MusicApi = musicapi.MusicApi_kuwo('')
    ret = MusicApi.get_kuwo_url(song_id)
    return _no_cache_redirect(ret)


@app.api_route("/kuwo/lrc/{song_id}.lrc", methods=["GET", "POST"], tags=["酷我音乐API"])
async def kuwo_lrc(song_id: str):
    MusicApi = musicapi.MusicApi_kuwo('')
    ret = MusicApi.get_kuwo_lrc(song_id)
    return Response(content=ret, media_type="text/plain; charset=utf-8")


@app.api_route("/kuwo/random_music_list", methods=["GET", "POST"], tags=["酷我音乐API"])
async def kuwo_random_list():
    MusicApi = musicapi.MusicApi_kuwo('')
    return Response(content=MusicApi.random_music_list, media_type="application/json; charset=utf-8")


@app.api_route("/music/songlist", methods=["GET", "POST"], tags=["歌单列表"])
async def music_songlist(server: str = Query(""), id: str = Query("")):
    music_info = musicapi.MusicApi_kuwo(id)
    if server and id:
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
    return Response(
        content=json.dumps(resp, ensure_ascii=False, separators=(",", ":")),
        media_type="application/json",
    )


if __name__ == "__main__":
    print("MusicApi start run")
    uvicorn.run(app, host="0.0.0.0", port=7878)
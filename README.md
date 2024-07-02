# 前言
- 做这个的初衷就是[Meting](https://github.com/metowolf/Meting)这个项目不稳定且不能满足自己的需求所以才有的这个项目
- 我的主要用途是构建博客的歌单列表，所以此项目只是以我博客的需求做的接口
- 目前已支持`酷狗、网易、QQ、酷我`音乐
- 浏览[我的歌单](https://www.app966.cn/music/)查看效果

# 如何添加COOKIE以及COOKIE有何作用
- `MusicApi_set_cookie`此方法添加COOKIE
- 如果你有会员的情况下是可以下载或试听会员音乐的(**注：禁止商业用途**)

# 如何使用
1. 下载本项目到本地
  ```shell
  git clone https://github.com/Superheroff/musicapi.git
  ```
2. 安装环境依赖
  ```shell
  pip install -r requirements.txt
  ```
3. 运行项目
  ```shell
  python main.py
  ```



# 请求示例
- **获取歌单列表信息**
- 请求地址：`http://127.0.0.1:7878`
- 路径：`/music/songlist`
- 请求方式：`POST,GET`
- 酷狗音乐示例：`http://127.0.0.1:7878/music/songlist?server=kugou&id=6222311`
- 网易云音乐示例：`http://127.0.0.1:7878/music/songlist?server=wyy&id=7480897649`
- QQ音乐示例：`http://127.0.0.1:7878/music/songlist?server=qqmusic&id=8672698451`
- 酷我音乐示例：`http://127.0.0.1:7878/music/songlist?server=kuwo&id=3563672431`
- 酷我获取推荐歌单列表示例：`http://127.0.0.1:7878/kuwo/random_music_list`

参数名|参数类型|参数描述|参数示例
---|---|---|---
server|string|音乐平台|kugou,wyy,qqmusic,kuwo
id|string|歌单ID|6222311,7480897649,8672698451,3563672431

# 响应示例
```
[
  {
    "author": "小霞、海洋Bo",
    "lrc": "http://127.0.0.1:7878/kugou/lrc/2E6D88A0CA2290BA32B614FC9C7EA43B.lrc",
    "music_id": "2E6D88A0CA2290BA32B614FC9C7EA43B",
    "pic": "http://imge.kugou.com/stdmusic/20230607/20230607152301805906.jpg",
    "title": "向云端",
    "url": "http://127.0.0.1:7878/kugou/2E6D88A0CA2290BA32B614FC9C7EA43B"
  },
  {
    "author": "张叶蕾",
    "lrc": "http://127.0.0.1:7878/wyy/lrc/2152040455.lrc",
    "music_id": "2152040455",
    "pic": "https://p2.music.126.net/zqd0535UOc3EDJvFf0Ymjw==/109951169555226745.jpg",
    "title": "爱你",
    "url": "http://127.0.0.1:7878/wyy/2152040455"
  },
  {
    "author": "任素汐",
    "lrc": "http://127.0.0.1:7878/qqmusic/lrc/001D51640M6ZeR.lrc",
    "music_id": "001D51640M6ZeR",
    "pic": "https://y.qq.com/music/photo_new/T002R300x300M00000003uSK0ttEuV.jpg",
    "title": "王招君 (你看你拉住我的模样)",
    "url": "http://127.0.0.1:7878/qqmusic/001D51640M6ZeR"
  },
  {
    "author": "杨宗纬&宝石Gem&王宇宙Leto",
    "lrc": "http://127.0.0.1:7878/kuwo/lrc/377413145.lrc",
    "music_id": "377413145",
    "pic": "https://img2.kuwo.cn/star/albumcover/500/s3s52/26/4134677797.png",
    "title": "若月亮没来(Live)",
    "url": "http://127.0.0.1:7878/kuwo/377413145"
  }
]
```

参数名|参数类型|参数描述
---|---|---
author|string|作者
lrc|string|歌词地址（待解析）
pic|string|歌曲封面
title|string|歌曲名
url|string|歌曲地址（待解析）
music_id|string|音乐ID


# 声明
- **本源码仅限用于学习交流，请勿用于商业用途，非法使用与作者无关**
- 如有侵权请联系我删除
- 学习交流QQ群：816017833

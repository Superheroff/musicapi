# 前言
- 做这个的初衷就是`hexo-tag-aplayer`不稳定且不能满足自己的需求所以才有的这个项目
- 我的主要用途是构建博客的歌单列表，所以此项目只是以我博客的需求做的接口
- 目前已支持`酷狗、网易、QQ、酷我`音乐
- 浏览[我的歌单](https://www.app966.cn/music/)查看效果

# 为此接口的升级版
```
https://api.i-meto.com/meting/api?server=tencent&type=playlist&id=8672698451
```

# 如何添加COOKIE以及COOKIE有何作用
- `MusicApi_set_cookie`此方法添加COOKIE
  - 如果你有会员的情况下是可以下载或试听会员音乐的（**注：请勿用于商业用途**）


# 接口说明
- **获取歌单列表信息**
- 本次更新新增酷我音乐接口

- 请求地址：`https://api2.52jan.com`
- 路径：`/music/songlist`
- 请求方式：`POST`
- 酷狗音乐示例：`https://api2.52jan.com/music/songlist?server=kugou&id=6222311`
- 网易云音乐示例：`https://api2.52jan.com/music/songlist?server=wyy&id=7480897649`
- QQ音乐示例：`https://api2.52jan.com/music/songlist?server=qqmusic&id=8672698451`
- 酷我音乐示例：`https://api2.52jan.com/music/songlist?server=kuwo&id=3563672431`
- **尽量不要用我的接口，下载源码自己部署吧**
- 查看[接口调用情况](https://www.app966.cn/charts/)

参数名|参数类型|参数描述|参数示例
---|---|---|---
server|string|音乐平台|kugou,wyy,qqmusic,kuwo
id|string|歌单ID|6222311,7480897649,8672698451,3563672431

# 响应参数
```
[{
	"author": "Uu(刘梦妤)",
	"lrc": "https://api2.52jan.com/kugou/lrc/0DBB2B56582BE6CB062F79D1D13FE21E.lrc",
	"pic": "https://imge.kugou.com/stdmusic/20210616/20210616180124589946.jpg",
	"title": "小城小爱",
	"url": "https://api2.52jan.com/kugou/0DBB2B56582BE6CB062F79D1D13FE21E"
}, {
	"author": "接个吻，开一枪/火鸡/吕口口/Lambert/杨胖雨",
	"lrc": "https://api2.52jan.com/wyy/lrc/1413464902.lrc",
	"pic": "https://p1.music.126.net/A157zQR5rR66LMatjYAucQ==/109951164595606537.jpg",
	"title": "春风十里报新年",
	"url": "https://api2.52jan.com/wyy/1413464902"
}, {
	"author": "周杰伦",
	"lrc": "https://api2.52jan.com/qqmusic/lrc/00265Jxe3JzXOJ.lrc",
	"pic": "https://y.qq.com/music/photo_new/T002R300x300M000000bviBl4FjTpO.jpg",
	"title": "说了再见",
	"url": "https://api2.52jan.com/qqmusic/00265Jxe3JzXOJ"
}, {
	"author": "李荣浩",
	"lrc": "https://api2.52jan.com/qqmusic/lrc/001GLG5B45uLhI.lrc",
	"pic": "https://y.qq.com/music/photo_new/T002R300x300M000002PwL9x3TiVdh.jpg",
	"title": "乌梅子酱",
	"url": "https://api2.52jan.com/qqmusic/001GLG5B45uLhI"
}]
```

参数名|参数类型|参数描述
---|---|---
author|string|作者
lrc|string|歌词地址（待解析）
pic|string|歌曲封面
title|string|歌曲名
url|string|歌曲地址（待解析）
music_id|string|音乐ID

# 闲话
- 由于歌曲地址会过期，而歌词文件又过大，所以我们先获取歌词、歌曲地址的解析地址，等待用户点击播放后再获取到歌曲、歌词文件；
- 这样既解决了源地址时效问题又解决了歌词文件直接显示过大不美观的问题。

# 声明
- 本源码仅限用于学习交流，请勿用于商业用途，非法使用与作者无关
- 如有侵权请联系我删除
- 学习交流QQ群：816017833

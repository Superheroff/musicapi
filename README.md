# 前言

- 目前已支持`酷狗、网易、QQ`音乐
- 浏览[我的歌单](http://www.app966.cn/music/)查看效果

# 接口说明
- **获取歌单列表信息**
- 请求地址：`http://api2.52jan.com`
- 路径：`/music/songlist`
- 请求方式：`POST`
- 酷狗音乐示例：`http://api2.52jan.com/music/songlist?server=kugou&id=6222311`
- 网易云音乐示例：`http://api2.52jan.com/music/songlist?server=wyy&id=7480897649`
- QQ音乐示例：`https://api2.52jan.com/music/songlist?server=qqmusic&id=8672698451`
- 尽量不要用我的接口，下载源码自己部署吧
- 查看[接口调用情况](https://www.app966.cn/charts/)

参数名|参数类型|参数描述|参数示例
---|---|---|---
server|string|音乐平台|kugou、wyy、qqmusic
id|string|歌单ID|6222311、7480897649、8672698451

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
	"author": "刘至佳",
	"lrc": "https://api2.52jan.com/qqmusic/lrc/0022fsjW39a0zG.lrc",
	"pic": "https://y.qq.com/music/photo_new/T002R300x300M0000016lk1t0LgKw6.jpg",
	"title": "说爱你",
	"url": "https://api2.52jan.com/qqmusic/0022fsjW39a0zG"
}]
```

参数名|参数类型|参数描述
---|---|---
author|string|作者
lrc|string|歌词地址（待解析）
pic|string|歌曲封面
title|string|歌曲名
url|string|歌曲地址（待解析）

# 说明
- 由于歌曲地址会过期，而歌词文件又过大，所以我们先获取歌词、歌曲地址的解析地址，等待用户点击播放后再获取到歌曲、歌词地址；
- 这样既解决了源地址时效问题又解决了歌词文件直接显示过大不美观的问题。

# 结尾
- 本源码仅限用于学习交流
- 如有侵权请联系我删除
- 谨慎使用，且行且珍惜

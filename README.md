# 前言
- Q：为什么无法播放呢？
- A：因为`hexo-tag-aplayer`这个插件的接口G了，我们自己做个接口替换就行了
- 由于时间有限，只花了一天时间目前只支持`酷狗、网易`音乐，后续更新企鹅音乐
- 浏览[我的歌单](http://www.app966.cn/music/)查看效果

# 接口说明
- **获取歌单列表信息**
- 请求地址：`http://api2.52jan.com`
- 路径：`/music/songlist`
- 请求方式：`POST`
- 酷狗音乐示例：`http://api2.52jan.com/music/songlist?server=kugou&id=6222311`
- 网易云音乐示例：`http://api2.52jan.com/music/songlist?server=wyy&id=7480897649`
- 尽量不要用我的接口，下载源码自己部署吧
- 查看[接口调用情况](https://www.app966.cn/charts/)

参数名|参数类型|参数描述|参数示例
---|---|---|---
server|string|音乐平台|kugou、wyy
id|string|歌单ID|6222311、7480897649

# 响应参数
```
[{
	"author": "不是源源/mok",
	"lrc": "http://api2.52jan.com/wyy/lrc/1912699471.lrc",
	"pic": "http://p1.music.126.net/fiXR2nTk6SLUKphHDmafJw==/109951166942065288.jpg",
	"title": "爆竹声声响",
	"url": "http://api2.52jan.com/wyy/1912699471"
}, {
	"author": "接个吻，开一枪/火鸡/吕口口/Lambert/杨胖雨",
	"lrc": "http://api2.52jan.com/wyy/lrc/1413464902.lrc",
	"pic": "http://p1.music.126.net/A157zQR5rR66LMatjYAucQ==/109951164595606537.jpg",
	"title": "春风十里报新年",
	"url": "http://api2.52jan.com/wyy/1413464902"
}]
```

参数名|参数类型|参数描述
---|---|---
author|string|作者
lrc|string|歌词地址（待解析）
pic|string|歌曲封面
title|string|歌曲名
url|string|歌曲地址（待解析）

# 原理
- 由于歌曲地址会过期，而歌词文件又过大，所以我们先获取歌词、歌曲地址的解析地址，等待用户点击播放后再获取到歌曲、歌词地址

# 结尾
- 本源码仅限用于学习交流
- 如有侵权请联系我删除

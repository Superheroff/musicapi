
function __to_blog(old_data=[], host="https://qcloud.app966.cn/music/") {
    let new_data = [];
    let music_dict = undefined;
    if (old_data.length > 0) {
        for (let i = 0; i < old_data.length; i++) {
            music_dict = {
            'name': old_data[i].title,
            'artist': old_data[i].author,
            'url': host + old_data[i].title + ".mp3",
            'cover': old_data[i].pic,
            'lrc': old_data[i].lrc,
            'theme': '#ad7a86'
            }
            new_data.push(music_dict)
        }
    }
    return JSON.stringify(new_data, null, 2)
}

music_list = [{"author":"吉星出租","lrc":"https://api2.52jan.com/qqmusic/lrc/003TjJPk1XR0yu.lrc","music_id":"003TjJPk1XR0yu","pic":"https://y.qq.com/music/photo_new/T002R300x300M000004YjcJf1P6Ro8.jpg","title":"暮色回响","url":"https://api2.52jan.com/qqmusic/003TjJPk1XR0yu"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/001cwR9G0LEC32.lrc","music_id":"001cwR9G0LEC32","pic":"https://y.qq.com/music/photo_new/T002R300x300M000003PIMo40rxcAn.jpg","title":"恋爱ing","url":"https://api2.52jan.com/qqmusic/001cwR9G0LEC32"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/001BAFqt1Ay4Vf.lrc","music_id":"001BAFqt1Ay4Vf","pic":"https://y.qq.com/music/photo_new/T002R300x300M000002PYDbl3I5L2k.jpg","title":"离开地球表面","url":"https://api2.52jan.com/qqmusic/001BAFqt1Ay4Vf"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/004LlhsV2NmnVY.lrc","music_id":"004LlhsV2NmnVY","pic":"https://y.qq.com/music/photo_new/T002R300x300M000001fbipy4azgKM.jpg","title":"我不愿 让你一个人","url":"https://api2.52jan.com/qqmusic/004LlhsV2NmnVY"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/0035sVym0anwc4.lrc","music_id":"0035sVym0anwc4","pic":"https://y.qq.com/music/photo_new/T002R300x300M000001YhoWf2XcCS7.jpg","title":"玫瑰少年","url":"https://api2.52jan.com/qqmusic/0035sVym0anwc4"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/003L6xyk0vvEeA.lrc","music_id":"003L6xyk0vvEeA","pic":"https://y.qq.com/music/photo_new/T002R300x300M0000042miPf28nzum.jpg","title":"温柔","url":"https://api2.52jan.com/qqmusic/003L6xyk0vvEeA"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/003g4dpV4bOEJs.lrc","music_id":"003g4dpV4bOEJs","pic":"https://y.qq.com/music/photo_new/T002R300x300M0000020I7sO0ayXhN.jpg","title":"你不是真正的快乐","url":"https://api2.52jan.com/qqmusic/003g4dpV4bOEJs"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/0033P66R0qEtlT.lrc","music_id":"0033P66R0qEtlT","pic":"https://y.qq.com/music/photo_new/T002R300x300M000003PIMo40rxcAn.jpg","title":"知足","url":"https://api2.52jan.com/qqmusic/0033P66R0qEtlT"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/004HyLC74RYiBC.lrc","music_id":"004HyLC74RYiBC","pic":"https://y.qq.com/music/photo_new/T002R300x300M000002plCgA0zOyYF.jpg","title":"倔强","url":"https://api2.52jan.com/qqmusic/004HyLC74RYiBC"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/0022QuVR1LcRHN.lrc","music_id":"0022QuVR1LcRHN","pic":"https://y.qq.com/music/photo_new/T002R300x300M000002fRO0N4FftzY.jpg","title":"后来的我们","url":"https://api2.52jan.com/qqmusic/0022QuVR1LcRHN"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/002M8hNI2QgtRY.lrc","music_id":"002M8hNI2QgtRY","pic":"https://y.qq.com/music/photo_new/T002R300x300M0000020I7sO0ayXhN.jpg","title":"突然好想你","url":"https://api2.52jan.com/qqmusic/002M8hNI2QgtRY"},{"author":"五月天","lrc":"https://api2.52jan.com/qqmusic/lrc/003lhef916qYN2.lrc","music_id":"003lhef916qYN2","pic":"https://y.qq.com/music/photo_new/T002R300x300M0000006MmDz4Hl2Ud.jpg","title":"步步","url":"https://api2.52jan.com/qqmusic/003lhef916qYN2"},{"author":"任素汐","lrc":"https://api2.52jan.com/qqmusic/lrc/001D51640M6ZeR.lrc","music_id":"001D51640M6ZeR","pic":"https://y.qq.com/music/photo_new/T002R300x300M00000003uSK0ttEuV.jpg","title":"王招君 (你看你拉住我的模样)","url":"https://api2.52jan.com/qqmusic/001D51640M6ZeR"}]

console.log(__to_blog(music_list))
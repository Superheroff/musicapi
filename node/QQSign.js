
window = {};
location = {
    "ancestorOrigins": {},
    "href": "https://y.qq.com/n/ryqq/search?w=%E8%90%BD%E7%A9%BA&t=song&remoteplace=txt.yqq.center",
    "origin": "https://y.qq.com",
    "protocol": "https:",
    "host": "y.qq.com",
    "hostname": "y.qq.com",
    "port": "",
    "pathname": "/n/ryqq/search",
    "search": "?w=%E8%90%BD%E7%A9%BA&t=song&remoteplace=txt.yqq.center",
    "hash": ""
}
navigator = {
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
require('./node/QQMusic.js')
window.n = Function()
!function(e) {
    function t(t) {
        for (var r, n, d = t[0], c = t[1], i = t[2], l = 0, u = []; l < d.length; l++)
            n = d[l],
            Object.prototype.hasOwnProperty.call(o, n) && o[n] && u.push(o[n][0]),
            o[n] = 0;
        for (r in c)
            Object.prototype.hasOwnProperty.call(c, r) && (e[r] = c[r]);
        for (b && b(t); u.length; )
            u.shift()();
        return f.push.apply(f, i || []),
        a()
    }
    function a() {
        for (var e, t = 0; t < f.length; t++) {
            for (var a = f[t], r = !0, n = 1; n < a.length; n++) {
                var c = a[n];
                0 !== o[c] && (r = !1)
            }
            r && (f.splice(t--, 1),
            e = d(d.s = a[0]))
        }
        return e
    }
    var r = {}
      , n = {
        21: 0
    }
      , o = {
        21: 0
    }
      , f = [];
    function d(t) {
        if (r[t])
            return r[t].exports;
        var a = r[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(a.exports, a, a.exports, d),
        a.l = !0,
        a.exports
    }
    window.n = d;
    d.e = function(e) {
        var t = [];
        n[e] ? t.push(n[e]) : 0 !== n[e] && {
            1: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            20: 1,
            22: 1,
            23: 1,
            24: 1,
            25: 1,
            26: 1
        }[e] && t.push(n[e] = new Promise((function(t, a) {
            for (var r = "css/" + ({
                1: "common",
                3: "album",
                4: "albumDetail",
                5: "album_mall",
                6: "category",
                7: "cmtpage",
                8: "download_detail",
                9: "index",
                10: "msg_center",
                11: "mv",
                12: "mvList",
                13: "mv_toplist",
                14: "notfound",
                15: "player",
                16: "player_radio",
                17: "playlist",
                18: "playlist_edit",
                19: "profile",
                20: "radio",
                22: "search",
                23: "singer",
                24: "singer_list",
                25: "songDetail",
                26: "toplist"
            }[e] || e) + "." + {
                1: "092d215c4a601df90f9f",
                3: "5cf0d69eaf29bcab23d2",
                4: "798353db5b0eb05d5358",
                5: "df4c243f917604263e58",
                6: "20d532d798099a44bc88",
                7: "e3bedf2b5810f8db0684",
                8: "559f0a2e11f1f5800b13",
                9: "ea0adb959fef9011fc25",
                10: "020422608fe8bfb1719a",
                11: "8bdb1df6c5436b790baa",
                12: "47ce9300786df1b70584",
                13: "4aee33230ba2d6b81dce",
                14: "e6f63b0cf57dd029fbd6",
                15: "1d2dbefbea113438324a",
                16: "d893492de07ce97d8048",
                17: "9484fde660fe93d9f9f0",
                18: "67fb85e7f96455763c83",
                19: "5e8c651e74b13244f7cf",
                20: "3befd83c10b19893ec66",
                22: "b2d11f89ea6a512a2302",
                23: "c7a38353c5f4ebb47491",
                24: "df0961952a2d3f022894",
                25: "4c080567e394fd45608b",
                26: "8edb142553f97482e00f"
            }[e] + ".chunk.css?max_age=2592000", o = d.p + r, f = document.getElementsByTagName("link"), c = 0; c < f.length; c++) {
                var i = (b = f[c]).getAttribute("data-href") || b.getAttribute("href");
                if ("stylesheet" === b.rel && (i === r || i === o))
                    return t()
            }
            var l = document.getElementsByTagName("style");
            for (c = 0; c < l.length; c++) {
                var b;
                if ((i = (b = l[c]).getAttribute("data-href")) === r || i === o)
                    return t()
            }
            var u = document.createElement("link");
            u.rel = "stylesheet",
            u.type = "text/css",
            u.onload = t,
            u.onerror = function(t) {
                var r = t && t.target && t.target.src || o
                  , f = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                f.code = "CSS_CHUNK_LOAD_FAILED",
                f.request = r,
                delete n[e],
                u.parentNode.removeChild(u),
                a(f)
            }
            ,
            u.href = o,
            0 !== u.href.indexOf(window.location.origin + "/") && (u.crossOrigin = "anonymous"),
            document.getElementsByTagName("head")[0].appendChild(u)
        }
        )).then((function() {
            n[e] = 0
        }
        )));
        var a = o[e];
        if (0 !== a)
            if (a)
                t.push(a[2]);
            else {
                var r = new Promise((function(t, r) {
                    a = o[e] = [t, r]
                }
                ));
                t.push(a[2] = r);
                var f, c = document.createElement("script");
                c.charset = "utf-8",
                c.timeout = 120,
                d.nc && c.setAttribute("nonce", d.nc),
                c.src = function(e) {
                    return d.p + "js/" + ({
                        1: "common",
                        3: "album",
                        4: "albumDetail",
                        5: "album_mall",
                        6: "category",
                        7: "cmtpage",
                        8: "download_detail",
                        9: "index",
                        10: "msg_center",
                        11: "mv",
                        12: "mvList",
                        13: "mv_toplist",
                        14: "notfound",
                        15: "player",
                        16: "player_radio",
                        17: "playlist",
                        18: "playlist_edit",
                        19: "profile",
                        20: "radio",
                        22: "search",
                        23: "singer",
                        24: "singer_list",
                        25: "songDetail",
                        26: "toplist"
                    }[e] || e) + ".chunk." + {
                        1: "eca3662fc5b34a080a57",
                        3: "f81d43e009b4d67acacf",
                        4: "4edebfdb0df6ae8b378a",
                        5: "8c99bfd1916c12bc64b3",
                        6: "b9a6d05d76a5f4a036bf",
                        7: "2c21cfbc014d4f435c6a",
                        8: "a776d3e1efb207cc74f7",
                        9: "4b5e4ed735dbad43a27c",
                        10: "83ffc6f852570f6e2aed",
                        11: "df364030d44efaa0fa76",
                        12: "690679ed97831c34eed5",
                        13: "bd404a637436c5700e66",
                        14: "3915242477f064e5d7fb",
                        15: "db0cad998dcb3bb3dc20",
                        16: "e13684bda35ff82b76aa",
                        17: "2e25bd5a4ad005ef7702",
                        18: "53a56f111ccc89c3b665",
                        19: "1d506bc195dc88207973",
                        20: "4ea6ba90c0cbf08082cd",
                        22: "a0081e579f9f618a5636",
                        23: "8d5c9f22d813b3c979e6",
                        24: "368ee01b1ebea4e5e9ad",
                        25: "7c4c17b1bd7bfba97137",
                        26: "80ef58f1657196f0b399"
                    }[e] + ".js?max_age=2592000"
                }(e),
                0 !== c.src.indexOf(window.location.origin + "/") && (c.crossOrigin = "anonymous");
                var i = new Error;
                f = function(t) {
                    c.onerror = c.onload = null,
                    clearTimeout(l);
                    var a = o[e];
                    if (0 !== a) {
                        if (a) {
                            var r = t && ("load" === t.type ? "missing" : t.type)
                              , n = t && t.target && t.target.src;
                            i.message = "Loading chunk " + e + " failed.\n(" + r + ": " + n + ")",
                            i.name = "ChunkLoadError",
                            i.type = r,
                            i.request = n,
                            a[1](i)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    f({
                        type: "timeout",
                        target: c
                    })
                }
                ), 12e4);
                c.onerror = c.onload = f,
                document.head.appendChild(c)
            }
        return Promise.all(t)
    }
    ,
    d.m = e,
    d.c = r,
    d.d = function(e, t, a) {
        d.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: a
        })
    }
    ,
    d.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    d.t = function(e, t) {
        if (1 & t && (e = d(e)),
        8 & t)
            return e;
        if (4 & t && "object" === typeof e && e && e.__esModule)
            return e;
        var a = Object.create(null);
        if (d.r(a),
        Object.defineProperty(a, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var r in e)
                d.d(a, r, function(t) {
                    return e[t]
                }
                .bind(null, r));
        return a
    }
    ,
    d.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return d.d(t, "a", t),
        t
    }
    ,
    d.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    d.p = "/ryqq/",
    d.oe = function(e) {
        throw e
    }
    ;
    var c = window.webpackJsonp = window.webpackJsonp || []
      , i = c.push.bind(c);
    c.push = t,
    c = c.slice();
    for (var l = 0; l < c.length; l++)
        t(c[l]);
    var b = i;
    a()
}([]);

const get_sign = window.n(350).default;

// data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":838210720,"g_tk_new_20200303":1944630473,"g_tk":1944630473},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.center","searchid":"63831761079354161","search_type":0,"query":"落空","page_num":1,"num_per_page":10}}}'
// console.log(get_sign)
// console.log(get_sign(data))
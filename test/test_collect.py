# import nose
from test import client


def test_collect_channel():
    cids = {"3000411": "You're Beautiful",
            "3701080": "亲密爱人",
            "3813365": "愛をこめて。海"}
    for cid in cids.keys():
        client.fm.collect_channel(cid=cid)


def test_collect_programmes():
    pids = {"1364115": "日本BGM",
            "300327": "会想起你，文艺青年",
            "26265": "那些感动你的中国摇滚乐"}
    for pid in pids.keys():
        client.fm.collect_programme(pid=pid)


def test_like_song():
    sids = {"1954748": "漂洋过海来看你",
            "1455725": "公路",
            "2005435": "离别赋"}
    for sid in sids.keys():
        client.fm.like_song(sid=sid)

# if __name__ == "__main__":
#     nose.main()
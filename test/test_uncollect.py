# import nose
from test import client


def test_uncollect_channel():
    cids = {"3000411": "You're Beautiful"}
    for cid in cids.keys():
        client.fm.uncollect_channel(cid)


def test_uncollect_multiple_channel():
    cids = {"3701080": "亲密爱人",
            "3813365": "愛をこめて。海"}
    cids = ",".join(cids.keys())
    client.fm.uncollect_multiple_channel(cids=cids)


def test_uncollect_programme():
    pids = {"1364115": "日本BGM", }
    for pid in pids.keys():
        client.fm.uncollect_programme(pid=pid)


def test_uncollect_multiple_programme():
    pids = {
        "300327": "会想起你，文艺青年",
        "26265": "那些感动你的中国摇滚乐"}
    pids = ",".join(pids.keys())
    client.fm.uncollect_multiple_programme(pids=pids)


def test_unlike_song():
    sids = {"1954748": "漂洋过海来看你",
            "1455725": "公路",
            "2005435": "离别赋"}
    for sid in sids.keys():
        client.fm.unlike_song(sid=sid)


def test_ban_song():
    sids = {"759512": "想太多",
            "1383143": "单身情歌",
            "179375": "如果还有明天"}
    for sid in sids.keys():
        client.fm.ban_song(sid=sid)

# if __name__ == "__main__":
#     nose.main()
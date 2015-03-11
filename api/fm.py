# -*- coding: utf-8 -*-

from .base import DoubanAPIBase


class FM(DoubanAPIBase):
    def __repr__(self):
        return "<DoubanAPI FM>"

    def user_info(self):
        return self._get("/v2/fm/user_info")

    # 红心歌曲
    def user_play_record(self, start="0", type="liked"):
        return self._get("/v2/fm/user_play_record",
                         start=start,
                         type=type)

     # 添加红心
    def like_song(self, sid):
        return self._post("/v2/fm/like_song",
                          sid=sid)

    # 取消红心
    def unlike_song(self, sid):
        return self._post("/v2/fm/unlike_song",
                          sid=sid)

    # 垃圾桶(不再收听)
    def ban_song(self, sid):
        return self._post("/v2/fm/ban_song",
                          sid=sid)

    # 获取歌词  (ssid在歌曲信息里面)
    def song_lyric(self, sid, ssid):
        return self._get("/v2/fm/lyric",
                         sid=sid,
                         ssid=ssid)

    # 与歌曲相关(相似兆赫/与这首歌相关的节目)
    def song_detail(self, sid):
        return self._get("/v2/fm/song_detail",
                         sid=sid)

    # type="n" 打开新频道(sid参数为空)   新的播放列表
    # type="r" 添加红心(sid当前播放歌曲sid)   新的播放列表
    # type="u" 取消红心(sid当前播放歌曲sid)   新的播放列表
    # type="b" 垃圾桶(sid当前播放歌曲sid)    新的播放列表
    # type="s" 切歌(sid当前播放歌曲sid)     新的播放列表
    # type="e" 正常播放完(sid当前播放歌曲sid)
    def play_list(self, sid="", type="n", channel="0",
                  version="630", app_name="radio_android"):
        return self._get("/v2/fm/playlist",
                         sid=sid,  # 不可缺
                         type=type,  # 不可缺
                         channel=channel,  # 不可缺
                         version=version,  # 不可缺
                         app_name=app_name  # 不可缺
                         # client=client,   # 缺少后，可能被服务器判断为未认证用户
                         )


    # =========================兆赫==================== #
    # 发现音乐－兆赫(我的兆赫/推荐兆赫/热门兆赫/上升最快兆赫/品牌兆赫)
    def channels(self):
        return self._get("/v2/fm/app_channels")

    # 用户收藏的兆赫
    def channels_collect(self, start="0", limit="50"):
        return self._get("/v2/fm/channel_collection",
                         start=start,
                         limit=limit)

    # 收藏兆赫
    def collect_channel(self, cid):
        self._post("/v2/fm/app_collect_channel",
                   id=cid)

    # 取消收藏兆赫
    def uncollect_channel(self, cid):
        return self._post("/v2/fm/app_uncollect_channel",
                          id=cid)

    # 取消收藏多个兆赫
    def uncollect_multiple_channel(self, cids):
        return self._post("/v2/fm/app_uncollect_channel_multi",
                          ids=cids)

    # ===========================节目===================== #

    # 发现音乐－节目(热门节目/猜你喜欢的节目)
    def hot_and_guess_programmes(self):
        return self._get("/v2/fm/programme/selections")

    # 用户收藏的节目
    def programmes_collect(self, start="0", limit="50"):
        return self._get("/v2/fm/programme/collection",
                         start=start,
                         limit=limit)

    # 节目内容
    def programmes_detail(self, pid):
        return self._get("/v2/fm/programme/detail",
                         id=pid)

    # 收藏节目
    def collect_programme(self, pid):
        return self._post("/v2/fm/programme/collect",
                          id=pid)

    # 取消收藏的节目
    def uncollect_programme(self, pid):
        return self._post("/v2/fm/programme/uncollect",
                          id=pid)

    # 取消多个收藏的节目
    # pids="348294,1360905,1364115"
    def uncollect_multiple_programme(self, pids):
        return self._post("/v2/fm/programme/uncollect_multi",
                          pids=pids)

    # 播放节目
    def play_log(self):
        pass

    # =============================搜索=================== #

    # 兆赫搜索
    def search_channel(self, query, start="0", limit="50"):
        return self._get("/v2/fm/search/channel",
                         q=query,
                         start=start,
                         limit=limit)

    # 节目搜索
    def search_programme(self, query, start="0", limit="50"):
        return self._get("/v2/fm/search/programme",
                         q=query,
                         start=start,
                         limit=limit)

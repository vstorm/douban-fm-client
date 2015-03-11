# import nose

from test import client, get_file_path, write_to_file


def get_play_list(sid, type, channel):
    return client.fm.play_list(sid=sid,
                               type=type,
                               channel=channel)
#
#
# def test_play_new_channel():
#     file_path = get_file_path("play_list/play_new_channel")
#     sid = ""
#     type = "n"
#     channel = "1"  # 华语MHZ
#     play_list = get_play_list(sid, type, channel)
#     write_to_file(file_path, play_list)
#
#
# def test_skip_song():
#     file_path = get_file_path("play_list/skip_song")
#     sid = "277041"  # 亲爱的小孩 (六个小孩)
#     type = "s"
#     channel = "4221247"  # 缘系MHZ
#     play_list = get_play_list(sid, type, channel)
#     write_to_file(file_path, play_list)
#
#
# def test_like_song():
#     file_path = get_file_path("play_list/like_song")
#     sid = "291697"  # 花火（国语）
#     type = "r"
#     channel = "4221247"  # 缘系MHZ
#     play_list = get_play_list(sid, type, channel)
#     write_to_file(file_path, play_list)
#
#
# def test_unlike_song():
#     file_path = get_file_path("play_list/unlike_song")
#     sid = "291697"  # 花火（国语）
#     type = "u"
#     channel = "4221247"  # 缘系MHZ
#     play_list = get_play_list(sid, type, channel)
#     write_to_file(file_path, play_list)
#
#
# def test_ban_song():
#     file_path = get_file_path("play_list/ban_song")
#     sid = "33120"  # 再一次
#     type = "b"
#     channel = "4221247"  # 缘系MHZ
#     play_list = get_play_list(sid, type, channel)
#     write_to_file(file_path, play_list)


def test_normal_play_song():
    file_path = get_file_path("play_list/normal_play_song")
    sid = "1699763"  # 没收
    type = "e"
    channel = "4221247"  # 缘系MHZ
    play_list = get_play_list(sid, type, channel)
    write_to_file(file_path, play_list)


# if __name__ == "__main__":
#     nose.runmodule()
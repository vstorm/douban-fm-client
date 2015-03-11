# -*- coding: utf-8 -*-
import nose

from test import client, get_file_path, write_to_file

def test_user_info():
    file_path = get_file_path("user_info")
    user_info = client.fm.user_info()
    write_to_file(file_path, user_info)


def test_channels():
    file_path = get_file_path("channels")
    channels = client.fm.channels()
    write_to_file(file_path, channels)


def test_channels_collect():
    file_path = get_file_path("channels_collect")
    channels_collect = client.fm.channels_collect()
    write_to_file(file_path, channels_collect)


def test_programmes_collect():
    file_path = get_file_path("programmes_collect")
    programmes_collect = client.fm.programmes_collect()
    write_to_file(file_path, programmes_collect)


def test_hot_and_guess_programmes():
    file_path = get_file_path("hot_and_guess_programmes")
    hot_and_guess_programmes = client.fm.hot_and_guess_programmes()
    write_to_file(file_path, hot_and_guess_programmes)


def test_programme_detail():
    file_path = get_file_path("programme_detail")
    pid = "1364115"  # 日本BGN
    programme_detail = client.fm.programmes_detail(pid=pid)
    write_to_file(file_path, programme_detail)


def test_user_play_record():
    file_path = get_file_path("user_play_record")
    user_play_record = client.fm.user_play_record()
    write_to_file(file_path, user_play_record)


def test_song_lyric():
    file_path = get_file_path("song_lyric")
    sid = "1954748"
    ssid = "1c3c"
    song_lyric = client.fm.song_lyric(sid=sid, ssid=ssid)
    write_to_file(file_path, song_lyric)


def test_song_detail():
    file_path = get_file_path("song_detail")
    s = {"1954748": "漂洋过海来看你"}
    sid = "1954748"
    song_detail = client.fm.song_detail(sid=sid)
    write_to_file(file_path, song_detail)


def test_search_channel():
    file_path = get_file_path("search_channel")
    query = "华语"
    search_channel = client.fm.search_channel(query=query)
    write_to_file(file_path, search_channel)


def test_search_programme():
    file_path = get_file_path("search_programme")
    query = "华语"
    search_programme = client.fm.search_programme(query=query)
    write_to_file(file_path, search_programme)


if __name__ == "__main__":
    nose.main()
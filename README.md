# douban-fm-client(Beta)
Python client library(not official version) for Douban Fm API

## 功能
* OAuth2 认证
* 个人信息
* 添加红心/取消红心/不在收听/切歌
* 所有红心歌曲
* 歌词
* 与歌曲相关(相似兆赫/相关的节目)
* 播放新兆赫
* 我的兆赫/推荐兆赫/热门兆赫/上升最快兆赫/品牌兆赫
* 收藏的兆赫
* 收藏兆赫/取消收藏
* 播放节目
* 热门节目/猜你喜欢的节目
* 收藏的节目
* 节目内容
* 收藏节目/取消收藏
* 兆赫搜索
* 节目搜索

## 使用方法

### OAuth 2.0 认证
    from client import DoubanFmClient

    API_KEY = 'your api key'
    API_SECRET = 'your api secret'
    REDIRECT_URL = "http://douban.fm"

    client = DoubanFmClient(API_KEY, API_SECRET, REDIRECT_URL)

    # 以下方式 3 选 1:
    # 1. 引导用户授权
    print 'Go to the following link in your browser:'
    print client.authorize_url
    code = raw_input('Enter the verification code:')
    client.auth_with_code(code)

    # 2. 如果有之前有 token，则可以
    client.auth_with_token(token)

    # Token Code
    token_code = client.token_code

    # Refresh Token
    # 请注意：`refresh_token_code` 值仅可在授权完成时获取(即在 `auth_with_code`, `auth_with_password` 之后)
    refresh_token_code = client.refresh_token_code
    client.refresh_token(refresh_token_code) # refresh token

    # 3. 用户使用邮箱和密码
    client.auth_with_password(your_username, your_password)

### 接口说明
    # 例子

    # 以下cid为兆赫id
    收藏兆赫　client.fm.collect_channel(cid=cid)
    取消收藏  client.fm.uncollect_channel(cid=cid)

    (详细用法可以查看*api/fm.py*文件注释)

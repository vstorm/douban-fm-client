from .fm import FM


class DoubanFmAPI(object):
    def __repr__(self):
        return "<DoubanFmClient API>"

    @property
    def fm(self):
        return FM(self.access_token)
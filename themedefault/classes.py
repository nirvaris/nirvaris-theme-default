

class Img():
    def __init__(self, url):
        self.url = url

class TagImage():

    def __init__(self, tinny_url, small_url, full_url, description):
        self.tinny = Img('/static/gallery/' + tinny_url)
        self.small = Img('/static/gallery/' + small_url)
        self.full = Img('/static/gallery/' + full_url)
        self.description = description


from interviewcake.url_shortener import *


def test_shorten1():
    url = "http://www.linkedin.com/JDFagan"
    us = UrlShortener()
    url_short = us.shorten(url)
    print("url = {}".format(url))
    print("shortened_url = {}".format(url_short))
    assert us.lengthen(url_short) == "http://www.linkedin.com/JDFagan"

import random

# O(inf) time and O(n) space
class UrlShortener:
    # Requirements:
    # Strip out prefix if exists (http:// or https://) and the domain - simply replace always with http://ca.ke/
    # Fixed length shortened URL like bit.ly does - 7 alphanumeric characters
    # Preserve case within local scope of the url (e.g., http://www.LinkedIn.com/JDFagan
    #           -> (http://ca.ke/1lkasjdf, http://www.linkedin.com/JDFagan)

    HTTP = 'http://'
    HTTPS = 'https://'
    CAKE = 'http://ca.ke/'
    DIGITS = '0123456789'
    ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        self.urls_by_long = {}
        self.urls_by_short = {}

    def __random_url(self):
        while True:
            random_url1 = ''.join(random.choice(UrlShortener.DIGITS) for i in range(1))
            random_url_rest = ''.join(random.choice(UrlShortener.ALPHA) for i in range(6))
            random_url = random_url1 + random_url_rest
            if random_url not in self.urls_by_short:
                return random_url

    def shorten(self, url: str):
        # Clean domain url part
        url_lower = url.lower()

        http_loc = url_lower.find(UrlShortener.HTTP)
        https_loc = url_lower.find(UrlShortener.HTTPS)

        if http_loc >= 0:
            domain_loc = url_lower.find('/', http_loc)
        elif https_loc >= 0:
            domain_loc = url_lower.find('/', https_loc)
        else:
            domain_loc = url_lower.find('/')

        # Check for impossible URL
        if domain_loc < 3:
            raise ValueError('Invalid URL')

        domain_part = url_lower[0:domain_loc]
        local_part = url[domain_loc:]
        cleansed_url = domain_part + local_part

        if cleansed_url not in self.urls_by_long:
            random_url = UrlShortener.CAKE + self.__random_url()
            self.urls_by_long[cleansed_url] = random_url
            self.urls_by_short[random_url] = cleansed_url

        return self.urls_by_long[cleansed_url]

    def lengthen(self, shortened_url):
        return self.urls_by_short[shortened_url]

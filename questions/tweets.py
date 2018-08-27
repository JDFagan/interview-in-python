# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

"""
From CircleUp:
Given a list of tweet tuples with a format of (sentence, timestamp), you need to answer the following questions about
the data:

- Total number of words across all of time
- Total number of unique words across all of time
- Unique hashtag words used across all of time
- Total number of unique words with character length of 5 used across all time
- Total number of words in the last minute, 10 minutes, and last hour
- Most common word length for words in the last hour
"""

from datetime import datetime
from datetime import timedelta

tweets = [
    ('hello world', datetime.now()),
    ('a second sentence', datetime.now() - timedelta(days=7)),
    ('a hello #hashtag', datetime.now() - timedelta(hours=1)),
    ('#hello there #helio', datetime.now() - timedelta(minutes=5))
    ]


class TweetAnalysis():
    def __init__(self, tweets):
        self.tweets = tweets

    def get_words(self):
        words = []
        for t in tweets:
            words.extend(t[0].split(' '))

        return len(words)

    def unique_words(self):
        words = set()
        for t in tweets:
            words.update(t[0].split(' '))

        return len(words)

    def unique_tags(self):
        words = set()
        for t in tweets:
            possible_words = t[0].split(' ')
            for pw in possible_words:
                if pw[0] == '#':
                    words.add(pw)

        return len(words)

    def unique_words_equal_len(self, l):
        words = set()
        for t in tweets:
            possible_words = t[0].split(' ')
            for pw in possible_words:
                if len(pw) == l:
                    words.add(pw)

        return len(words)

    def words_over_time(self):
        result = []

        for td in [timedelta(minutes=1), timedelta(minutes=10), timedelta(hours=1)]:
            words = []
            for t in tweets:
                t_datetime = t[1]
                if t_datetime >= datetime.now() - td:
                    words.extend(t[0].split(' '))

            result.append(len(words))

        return result

    def most_common_word_len_over_time(self, td):
        word_lens = {}
        for t in tweets:
            t_datetime = t[1]
            if t_datetime >= datetime.now() - td:
                my_words = t[0].split(' ')
                for w in my_words:
                    len_of_word = len(w)
                    word_lens[len_of_word] = word_lens[len_of_word] + 1 if len_of_word in word_lens else 1

        result = None
        max_word_len_freq = 0
        for k, v in word_lens.items():
            print("{}, {}".format(k, v))
            if v > max_word_len_freq:
                max_word_len_freq = v
                result = k

        return result


ta = TweetAnalysis(tweets)
print(ta.get_words())
print(ta.unique_words())
print(ta.unique_tags())
print(ta.unique_words_equal_len(5))
print(ta.words_over_time())
print(ta.most_common_word_len_over_time(timedelta(hours=1)))

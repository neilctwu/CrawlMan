import hashlib
import random
import time


def hashhex(s):
    """Returns a heximal formated SHA1 hash of the input string."""
    h = hashlib.sha1()
    h.update(s.encode('utf-8'))
    return h.hexdigest()


def random_sleep(s, e):
    t = random.randint(s, e)
    print('<Sleeping> For {} seconds'.format(t))
    time.sleep(t)

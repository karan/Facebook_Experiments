# http://stackoverflow.com/questions/16675803/learning-python-and-threading-i-think-my-code-runs-infinitely-help-me-find-bug

import json
import urllib2
from collections import Counter
from multiprocessing.dummy import Pool # use threads
import time

def get_name(url):
    try:
        return json.load(urllib2.urlopen(url))['gender']
    except Exception:
        return None # error

start = time.time()
urls = ('http://graph.facebook.com/%d' % i for i in xrange(200))
p = Pool(5) # 5 concurrent connections
first_names = Counter(p.imap_unordered(get_name, urls))
print first_names.most_common()
print 'It took %s s' % (time.time() - start)

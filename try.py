import requests
import json
import random
import time
import sets

visited = sets.Set()

for j in range(10):
    success = 0
    fail = 0
    start = time.time()
    for i in range(50):
        ID = random.randint(1000, 100000000)
        if ID not in visited:
            try:
                url = 'http://graph.facebook.com/' + str(ID)
                res = requests.get(url)
                if res.status_code == 200:
                    success += 1
                else:
                    fail += 1
                visited.add(ID)
            except:
                print 'well...'
    print '%s successes and %s fails in %s s\n' % (success, fail, (time.time()-start))

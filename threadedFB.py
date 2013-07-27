import requests
import json
import time
import threading
import Queue

GraphURL = 'http://graph.facebook.com/'
first_names = {} # will store first names and their counts
queue = Queue.Queue()

def getOneUser(url):
    http_response = requests.get(url) # open the request URL
    if http_response.status_code == 200:
        data = http_response.text.encode('utf-8', 'ignore') # Get the text of response, and encode it
        json_obj = json.loads(data) # load it as a json object
        # name = json_obj['name']
        return json_obj['first_name']
        # last = json_obj['last_name']
    else:
        return None

class ThreadGet(threading.Thread):
    """ Threaded name scraper """
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url = GraphURL + str(self.queue.get())
            first = getOneUser(url) # get one user's first name
            if first is not None:
                if first_names.has_key(first): # if name has been encountered before
                    first_names[first] = first_names[first] + 1 # increment the count
                else:
                    first_names[first] = 1 # add the new name
            self.queue.task_done()

def main():
    start = time.time()

    for i in range(10):
        t = ThreadGet(queue)
        t.setDaemon(True)
        t.start()

    for i in range(100):
        queue.put(i)

    queue.join()

    for name in first_names.keys():
        print name + ': ' + str(first_names[name])

    print '----------------------------------------------------------------'
    # Print top first names
    for key in first_names.keys():
        if first_names[key] > 5:
            print key + ': ' + str(first_names[key])
        
    print 'It took ' + str(time.time()-start) + 's'
    
main()

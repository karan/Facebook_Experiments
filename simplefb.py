import requests
import json
import time


def getOneUser(count):
    url = 'http://graph.facebook.com/' + str(count)
    http_response = requests.get(url) # open the request URL
    if http_response.status_code == 200:
        data = http_response.text.encode('utf-8', 'ignore') # Get the text of response, and encode it
        json_obj = json.loads(data) # load it as a json object
        # name = json_obj['name']
        return json_obj['first_name']
        # last = json_obj['last_name']
    return None


def main():
    start = time.time() # It took 17.6830000877s

    names = {} # will store full names and their counts
    first_names = {} # will store first names and their counts
    last_names = {} # will store last names and their counts

    for count in range(1, 2000):
        first = getOneUser(count) # get one user's first name
        if first is not None:
            if first_names.has_key(first): # if name has been encountered before
                first_names[first] = first_names[first] + 1 # increment the count
            else:
                first_names[first] = 1 # add the new name
        count = count + 1

    end = time.time()

    # Print all names and their count
    for key in first_names.keys():
        print key + ': ' + str(first_names[key])

    """
    print '----------------------------------------------------------------'
    print '================================================================'

    
    # Print top first names
    for key in first_names.keys():
        if first_names[key] > 5:
            print key + ': ' + str(first_names[key])
    """
    print 'It took ' + str(end-start) + 's'
    

if __name__ == '__main__':
    main()

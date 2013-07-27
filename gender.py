import requests
import json
import time


def getOneUser(count):
    url = 'http://graph.facebook.com/' + str(count)
    http_response = requests.get(url) # open the request URL
    if http_response.status_code == 200:
        data = http_response.text.encode('utf-8', 'ignore') # Get the text of response, and encode it
        json_obj = json.loads(data) # load it as a json object
        if 'gender' in json_obj.keys():
            return json_obj['gender']
    return None


def main():
    start = time.time() # It took 17.6830000877s

    males = 0
    females = 0
    
    for count in range(1, 100):
        gender = getOneUser(count) # get one user's first name
        if gender is not None:
            print str(count) + gender
            if gender == 'male':
                males += 1
            elif gender == 'female':
                females += 1
        count = count + 1

    end = time.time()

    print '%s males and %s females' % (males, females)
    

if __name__ == '__main__':
    main()

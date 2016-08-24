# this causes an error where are you getting this library?
# seems you have to download the requests library separately but that doesn't seem necessary for our purposes.  
#urllib2 should probably do the trick
# import requests

import urllib2
import urllib

token_file = open("reviewer_api_key.txt")
TOKEN = token_file.read()
CERTIFICATIONS_URL = 'https://review-api.udacity.com/api/v1/me/certifications.json'
# I'm having trouble getting through the authorization on the udacity reviews page.  
# When I put the headers variable in my request I get an error (see below).  
# But when when I remove them I get an 'unauthorized' error
# headers = {'Authorization': TOKEN}
# req = urllib2.Request(CERTIFICATIONS_URL, headers)

# response = urllib2.urlopen(req)
# page_contents = response.read()





def startReviewBot():
	print TOKEN
    # print page_contents


    

def main():
    print "oh hey Joel"
    print "Welcome to the big leagues"
    startReviewBot()

if __name__ == '__main__':
    main()

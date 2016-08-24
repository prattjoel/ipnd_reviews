
# requests library now working
import requests
import json

token_file = open("reviewer_api_key.txt")
TOKEN = token_file.read()
CERTIFICATIONS_URL = 'https://review-api.udacity.com/api/v1/me/certifications.json'
headers = {'Authorization': TOKEN, 'Content-Length': '0'}
response = requests.get(CERTIFICATIONS_URL, headers=headers)

def startReviewBot():
	print response.status_code
	print response.headers['content-type']
	print response.text

    

def main():
    print "oh hey Joel"
    print "Welcome to the big leagues"
    startReviewBot()

if __name__ == '__main__':
    main()

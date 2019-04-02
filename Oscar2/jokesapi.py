import requests
import json


# call rest API to get horoscope for a given zodiac sign
def get_joke():
	response = requests.get('https://geek-jokes.sameerkumar.website/api')
	data =response.json
	print (data)
	print (response.url)
	print (response.status_code)
	#print response.headers["content-type"]
	json_data = response.json()
	#json is raw data which contains all the data from the api response
	return json_data

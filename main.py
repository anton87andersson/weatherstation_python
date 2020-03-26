# Set API-key from openweathermap.org
apikey = "ed5b646a676bec3d15f7f13b3299ebd9"

# Set the City from what the user input
city = raw_input("Enter city name: ")

# Set the units
units = "metric"

# Define the function 
def weather(value, value2):
	import urllib2
	import json

	# The request-URL
	req = urllib2.Request("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}".format(city, apikey, units))
	opener = urllib2.build_opener()
	f = opener.open(req)
	
	# Get the json-data
	json = json.loads(f.read())
	
	# Return the values from the Json
	return json[value][value2]


try:

	# Format the temprature string
	the_temprature = "The temprature in {} is: {} C and feels like {} C".format(city, weather("main", "temp"), weather("main", "feels_like"))
	
	# Format the humidity
	the_humidity = "The humidity is {}% ".format(weather("main", "humidity"))
	print ""
	print ""
	print "--------------------------------------------------------"
	print the_temprature
	print "--------------------------------------------------------"
	print the_humidity
	print "--------------------------------------------------------"
	print ""
	print ""

except:
    print('There was an error.')





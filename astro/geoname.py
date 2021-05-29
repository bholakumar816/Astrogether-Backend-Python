from urllib.request import urlopen
from urllib.parse import urlencode
from xml.dom.minidom import parseString
from socket import timeout
from urllib.error import HTTPError, URLError


def _getText(nodelist):
	"""Internal function to return text from nodes
	"""
	rc = ""
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc = rc + node.data
	return rc

def search(city_name='',country_code=''):
	if city_name == '':
		print('No name specified!')
		return None
		
	#open connection and read xml
	params = urlencode({'q': city_name,'country':country_code,'maxRows':1,'featureClass':'P','username': 'astro_login'})

	try:
		f = urlopen("http://api.geonames.org/search?%s" % params, timeout=20)

	except (HTTPError, URLError) as error:
		print('Errir: not retrieved because %s\nURL: %s', error, f)

	except timeout:
		print('Timeout on search!')
		return None
	
	data = f.read()
	dom = parseString(data)

	#totalResultsCount
	totalResultsCount = _getText(dom.getElementsByTagName("totalResultsCount")[0].childNodes)
	
	#geoname
	geoname=[]
	for i in dom.getElementsByTagName("geoname"):
		geoname.append({})
		geoname[-1]['name']=_getText(i.getElementsByTagName("name")[0].childNodes)
		geoname[-1]['lat']=_getText(i.getElementsByTagName("lat")[0].childNodes)
		geoname[-1]['lng']=_getText(i.getElementsByTagName("lng")[0].childNodes)
		geoname[-1]['geonameId']=_getText(i.getElementsByTagName("geonameId")[0].childNodes)
		geoname[-1]['countryCode']=_getText(i.getElementsByTagName("countryCode")[0].childNodes)
		geoname[-1]['countryName']=_getText(i.getElementsByTagName("countryName")[0].childNodes)
		geoname[-1]['fcl']=_getText(i.getElementsByTagName("fcl")[0].childNodes)
		geoname[-1]['fcode']=_getText(i.getElementsByTagName("fcode")[0].childNodes)
		#get timezone
		tparams = urlencode({'lat':geoname[-1]['lat'],'lng':geoname[-1]['lng'],'username':'century.boy'})		
		try:
			f = urlopen("http://api.geonames.org/timezone?%s" % tparams, timeout=20)
		except (HTTPError, URLError) as error:
			print('Errir: not retrieved because %s\nURL: %s', error, f)
		except timeout:
			print('Timeout on search!')
			return None

		data = f.read()
		tdom = parseString(data)
		geoname[-1]['timezonestr']=_getText(tdom.getElementsByTagName("timezoneId")[0].childNodes)
		tdom.unlink()
		break
	#close dom
	dom.unlink()
	
	#return results
	if totalResultsCount == "0":
		print("No results!")
		return None
	else:
		return geoname
import firebase_admin
from firebase_admin import credentials, firestore
import requests


from bs4 import BeautifulSoup
cred = credentials.Certificate("./serviceAccountKey.json")
authApp = firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://smart-banks.firebaseio.com/'
})

database = firestore.client()
sources = database.collection('gold_sources').stream()
gold_prices_ref = database.collection('gold_prices')
for source in sources:
	val = source.to_dict()
	page = requests.get(val['url'])
	soup = BeautifulSoup(page.content, 'html.parser')
	table = soup.select(val['table'])[0]
	if val['buyr']!=-1:
		buyrow = table.find_all('tr')[val['buyr']]
		buy = buyrow.find_all('td')[val['buyc']]
		buystr = buy.get_text().split(' ')[0].replace(',','.')
	else:
		buystr = '-1'
	if val['sellr']!=-1:
		sellrow = table.find_all('tr')[val['sellr']]
		sell = sellrow.find_all('td')[val['sellc']]
		sellstr = sell.get_text().split(' ')[0].replace(',','.')
	else:
		sellstr = '-1'
	
	gold_price = gold_prices_ref.document(val['goldId'])
	try:
		buyfloat = float(buystr)
	except ValueError:
		buyfloat=-1
	try:
		sellfloat = float(sellstr)
	except ValueError:
		sellfloat=-1
	
	field_updates = {"buy": buyfloat,"sell":sellfloat,"updated":firestore.SERVER_TIMESTAMP}
	gold_price.update(field_updates)

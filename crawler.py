import firebase_admin
from firebase_admin import credentials, firestore
import requests


from bs4 import BeautifulSoup
cred = credentials.Certificate("./serviceAccountKey.json")
authApp = firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://smart-banks.firebaseio.com/'
})

database = firestore.client()
sources = database.collection('sources').stream()
banks_ref = database.collection('banks')
for source in sources:
	val = source.to_dict()
	if val['type']=='HTML':
		page = requests.get(val['url'])
		soup = BeautifulSoup(page.content, 'html.parser')
		table = soup.select(val['table'])[val['tableindex']]
		if val['t3r']!=-1:
			t3row = table.find_all('tr')[val['t3r']]
			t3 = t3row.find_all('td')[val['t3c']]
			t3str = t3.get_text().split(' ')[0].replace(',','.')
		else:
			t3str = '-1'
		if val['t6r']!=-1:
			t6row = table.find_all('tr')[val['t6r']]
			t6 = t6row.find_all('td')[val['t6c']]
			t6str = t6.get_text().split(' ')[0].replace(',','.')
		else:
			t6str = '-1'
		if val['t12r']!=-1:
			t12row = table.find_all('tr')[val['t12r']]
			t12 = t12row.find_all('td')[val['t12c']]
			t12str = t12.get_text().split(' ')[0].replace(',','.')
		else:
			t12str = '-1'
		if val['t0r']!=-1:
			t0row = table.find_all('tr')[val['t0r']]
			t0 = t0row.find_all('td')[val['t0c']]
			t0str = t0.get_text().split(' ')[0].replace(',','.')
		else:
			t0str = '-1'
		if val['t1r']!=-1:
			t1row = table.find_all('tr')[val['t1r']]
			t1 = t1row.find_all('td')[val['t1c']]
			t1str = t1.get_text().split(' ')[0].replace(',','.')
		else:
			t1str = '-1'
		if val['t9r']!=-1:
			t9row = table.find_all('tr')[val['t9r']]
			t9 = t9row.find_all('td')[val['t9c']]
			t9str = t9.get_text().split(' ')[0].replace(',','.')
		else:
			t9str = '-1'
		if val['t18r']!=-1:
			t18row = table.find_all('tr')[val['t18r']]
			t18 = t18row.find_all('td')[val['t18c']]
			t18str = t18.get_text().split(' ')[0].replace(',','.')
		else:
			t18str = '-1'
		if val['t24r']!=-1:
			t24row = table.find_all('tr')[val['t24r']]
			t24 = t24row.find_all('td')[val['t24c']]
			t24str = t24.get_text().split(' ')[0].replace(',','.')
		else:
			t24str = '-1'
		if val['t36r']!=-1:
			t36row = table.find_all('tr')[val['t36r']]
			t36 = t36row.find_all('td')[val['t36c']]
			t36str = t36.get_text().split(' ')[0].replace(',','.')
		else:
			t36str = '-1'
		bank = banks_ref.document(val['bankId'])
		try:
			t3float = float(t3str)
		except ValueError:
			t3float=-1
		try:
			t6float = float(t6str)
		except ValueError:
			t6float=-1
		try:
			t12float = float(t12str)
		except ValueError:
			t12float=-1
		try:
			t0float = float(t0str)
		except ValueError:
			t0float=-1
		try:
			t1float = float(t1str)
		except ValueError:
			t1float=-1
		try:
			t9float = float(t9str)
		except ValueError:
			t9float=-1
		try:
			t18float = float(t18str)
		except ValueError:
			t18float=-1
		try:
			t24float = float(t24str)
		except ValueError:
			t24float=-1
		try:
			t36float = float(t36str)
		except ValueError:
			t36float=-1
		field_updates = {"quarter": t3float,"half":t6float,"full":t12float,"t0": t0float,"t1":t1float,"t9":t9float,"t18": t18float,"t24":t24float,"t36":t36float,"updated":firestore.SERVER_TIMESTAMP}
		bank.update(field_updates)

import firebase_admin
from firebase_admin import credentials, firestore
import requests

cred = credentials.Certificate("./serviceAccountKey.json")
authApp = firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://smart-banks.firebaseio.com/'
})

database = firestore.client()
sources = database.collection('sources').stream()
sources_ref = database.collection('sources')
for source in sources:
	val = source.to_dict()
	if val['type']=='HTML':
		t0r=val['t3r']
		t1r=val['t3r']
		t9r=val['t3r']
		t18r=val['t3r']
		t24r=val['t3r']
		t36r=val['t3r']
		t0c=1
		t1c=2
		t9c=5
		t18c=7
		t24c=8
		t36c=9
		field_updates = {'t0r':t0r,'t1r':t1r,'t9r':t9r,'t18r':t18r,'t24r':t24r,'t36r':t36r,'t0c':t0c,'t1c':t1c,'t9c':t9c,'t18c':t18c,'t24c':t24c,'t36c':t36c,}
		sourceObj = sources_ref.document(source.id)
		sourceObj.update(field_updates)

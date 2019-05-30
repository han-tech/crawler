import firebase_admin
from firebase_admin import credentials, firestore
import requests

cred = credentials.Certificate("./serviceAccountKey.json")
authApp = firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://smart-banks.firebaseio.com/'
})

database = firestore.client()
sources = database.collection('gold_sources').stream()
sources_ref = database.collection('gold_sources')
for source in sources:
	val = source.to_dict()
	field_updates = {'t0r':t0r,'t1r':t1r,'t9r':t9r,'t18r':t18r,'t24r':t24r,'t36r':t36r,'t0c':t0c,'t1c':t1c,'t9c':t9c,'t18c':t18c,'t24c':t24c,'t36c':t36c,}
	sourceObj = sources_ref.document(source.id)
	sourceObj.update(field_updates)

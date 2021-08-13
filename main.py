#!/usr/bin/python3
-*- coding: utf-8 -*-

# import pandas and requests
import pandas as pd
import requests
 
# load data
# replace <file path> with file path of contact.xlsx file
data = pd.read_excel('<file path>')
 
# create Dataframe from data
data = pd.DataFrame(data=data)

#create a colummn with properly formatted number i.e start with 233
data['phone'] = ['233' + str(i) for i in data['phone']]
 
#split the data into the portions for processing
dataA = data.iloc[:round(0.6*len(data)), :]
 
dataB = data.iloc[round(0.6*len(data)):, :]
 
#convert to json format
dataA = dataA.to_json(orient='records')
dataB = dataB.to_json(orient='records')
 
urlA = "http://domainA:12345/sendsms?username=domainA&password=passA&to=233548617798&from=senderA&text=TestA"
urlB = "http://domainB:09876/sendsms?username=domainB&password=passB&to=233267722174&from=senderB&text=TestB"
 
#send data to be processed by URLs
for data in dataA:
 requests.post(url=urlA, data = dataA)
 
for data in dataB:
 requests.post(url=urlB, data = dataB)
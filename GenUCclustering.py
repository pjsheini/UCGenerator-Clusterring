import itertools
import copy
import time
#import pandas as pd
#import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import uuid
import json
#import randomcolor
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout
def genUniversalConcepts(concept,outfile):

	output={}

	output['UC']=[]
	output['GUID'] = []
	
	output['UC'].append(concept)
	output['GUID'].append(uuid.uuid4().hex)

	json.dump(output, outfile, ensure_ascii=False)
	outfile.write('\n')

def translate (driver, word):

	query = driver.find_element_by_id("source")
	query.clear()
	origingword = word
	wrd = origingword + '\t'
	query.send_keys(wrd)
	#time.sleep(1)
	result = driver.find_element_by_id("gt-src-is-list")
	time.sleep(1)
	listofsyn = str(result.text).split('\n')
	if len(listofsyn) > 1:
		return (listofsyn[1])
	else:
		return (listofsyn[0])
	#time.sleep(5)

	


if __name__ == '__main__':

	driver = webdriver.Firefox(executable_path='/Users/psheinidashtegol/Documents/geckodriver')

	from_lang = 'en'
	to_lang = 'de'
	baseUrl = "https://translate.google.com/#"
	final_url = baseUrl + from_lang + '/' + to_lang
	driver.get(final_url)
	with open('UniConceptClusteringENDE50k.txt', 'w') as outfile:
		with open ("Computed-UniversalConceptsOptV03.txt",'r') as ENUC:
			data = json.load(ENUC)
			for i in range(0,len(data)):
				Combined_Words = []
				EnWords = []
				print( i )
				EnWords = data[str(i)].split(';')
				EnESWords = []
				for wd in EnWords:
					print(wd)
					#try:
					#wd ="courts"
					wdn = translate(driver, wd)
					EnESWords.append(wdn.strip())
					#except Exception,e:
						#print (str(e))
				print(EnESWords)
				Combined_Words = EnWords+EnESWords 
				genUniversalConcepts(Combined_Words, outfile)
				
				#json_out.write('{}\n'.format(word))
		driver.close()
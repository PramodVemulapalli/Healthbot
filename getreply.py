# Module: f2.py
from bs4 import BeautifulSoup

import urllib.parse
import requests
import json
import lxml
import sys
import os
import random
import pdb

def get_reqheaders():
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    return req_headers


def get_reply(inputSymptom, currentUrl):

    firstfetchbaseurl = 'https://www.healthline.com/symptom/'
    completeurl = firstfetchbaseurl + inputSymptom.lower().replace(" ","-")
    with requests.Session() as s:
        r = s.get(completeurl, headers=get_reqheaders())
        soup2 = BeautifulSoup(r.content, 'lxml')
        if (soup2.find(text='Add symptoms to narrow your search')):
            answerurl = ''
            step2 = soup2.find('span',text='Add symptoms to narrow your search')
            answertext = 'Based on your symptom: ' + inputSymptom + '. Here are the top 5 possible conditions : \n '
            allmatches = soup2.find_all("h2")
            countitems = 0
            for eachmatch in allmatches:
                z=eachmatch.find_parent('a')
                if ( z is not None ):
                    answertext = answertext + str(countitems+1) + ') ' + z.find('h2').text
                    answertext = answertext + '   https://www.healthline.com' + z['href']
                    answertext = answertext + ' \n'
                    countitems += 1

                if (countitems == 5):
                    break


            answerurl = ''
        else:
            answerurl = ''
            answertext = 'Based on your input symptoms: ' + inputSymptom + '. Here is some useful information: ' + completeurl
    return answerurl, answertext

# Example 2: class methods to store and retrieve properties
class fromtheweb(object):
    def __init__(self):
        self.inputSymptom = ''
        self.currentUrl = ''
    def setinputSymptom(self, myVar):
        self.inputSymptom = myVar
    def setcurrentUrl(self, myVar):
        self.currentUrl = myVar
    def getreply(self):
        return get_reply(self.inputSymptom, self.currentUrl)

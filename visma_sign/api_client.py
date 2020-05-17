import requests 
import hashlib 
import base64
import time
import hmac
import email.utils
import datetime
import json

from .config import *

class ApiClient:
   
    def __init__(self):
        print('Init VismaSign')


    def addAuthentication(self, path, payload, http_type, fileContent ):
        content_type = "application/json"
        dt = datetime.datetime.now()
        today = email.utils.format_datetime(dt)
        md5_file = hashlib.md5( payload ).digest()
        content_md5 =  str(base64.b64encode( md5_file ), 'utf-8' )
        autorization_header = http_type+"\n"+ content_md5+"\n"+ fileContent +"\n"+ today +"\n"+path
        key = base64.b64decode(secret)
        autorization_header_enc =  'Onnistuu '+identifier+':'+str(base64.b64encode(hmac.new(key, autorization_header.encode(), hashlib.sha512).digest()), "utf-8")
        self.url = api_url + path
        self.header = {
            "Content-MD5": content_md5,
            "Content-Type":fileContent,
            "Date": today,
            "Authorization":autorization_header_enc
        }

    def createDocument(self, document):
        path = "/api/v1/document/"
        http_type = "POST"
        fileContent = "application/json"
        self.addAuthentication(path, document.encode() , http_type,fileContent)
        r = requests.post(url = self.url,  headers=self.header,data=document) 
        print(r.text)
        locationParts = r.headers['Location'].split('/')
        return locationParts[len(locationParts) -1]

    def addFile(self, documentUuid, payload, fileName):
        path = "/api/v1/document/" + documentUuid + "/files"
        http_type = "POST"
        fileContent = "application/pdf"
        self.addAuthentication(path, payload, http_type, fileContent)
        r = requests.post(url = self.url,  headers=self.header, data=payload ) 
        return json.loads(r.text)['uuid']

    def createInvitations(self, documentUuid, invitations):      
        path =  "/api/v1/document/" + documentUuid + "/invitations"
        http_type = "POST"
        fileContent = "application/json"
        self.addAuthentication(path, invitations.encode() , http_type,fileContent)
        r = requests.post(url = self.url,  headers=self.header,data=invitations)   
        return r

    def createFulfill(self, documentUuid, invitations):       
        path =  "/api/v1/invitation/" + documentUuid + "/signature"
        http_type = "POST"
        fileContent = "application/json"
        self.addAuthentication(path, invitations.encode() , http_type,fileContent)
        r = requests.post(url = self.url,  headers=self.header,data=invitations)   
        return r

    def getDocumentStatus (self, documentUuid):       
        path =  "/api/v1/document/" + documentUuid
        http_type = "GET"
        fileContent = "application/json"
        payload =""
        self.addAuthentication(path, payload.encode() , http_type,fileContent)
        r = requests.get(url = self.url,  headers=self.header)   
        return r

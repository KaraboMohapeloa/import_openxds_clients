import requests
import json

class Identifier:
    def __init__(self, identifier):
        self.json_file = open('identifier.json')
        self.identifier = identifier
        self.json_body = json.load(self.json_file)
        self.json_body["postUpdateIdentifiers"][0]["identifier"]=identifier

    def is_identifier_in_openxds(self, openxds_session):
        api_url = openxds_session.isIdentifierinXDSURL+self.identifier
        headers = {'Content-Type': 'application/json'}
        response = requests.get(api_url, headers=headers)
        if(response.status_code == 200):
            if(response.text == "false"):
                return False
            else:
                return True
        else:
            print("Print failed to validate patient identifier error code: ")
            print(response.status_code)
            return False # Avoid sending duplicate
    
    def send_to_openxds(self, openxds_session):
        response = requests.post(openxds_session.mpixds_syncURL, json=self.json_body, auth=(openxds_session.mpixds_username, openxds_session.mpixds_password))
        if(response.status_code == 200):
            return True
        else:
            return False

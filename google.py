# Accesses the Google Drive API as the passed user and displays the permissions for a file
# Execution: py google.py [user email address] [file ID]

from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from httplib2 import Http
import json
import sys

# Request permission scopes and load the credentials
scopes = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'private/service_account.json', scopes=scopes)

# Command-line arguments for the script
user = sys.argv[1]
fileId = sys.argv[2]
print ("You are now executing this as " + user + " via a service account")

delegated_credentials = credentials.create_delegated(user)
http_auth = delegated_credentials.authorize(Http())

print ("Accessing permissions for file " + fileId + "...")

drive = build('drive', 'v3', http=http_auth)
response = drive.permissions().list(fileId=fileId).execute()
print (json.dumps(response, sort_keys=True, indent=3))

exit(0)
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

# Become the specified user and delegate the credentials
delegated_credentials = credentials.create_delegated(user)
http_auth = delegated_credentials.authorize(Http())

# Grab the permissions from the specified file and spit them out
drive = build('drive', 'v3', http=http_auth)
response = drive.permissions().list(fileId=fileId).execute()
print (json.dumps(response, sort_keys=True, indent=3))

exit(0)
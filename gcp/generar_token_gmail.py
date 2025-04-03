
# Script para generar token_gmail.json usando credentials.json (OAuth Gmail API)

import os
import json
import pickle
import pathlib
from google_auth_oauthlib.flow import InstalledAppFlow

# SCOPES necesarios para Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    creds = None
    if not os.path.exists('credentials.json'):
        print("⚠️ No se encontró 'credentials.json'.")
        return

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # Guardar token
    with open('token_gmail.json', 'w') as token:
        token.write(creds.to_json())
    print("✅ Token generado correctamente y guardado como 'token_gmail.json'.")

if __name__ == '__main__':
    main()

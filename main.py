import os
# import requests
import google.auth.transport.requests
import google.oauth2.id_token
# import requests_toolbelt.adapters.appengine

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
# requests_toolbelt.adapters.appengine.monkeypatch()
HTTP_REQUEST = google.auth.transport.requests.Request()

app = FastAPI()

@app.get('/')
async def root(request: Request):
    # Verify Firebase auth.
    # [START age_python_verify_token] 
    id_token = request.headers['Authorization'].split(' ').pop()
    print('id_token:', id_token)
    # claims = google.oauth2.id_token.verify_firebase_token(
    #     id_token, HTTP_REQUEST, audience=os.environ.get('GOOGLE_CLOUD_PROJECT')
    # )

    try:
        claims = google.oauth2.id_token.verify_firebase_token(
            id_token, HTTP_REQUEST, audience='inobram-platform')

        print('claims;', claims)
    except ValueError as err:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"error": str(err)})

    return {'message': 'Hello World'}
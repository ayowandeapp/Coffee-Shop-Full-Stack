# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```
https://coffee-wande.us.auth0.com/authorize?response_type=token&client_id=AfUpesuheGwbC1twM6HcBtqgDFDRDtAt&redirect_uri=https://127.0.0.1:5000/&audience=drinks


ayooluwa71@gmail.com --manager
https://127.0.0.1:5000/#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRockZZX0xrTWRsN1dpcGNXM29LeiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZS13YW5kZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMwZmIyMTNmNTgyOGY2Zjk1NDY2NmZmIiwiYXVkIjoiZHJpbmtzIiwiaWF0IjoxNjYyMjc1NTE0LCJleHAiOjE2NjIyODI3MTQsImF6cCI6IkFmVXBlc3VoZUd3YkMxdHdNNkhjQnRxZ0RGRFJEdEF0Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.FZbD0imYc7GhonrfpuzMIExqE_pzghcjeyPTc8BT_ao4_oEuQcf1DT4EbE4U6HzTWt_a2hzQpzwWCuh6xiDaKwfyDMNtbxYK_6HpJm_jKHp8ssfYqOv-DxJJ-tFJxj-8ywrVsft48Z3qIFITpvbd2J2O8nu6qndMvvhjAOmBap9QciE0-jm3aPJ06SSRkBHNCdj27tPzGK21smpY7Uiw1e8U9cs9zZWK2_GTbNcDANZJy-A8uRFQQZRg6KNy0TDNhKSUhaGtXsq0yD2zVxEFcuwZyiKtLab2emuzbTHrBlCvZPsTVzPBSnE_xcTU0Ojsnr_rEsjBcUF1Hn-Ebl3haQ&expires_in=7200&token_type=Bearer



admin@hotmail.com --barista
https://127.0.0.1:5000/#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRockZZX0xrTWRsN1dpcGNXM29LeiJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZS13YW5kZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMwZmI0MmFhOTE2ZDUzMmYwNmFjZWVhIiwiYXVkIjoiZHJpbmtzIiwiaWF0IjoxNjYyMjc1NjEyLCJleHAiOjE2NjIyODI4MTIsImF6cCI6IkFmVXBlc3VoZUd3YkMxdHdNNkhjQnRxZ0RGRFJEdEF0Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.JG30KZtnyNWcTKyYdcnhhZsQ7pZW5ayxNXnK97_EJpfK7yjnS-VgHwt85pQb9oEgs8hIAxxTaC3oHJydy3XJDUP41QyjlQppY_GvjwgJQ4Zn_inTdZvAevEDp4kwbqKMbApPFu0nsq8b4rl3XJBNq8eeU8VeLbQRMWTRXSX9tSklsQ0nILwb2o3A1Vc2w7r1LuQUWPqGOyJtRvRzbI7_Je1QVQogHcgDPFesDNViXBzNtZ3dyeS2cWDfSE43U4wyQY6SSELVAE9y9OxtU2BYZz_SgQLXbEnCkLA944GTZeAO2Gvw0NV9Ri5lBmfvyXSJWeUeUfAcuceug2WaZu5TNQ&expires_in=7200&token_type=Bearer



The `--reload` flag will detect file changes and restart the server automatically.

## Tasks
5-tW5z&J7eg5-Ux

https://manage.auth0.com/dashboard/us/coffee-wande/apis
### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. Create new roles for:
   - Barista
     - can `get:drinks-detail`
     - can `get:drinks`
   - Manager
     - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`

# BLTServer
BioLifeTracker Server

## Installation
Install Python 3 in your computer and add to system path.
Go to this project's root folder in Terminal.
Run this code: ```pip3 install -r requirements.txt```
This will install the required Python modules.

Once it is finished, run this to start the server on localhost:
```python3 manage.py runserver```

## API Endpoints

### Authentication
The supported operations are summarized in the following table:

| Supported Operation | Endpoint | Remarks |
|---------------------|----------|---------|
| Login with Facebook | /auth/facebook/ | POST `{ "access_token" : "" }`|
| Login with Google | /auth/google/ |  POST `{ "access_token" : "" }` |
| Get currently logged-in user | /auth/current_user/ | GET. Determined by the token sent in HTTP Request header. |

### Models
There are a few classes of available models in this server:

| Class Name | URL Prefix |
|------------|------------|
| Project | /projects/ |
| Ethogram | /ethograms/ |
| Behaviour | /behaviours/ |
| Session | /sessions/ |
| Observation | /observations/ |
| Individual | /individuals/ |
| Tag | /tags/ |

For each model class, there are two kinds of viewing mode: **Listing** and **Detail**. 


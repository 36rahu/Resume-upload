import webbrowser
import uuid
from requests import Request


def get_access_token():
    '''Function only give the get request to the agiliq.com and return the corresponding address.And we obtain the access_token from the browser''' 
    params ={ 
        'client_id':'LhDptl2FRdQ1lAmfLY4v8Obb4cbX9DqjgLIDO8erBTYWbkGmq5',
        'redirect_uri':'http://127.0.0.1/callback',
        'client_secret':'i2BwkfoMwEE1YR9ud5kGTVFF9rPvx3aa9KRFWZdWTW00ACHPff',
        'code':'9QvVw2gmYVYDTUVRhihfrMpI5SCfm08QJ2ePSJ4otcLcHFEOjJ'
    }
    auth_url = 'http://join.agiliq.com/oauth/access_token/'
    r = Request('GET',url=auth_url,params=params).prepare()
 
    #rediect to authenticate application
   
    webbrowser.open(r.url)

get_access_token()

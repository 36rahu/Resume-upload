import webbrowser
import uuid
from requests import Request


def get_code():
    '''Function only give the get request to the agiliq,com and return the corresponding address.And we obtain the code from the browser''' 
    state = uuid.uuid4().get_hex()
    params ={ 
        'client_id':'LhDptl2FRdQ1lAmfLY4v8Obb4cbX9DqjgLIDO8erBTYWbkGmq5',
        'redirect_uri':'http://127.0.0.1/callback',
        'state': state
    }
    auth_url = 'http://join.agiliq.com/oauth/authorize/'
    r = Request('GET',url=auth_url,params=params).prepare()
 
    #rediect to authenticate application
   
    webbrowser.open(r.url)


get_code()

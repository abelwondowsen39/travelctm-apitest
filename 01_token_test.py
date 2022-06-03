import json
import requests

# method for testing the token(SCS-447)
def test_get_token():

    url = 'https://stage-content-services.ctmna-apps.net/api/v1/token'

    CLIENT_ID = 'b2103ba1-e616-4231-bcb8-4d4a2a2a53b9' 
    CLIENT_SECRET = 'Uh8SAC5n1E0HmNihqGUTlXVasIQOFYsdJekcyjlM'

    data = {
        'client_id':CLIENT_ID,
        'client_secret':CLIENT_SECRET
    }

    response = requests.post(url,data=data)
    json_res = response.json()
    # checks whether the staus code is 200
    assert response.status_code == 200 , "Status code is not 200"
    # checks the correct data structure is followed which is as belows
    # {
    #  'type':'',
    #  'id':'',
    #  'attributes':{
    #    'token':'',
    #    'token_type':'',
    #    'expires_in':''
    #   }
    # }
    assert json_res['data'] != None, "Data not in response body"
    assert json_res['data']['id'] != None , "Id not found in request body data"
    assert json_res['data']['attributes'] != None , "Attributes not found in request body data"
    assert json_res['data']['attributes']['token'] != None , "token not found in request body data attributes"
    assert json_res['data']['attributes']['token_type'] != None , "token_type not found in request body data attributes"
    assert json_res['data']['attributes']['expires_in'] != None , "expires_in not found in request body data attributes" 
    
    # checks whether the token exists
    # checks whether the type is token
    assert json_res['data']['type'] == "Token" ,"Type of data is not Token"
    # checks whether the token length is not 0
    assert len(json_res['data']['attributes']['token']) != 0 , "token does not have a value"
    # checks whether the token is 1025 characters long
    # assert len(json_res['data']['attributes']['token']) == 1025 ,"token length must always be 1025 characters"
    # checks whether the token expiry date is 30 days
    assert json_res['data']['attributes']['expires_in'] == '2592000','token doesnt expire in 30 days'
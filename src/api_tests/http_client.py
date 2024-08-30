import requests
import json

class HttpClient:
  def __init__(self, base_url, client_id, client_secret):
    self.base_url = base_url
    self.access_token = self.get_access_token(client_id, client_secret)
    self.default_headers = {
    'Authorization': 'Bearer {}'.format(self.access_token),
    'Content-Type': 'application/json'
}

  def get_access_token(self,client_id, client_secret):
    #client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
    header = {'accept': 'application/json'}
    response = requests.post(f'{self.base_url}/v2/token', headers=header, json=post_data)
    print("Get access token response {}".format(response.status_code))
    token_json = response.json()
    return token_json["data"]["access_token"]

  def get(self, endpoint, param=None, status_code = 200):
    response = requests.get(f'{self.base_url}{endpoint}', headers=self.default_headers, json=param)
    assert response.status_code == status_code
    return response.json()

  def post(self, endpoint, param=None, status_code = 200):
    response = requests.post(f'{self.base_url}{endpoint}', headers=self.default_headers, json=param)
    assert response.status_code == status_code
    return response.json()

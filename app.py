import requests
import json
from flask import Flask, render_template
app = Flask(__name__)


#In the first step, we are calling the /create endpoint to create a provider and generate 
# an access token. As per the requirement of this task, access to /company endpoint is blocked
url_token = "https://finch-sandbox-se-interview.vercel.app/api/sandbox/create"
payload_token = json.dumps({"provider": "gusto","products": ["directory","individual","employment","payment","pay_statement"]})
headers_token = {'Content-Type': 'application/json'}
response_token_ = requests.request("POST", url_token, headers=headers_token, data=payload_token)
response_token_json = json.loads(response_token_.content)
access_token = json.dumps(response_token_json["access_token"])

#stripping access token and storing it the variable
access_token = access_token.replace('"','') 

#building the access token for subsequent calls
auth_token_string='Bearer ' + access_token 


#defining different routs
@app.route('/')
def home():
    url = "https://finch-sandbox-se-interview.vercel.app/api/employer/directory"
    payload={}
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Authorization': auth_token_string
            }
    response = requests.get(url, headers=headers, data=payload)
    response_json = json.loads(response.content)
    return render_template('home.html',data=response_json)

#Rendering an employee page to display employee data
@app.route('/employee')
def employee():
    url = "https://finch-sandbox-se-interview.vercel.app/api/employer/employment"
    payload = json.dumps({"requests": [{"individual_id": "3f112ab2-8f0c-4096-9d66-ac5a8c4e7f6a"}]})
    headers = {
        'Authorization': auth_token_string,
        'Content-Type': 'application/json'
        }
    response = requests.post(url, headers=headers, data=payload)
    response_json = json.loads(response.content)
    return render_template('employee.html',data=response_json)


@app.route('/company')
def company():
    return render_template('company.html')

if __name__ == '__main__':
   app.run()
import boto3
import json

# Create the client
client = boto3.client('secretsmanager', region_name='ap-south-1') 

# Get secret
response = client.get_secret_value(SecretId='Fleet-APIUser',)

# Parse the SecretString as JSON
secret_dict = json.loads(response['SecretString'])
print(secret_dict)

# Extract the API token
api_token = secret_dict['API token']
print(api_token)
import boto3
import json
from botocore.exceptions import ClientError

# This snipped of code started with a template provided by AWS.
# If I were going to redo my work, I'd refactor this to take an argument for 
# the secret name.

def get_secret():
    secret_name = "YOUR_SECRET_NAME"
    endpoint_url = "https://secretsmanager.us-west-2.amazonaws.com" # Replace with your endpoint.
    region_name = "us-west-2"  # Replace with your region.

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager',
                            region_name=region_name,
                            endpoint_url=endpoint_url
                            )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
    else:
        # Decrypted secret using the associated KMS CMK
        # Depending on whether the secret was a string or binary, one of these fields will be populated
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']
        
        print('\n' + '#'*25 + '\n')
        
        # get_secret_value_response is a dictionary
        
        for key, value in get_secret_value_response.items():
            if key == 'SecretString':
                
                print('key: {}'.format(key))
                for sub_key, sub_value in json.loads(value).items():
                    print('\tkey: {}'.format(sub_key))
                    print('\tvalue: {}'.format(sub_value))
                    
                continue
                
            elif key == 'ResponseMetadata':
                
                print('key: {}'.format(key))
                
                for sub_key, sub_value in value.items():
                    if sub_key == 'HTTPHeaders':
                        print('\t' + 'key: {}'.format(sub_key))
                        
                        for header_key, header_value in sub_value.items():
                            print('\t'*2 + 'key: {}'.format(header_key))
                            print('\t'*2 + 'value: {}'.format(header_value))
                    
                    else: 
                        print('\t' + 'Key'': {}'.format(sub_key))
                        print('\t' + 'Value: {}'.format(sub_value))
                    
                    continue                    
                            
                continue
                
            else:
                    
                print('key: {}'.format(key))
                print('value: {}'.format(value))
        
        ###########
        ### I'm relatively new to python.
        ### So, I'll apologize for not using docstrings.
        ### I'll get better, I promise.
        ###########
        ### These are the keys available in AWS Secrets Manager.
        ### Though, this was when I added my own secret text.
        ###########
        
        print('\n' + '#'*25 + '\n')
        
        print('Keys available in AWS SecretsManager:\n')
        for key in get_secret_value_response.keys():
            print(key)
        
        print('\n' + '#'*25 + '\n')
        
        ###########
        # The value of SecretString is a JSON-formatted string.
        # To use it as a dictionary with key/value pairs, it must be converted.
        # The json library has a load function that does this.
        ###########
        
        secret_dict = json.loads(secret)
        
        for key in secret_dict.keys():
            print(key)
        
        print('\n' + '#'*25 + '\n')
            
        for key, value in secret_dict.items():
            print('Key: {}'.format(key))
            print('Value: {}'.format(value))
        
        print('\n' + '#'*25 + '\n')
        
    return
            
get_secret()

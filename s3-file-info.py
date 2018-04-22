import boto3    # AWS Python3 SDK
import botocore # AWS Python3 SDK 

BUCKET_NAME = 'my_s3_bucket_name' # replace with your bucket name
s3 = boto3.client('s3')

# Returns a Dictionary of Key/Value Pairs
# The keyword arguments:
#   Bucket is the bucket name.  S3 uses a global namespace.
#   Delimiter limits the depth of the values returned to the top.  
#     Without the Delimiter, a list of all the bucket's contents will be returned.
#     Adding a value of '/' returns only the values at the top of the tree.

folders = s3.list_objects_v2(Bucket=BUCKET_NAME,
                             Delimiter='/')

for key, value in folders.items():
    if type(value) is dict:
        print('Key: {}\nValue: '.format(key))
        
        for key, value in value.items():
            
            if type(value) is dict:
                print('Key: {}\nValue: '.format(key))
                
                for key, value in value.items():
                    print('\tKey: {}\n\tValue: {}\n'.format(key, value))
                    
                continue
                
            print('\tKey: {}\n\tValue: {}\n'.format(key, value))
            
        continue
        
    elif type(value) is list:
        for item in value:
            if type(item) is dict:
                print('Key: {}\nValue: '.format(key))
        
                for key, value in item.items():
            
                    if type(value) is dict:
                        print('Key: {}\nValue: '.format(key))
                
                        for key, value in value.items():
                            print('\tKey: {}\n\tValue: {}\n'.format(key, value))
                    
                        continue
                    else:
                        print('\tKey: {}\n\tValue: {}\n'.format(key, value))
                
                # print('\tKey: {}\n\tValue: {}\n'.format(key, value))
            
            continue
        
        continue
        
    print('Key: {}\nValue: {}\n'.format(key, value))
    

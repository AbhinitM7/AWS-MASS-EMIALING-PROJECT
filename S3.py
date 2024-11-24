s3 = boto3.client('s3') 
 
# Get recipient list from S3 
def get_recipient_list(bucket_name, key): 
    response = 
s3.get_object(Bucket=bucket_name, Key=key) 
    recipient_list = 
response['Body'].read().decode('utf
8').splitlines() 
    return recipient_list 

import boto
keyId = "your_aws_access_key_id"
sKeyId= "your_aws_secret_key_id"
conn = boto.connect_s3(keyId,sKeyId) #Connect to S3
buckets = conn.get_all_buckets() #Get the bucket list
for i in buckets:
 print(i.name)

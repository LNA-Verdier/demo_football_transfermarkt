from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("S3Access") \
    .config("spark.hadoop.fs.s3a.endpoint", "https://minio.lab.sspcloud.fr") \
    .config("spark.hadoop.fs.s3a.access.key", os.environ["AWS_ACCESS_KEY_ID"]) \
    .config("spark.hadoop.fs.s3a.secret.key", os.environ["AWS_SECRET_ACCESS_KEY"]) \
    .config("spark.hadoop.fs.s3a.session.token", os.environ["AWS_SESSION_TOKEN"]) \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()



'''
s3 = boto3.client("s3",endpoint_url = 'https://'+'minio.lab.sspcloud.fr',
                  aws_access_key_id= os.environ["AWS_ACCESS_KEY_ID"], 
                  aws_secret_access_key= os.environ["AWS_SECRET_ACCESS_KEY"], 
                  aws_session_token = os.environ["AWS_SESSION_TOKEN"]
                 )
'''
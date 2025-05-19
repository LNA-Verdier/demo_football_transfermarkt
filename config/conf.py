from pyspark.sql import SparkSession
import os
import json
from types import SimpleNamespace

def create_spark_session():
    spark = SparkSession.builder \
        .appName("MyApp") \
        .config("spark.hadoop.fs.s3a.endpoint", "https://minio.lab.sspcloud.fr") \
        .config("spark.hadoop.fs.s3a.access.key", os.environ["AWS_ACCESS_KEY_ID"]) \
        .config("spark.hadoop.fs.s3a.secret.key", os.environ["AWS_SECRET_ACCESS_KEY"]) \
        .config("spark.hadoop.fs.s3a.session.token", os.environ["AWS_SESSION_TOKEN"]) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()
    return spark


config_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "s3-paths.json")
with open(os.path.abspath(config_path), "r") as f:
    config = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
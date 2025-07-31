import boto3, os
from dotenv import load_dotenv

def upload_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    # Load .env file
    load_dotenv(os.path.dirname(os.path.abspath(__file__))+'/.env')

    # Get credentials from environment variables
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_DEFAULT_REGION")
    # print(aws_access_key, aws_secret_key, aws_region)
    # return
    # Create an S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id = aws_access_key,
        aws_secret_access_key = aws_secret_key,
        region_name = aws_region
    )

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
        return True
    except Exception as e:
        print(f"Failed to upload {file_name} to {bucket}/{object_name}: {e}")
        return False
    # Example usage
    
# Note: Ensure that you have configured your AWS credentials and have the necessary permissions to upload files to the specified S3 bucket.
# Make sure to install boto3 if you haven't already:
# pip install boto3
# This script uploads a file to an AWS S3 bucket using the boto3 library.
# Ensure you have the AWS credentials configured in your environment or use an IAM role with the necessary permissions.
# The script defines a function `upload_to_s3` that takes the file name, bucket name, and an optional object name.
# It creates an S3 client and attempts to upload the specified file to the given bucket.
# If the upload is successful, it prints a success message; otherwise, it prints an error message.
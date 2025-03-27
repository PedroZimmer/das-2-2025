import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region."""
    try:
        # Create S3 client
        s3_client = boto3.client('s3', region_name=region)
        
        # Create bucket
        if region:
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        else:
            response = s3_client.create_bucket(Bucket=bucket_name)
        
        print(f"Bucket '{bucket_name}' created successfully.")
        return response
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    bucket_name = "pedro23082004"
    region = "us-west-1"  # Specify your desired region
    create_s3_bucket(bucket_name, region)
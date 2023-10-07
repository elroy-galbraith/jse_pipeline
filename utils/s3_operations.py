import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3')

def list_s3_files(bucket_name):
    """
    List all files in the specified S3 bucket.

    Parameters:
    - bucket_name (str): Name of the S3 bucket.

    Returns:
    - List of file names in the bucket.
    """
    s3_client = boto3.client('s3')
    files = []

    bucket_name = "aeonllmbucket"
    prefix = "JSE_Financials/input_financials"
    extension = ".pdf"  # Hardcoding to only search for PDFs

    # List objects within the specified bucket with the specified prefix
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    for page in pages:
        for obj in page.get('Contents', []):
            if obj['Key'].endswith(extension):
                files.append(obj['Key'])

    return files

def select_file_from_s3(files):
    selected_idx = int(input("Enter the number of the PDF you want to select: ")) - 1
    selected_file = files[selected_idx]
    # Return the complete S3 path
    return f"s3://aeonllmbucket/{selected_file}"

def upload_file_to_s3(file_name, bucket_name, s3_file_name=None):
    """
    Upload a local file to an S3 bucket.

    Parameters:
    - file_name (str): Path to the local file.
    - bucket_name (str): Name of the destination S3 bucket.
    - s3_file_name (str, optional): Desired file name in the S3 bucket. If None, uses the local file name.

    Returns:
    - Response from the upload operation.
    """
    # Implementation here

def delete_file_from_s3(bucket_name, file_name):
    """
    Delete the specified file from the S3 bucket.

    Parameters:
    - bucket_name (str): Name of the S3 bucket.
    - file_name (str): Name of the file to delete.

    Returns:
    - Response from the delete operation.
    """
    # Implementation here

# (You can add more S3 related functions as needed)

if __name__ == "__main__":
    # This block is for testing the functions individually if needed
    pass

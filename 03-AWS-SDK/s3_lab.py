#!/usr/bin/env python3
# 03-AWS-SDK/s3_lab.py
"""
Simple Boto3 script for S3:
- List buckets
- Create bucket (if not exists)
- Upload file (Ahmed_Hossam_CV.pdf or test.txt)
- Generate a presigned URL (optional)
"""
import boto3
from botocore.exceptions import ClientError
import os

# Configuration
BUCKET_NAME = "ahmed-sdk-lab-2025-01"   # Change to a unique name if needed
REGION = "eu-central-1"
FILE_TO_UPLOAD = "Ahmed_Hossam_CV.pdf"  # or "test.txt"
PRESIGN_EXPIRES = 7 * 24 * 60 * 60      # 7 days in seconds

def ensure_bucket(s3_client, bucket_name, region):
    try:
        # Create bucket with region support
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"Bucket created: {bucket_name}")
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code")
        if code == "BucketAlreadyOwnedByYou":
            print(f"Bucket already exists and is owned by you: {bucket_name}")
        elif code == "BucketAlreadyExists":
            print(f"Bucket name already exists globally. Choose another name.")
            raise
        else:
            print("Create bucket error:", e)
            raise

def upload_file(s3_client, bucket_name, filename):
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return False
    try:
        s3_client.upload_file(filename, bucket_name, os.path.basename(filename))
        print(f"Uploaded: {filename} -> s3://{bucket_name}/{os.path.basename(filename)}")
        return True
    except ClientError as e:
        print("Upload error:", e)
        return False

def list_buckets_and_objects(s3_client, bucket_name):
    resp = s3_client.list_buckets()
    print("Buckets in account:")
    for b in resp.get("Buckets", []):
        print(" -", b["Name"])
    print("\nObjects in", bucket_name, ":")
    try:
        objects = s3_client.list_objects_v2(Bucket=bucket_name)
        for obj in objects.get("Contents", []):
            print(f" - {obj['Key']}  (size={obj['Size']})")
    except ClientError as e:
        print("List objects error (maybe empty or access issue):", e)

def generate_presigned_url(s3_client, bucket_name, object_key, expires_in):
    try:
        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=expires_in,
        )
        print("\nPresigned URL (valid for {} seconds):\n{}".format(expires_in, url))
        return url
    except ClientError as e:
        print("Presign error:", e)
        return None

def main():
    session = boto3.session.Session()
    s3_client = session.client("s3", region_name=REGION)

    print("Listing buckets (before):")
    list_buckets_and_objects(s3_client, BUCKET_NAME)

    # Ensure bucket exists (create if not)
    try:
        ensure_bucket(s3_client, BUCKET_NAME, REGION)
    except Exception:
        print("Bucket creation failed or bucket name conflict. Exiting.")
        return

    # Upload file
    uploaded = upload_file(s3_client, BUCKET_NAME, FILE_TO_UPLOAD)
    if not uploaded:
        print("Upload failed or file missing. Exiting.")
        return

    # List objects to verify
    print("\nListing contents after upload:")
    list_buckets_and_objects(s3_client, BUCKET_NAME)

    # Generate presigned URL
    presigned = generate_presigned_url(s3_client, BUCKET_NAME, os.path.basename(FILE_TO_UPLOAD), PRESIGN_EXPIRES)
    if presigned:
        print("\nYou can open the presigned URL in a browser to download the file.")

if __name__ == "__main__":
    main()

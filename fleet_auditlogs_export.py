from datetime import datetime, timedelta, timezone
import boto3
import json
import requests
import subprocess
import os
import sys

API_URL = "https://fleet.auditcue.com/api/v1/fleet/activities"
SECRET_NAME = "Fleet-APIUser"
REGION_NAME = "ap-south-1"
S3_BUCKET = "fleet-auditlog-bucket"

def calculate_range():
    return (datetime.now(timezone.utc) - timedelta(hours=12)).isoformat(timespec='seconds').replace('+00:00', 'Z')

def get_secret():
    print("Fetching API token from AWS Secrets Manager...")
    client = boto3.client('secretsmanager', region_name=REGION_NAME)
    try:
        secret_response = client.get_secret_value(SecretId=SECRET_NAME)
        secret_string = json.loads(secret_response['SecretString'])
        api_token = secret_string.get("API token")
        if not api_token:
            print("Error: API token not found.")
            sys.exit(1)
        return api_token
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        sys.exit(1)

def list_activities(api_token, since_time):
    print("Fetching activities from Fleet API...")
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")
        sys.exit(1)

    try:
        data = response.json()
    except ValueError:
        print("Error: Invalid JSON response.")
        sys.exit(1)

    activities = data.get("activities", [])
    filtered = [a for a in activities if a.get("created_at", "") >= since_time]

    if not filtered:
        print("No activities found in the last 12 hours.")
        return

    filename = f"fleet_activities_{datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%SZ')}.json"
    with open(filename, 'w') as f:
        json.dump(filtered, f, indent=2)
    print(f"Saved to {filename}.")

    archive_name = f"{filename}.tar.gz"
    subprocess.run(['tar', '-czf', archive_name, filename], check=True)

    try:
        boto3.client('s3').upload_file(archive_name, S3_BUCKET, archive_name)
        print("Uploaded to S3.")
        os.remove(filename)
        os.remove(archive_name)
    except Exception as e:
        print(f"Upload failed: {e}")
        sys.exit(1)

def main():
    since_time = calculate_range()
    api_token = get_secret()
    list_activities(api_token, since_time)

if __name__ == "__main__":
    main()
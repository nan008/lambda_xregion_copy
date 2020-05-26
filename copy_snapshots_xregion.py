import boto3
import datetime

client = boto3.client('ec2')

def lambda_handler(event, context):
    response = client.describe_snapshots(
                    Filters=[
                        {
                            'Name': 'tag:aws:dlm:lifecycle-policy-id',
                            'Values': ['policy-XXXXXXX']
                        },
                    ]
                )
    print(response)
    
    for snapshot in response["Snapshots"]:
        snapshot_date = snapshot['StartTime']
        if snapshot_date.date() == datetime.date.today():
            print("created today")
            snapshot_id = snapshot["SnapshotId"]
            destination_client = boto3.client('ec2', region_name='us-east-1')
            res = destination_client.copy_snapshot(SourceSnapshotId=snapshot_id,
                                                  SourceRegion='us-west-2')
        else:
            print("not created today")
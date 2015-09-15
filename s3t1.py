#!/usr/bin/env python
import boto3

s3=boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

data=open('/root/shootproxy.sh','r')
s3.Bucket('buckett1').put_object(Key='shootproxy',Body=data)

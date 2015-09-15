#!/usr/bin/env python
# encoding: utf-8

import boto3
client = boto3.client('ec2')
response = client.describe_instances(InstanceIds=["i-760710dd"])
onwerid = response['Reservations'][0].get('OwnerId')
print 'OnwerId is %s' % onwerid

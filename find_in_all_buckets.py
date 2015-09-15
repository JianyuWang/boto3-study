#!/usr/bin/env python
# encoding: utf-8

import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    for obj in bucket.objects.filter(Prefix='free'):
        print('{0}:{1}'.format(bucket.name,obj.key))

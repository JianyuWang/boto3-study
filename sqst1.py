#!/usr/bin/env python
# encoding: utf-8
import boto3
sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='test',Attributes={'DelaySeconds':'5'})
print (queue.url)
print (queue.attributes.get('DelaySeconds'))


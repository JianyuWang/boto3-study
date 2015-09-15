#!/usr/bin/env python
# encoding: utf-8

import boto3
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test')
queue.send_message(MessageBody='world')
queue.send_message(MessageBody='boto3',MessageAttributes={
    'Author':{
        'StringValue': 'tom',
        'DataType': 'String'
        }
    })
for i in xrange(0,10):
    queue.send_message(MessageBody='%s' % i)


#!/usr/bin/env python
# encoding: utf-8

import boto3
sqs=boto3.resource('sqs')
queue=sqs.get_queue_by_name(QueueName='test')
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    author_text=''
    if message.message_attributes is not None:
        print('%s' % message.message_attributes)
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)
    print('hello,{0}!{1}'.format(message.body,author_text))
   # message.delete()

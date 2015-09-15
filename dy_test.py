#!/usr/bin/env python
# encoding: utf-8

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookstest')
#table.put_item(
#    Item={
#        'IBSN':'BSG18909',
#        'language':'japanese',
#        'name':'fate'
#    }
#)
response = table.get_item(
    Key={
        'IBSN':'BSG18909',
        'language':'japanese'
    }
)
item = response['Item']
print(item)
print(response)

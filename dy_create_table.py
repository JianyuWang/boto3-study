#!/usr/bin/env python
# encoding: utf-8

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName="users",
    KeySchema=[
        {
            'AttributeName':'username',
            'keyType':'HASH'
        },
        {
            'AttributeName':'last_name',
            'keyType':'RANGE'
        }
    ]
    KeySchema=[
        {
            'AttributeName':'username',
            'keyType':'HASH'
        },
        {
            'AttributeName':'last_name',
            'keyType':'RANGE'
        }
    ]

)

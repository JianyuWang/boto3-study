#!/usr/bin/env python
# encoding: utf-8

import boto3
ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-760710dd')
instance.

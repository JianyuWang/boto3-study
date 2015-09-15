#!/usr/bin/env python
# encoding: utf-8

import boto3
import boto3.session
import threading

class MyTask(threading.Thread):
    def run(self,bucketname):
        session = boto3.session.Session()
        s3 = session.resource('s3')
        bucket1 = s3.Bucket('%s' % bucketname)
        print(bucket1.creation_date)
if __name__ == "__main__":
    mytask = MyTask()
    mytask.run("buckett1")




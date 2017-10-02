import boto3.rds
import boto3.iam
import boto3.ec2
import boto3.sqs

from config import REGION


def EC2Connection():
    return boto3.ec2.connect_to_region(REGION)

def RDSConnection():
    return boto3.rds.connect_to_region(REGION)

def IAMConnection():
    return boto3.iam.connect_to_region('universal')

def SQSConnection():
    return boto3.sqs.connect_to_region(REGION)
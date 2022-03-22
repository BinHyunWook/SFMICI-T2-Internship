import json
import logging
import datetime
import dateutil.tz
import boto3

def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.debug(json.dumps(event))
    jobid = event["CodePipeline.job"]["id"]
    ec2 = boto3.client('ec2')
    
    try:
        response = boto3.client('codepipeline').put_job_success_result(jobId=jobid)
        logger.debug(response)
        return 200
    except:
        response = boto3.client('codepipeline').put_job_failure_result(jobId=jobid, failureDetails=detail)
        logger.debug(response)
        return 404
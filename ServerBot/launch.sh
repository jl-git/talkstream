#!/bin/bash
AMI=ami-08111162
NUM_INSTANCES=1
aws configure set aws_access_key_id AKIAISOAOQKZPNRSDTCA
aws configure set aws_secret_access_key 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
aws configure set default.region us-east-1
aws ec2 run-instances --image-id ${AMI} --count $NUM_INSTANCES --instance-type t2.micro --user-data file://install.sh --key-name SSS
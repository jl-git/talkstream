#!/bin/bash
AMI=ami-08111162
NUM_INSTANCES=1
aws configure set aws_access_key_id $XYZ
aws configure set aws_secret_access_key $XYZ
aws configure set default.region $XYZ
aws ec2 run-instances --image-id ${AMI} --count $NUM_INSTANCES --instance-type t2.micro --user-data file://install.sh --key-name $XYZ
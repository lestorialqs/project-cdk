#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import DefaultStackSynthesizer, Environment
from proyecto_cdk.proyecto_cdk_stack import VmStack

app = cdk.App()

synthesizer = DefaultStackSynthesizer(
    deploy_role_arn='arn:aws:iam::708642711016:role/LabRole',
    cloud_formation_execution_role='arn:aws:iam::708642711016:role/LabRole',
    lookup_role_arn='arn:aws:iam::708642711016:role/LabRole',
    file_asset_publishing_role_arn='arn:aws:iam::708642711016:role/LabRole',
    image_asset_publishing_role_arn='arn:aws:iam::708642711016:role/LabRole',
    qualifier='lab'
)

VmStack(
    app, 
    "VmStack", 
    synthesizer=synthesizer,
    env=cdk.Environment(
        account="708642711016",
        region="us-east-1"
    )
)

app.synth()

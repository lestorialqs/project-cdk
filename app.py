#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import DefaultStackSynthesizer, Environment
from proyecto_cdk.proyecto_cdk_stack import VmStack

app = cdk.App()






VmStack(app, "VmStack", env=cdk.Environment( account="708642711016", region="us-east-1") )

app.synth()

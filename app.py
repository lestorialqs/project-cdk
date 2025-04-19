import aws_cdk as cdk

from aws_cdk import DefaultStackSynthesizer

from proyecto_cdk.proyecto_cdk_stack import VmStack


app = cdk.App()

custom_execution_role = "arn:aws:iam::708642711016:role/LabRole"

synth = DefaultStackSynthesizer(
    qualifier="projcdk",
    cloud_formation_execution_role=custom_execution_role
)


VmStack(app, "VmStack",
    env=cdk.Environment(account="708642711016", region="us-east-1"),
    synthesizer=synth
)   

app.synth()
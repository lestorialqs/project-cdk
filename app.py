import aws_cdk as cdk

from proyecto_cdk.proyecto_cdk_stack import VmStack


app = cdk.App()

custom_execution_role = 'arn:aws:iam::708642711016:role/LabRole'


VmStack(app, "VmStack",
    env=cdk.Environment(account="708642711016", region="us-east-1"),
    role=custom_execution_role
)

app.synth()
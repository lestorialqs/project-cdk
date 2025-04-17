import aws_cdk as cdk

from proyecto_cdk.proyecto_cdk_stack import VmStack

app = cdk.App()
VmStack(app, "VmStack",
    env=cdk.Environment(account="708642711016", region="us-east-1"),
    execute_role_arn="arn:aws:iam::708642711016:role/LabRole"  # Especifica el ARN aquí
)

app.synth()
import aws_cdk as cdk
from constructs import Construct



class TestStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, *, execute_role_arn: str = None, **kwargs):
        super().__init__(scope, id, execute_role_arn=execute_role_arn, **kwargs)

        
app = cdk.App()
TestStack(app, "TestStack",
    env=cdk.Environment(account="708642711016", region="us-east-1"),
    execute_role_arn="arn:aws:iam::708642711016:role/LabRole" 
)

app.synth()
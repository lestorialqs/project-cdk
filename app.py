import aws_cdk as cdk
from constructs import Construct



class TestStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, str = None, **kwargs):
        super().__init__(scope, id, **kwargs)

        
app = cdk.App()
TestStack(app, "TestStack",
    env=cdk.Environment(account="708642711016", region="us-east-1")
)

app.synth()
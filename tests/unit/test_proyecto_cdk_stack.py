import aws_cdk as core
import aws_cdk.assertions as assertions

from proyecto_cdk.proyecto_cdk_stack import ProyectoCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in proyecto_cdk/proyecto_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProyectoCdkStack(app, "proyecto-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

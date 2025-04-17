from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct
import aws_cdk.aws_iam as iam

class VmStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Obtener VPC predeterminada
        vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)

        # Obtener una subnet pública de esa VPC
        subnet_id = vpc.public_subnets[0].subnet_id

        # Grupo de seguridad
        sg = ec2.SecurityGroup(self, "SG",
            vpc=vpc,
            description="Permitir SSH y HTTP",
            allow_all_outbound=True
        )
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "SSH")
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "HTTP")

        # Instancia EC2 usando CfnInstance
        ec2.CfnInstance(self, "EC2Instance-aws-cdk",
            image_id="ami-0f2d4b21b93e88520",  # Cloud9 Ubuntu22 mas reciente
            instance_type="t2.micro",
            key_name="vockey",
            subnet_id=subnet_id,
            security_group_ids=[sg.security_group_id],
            block_device_mappings=[{
                "deviceName": "/dev/xvda",
                "ebs": {
                    "volumeSize": 20,
                    "volumeType": "gp2"
                }
            }]
        )
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct
import aws_cdk.aws_iam as iam

class VmStack(Stack):
    def __init__(self, scope: Construct, id: str, *, execute_role_arn: str = None, **kwargs):
        super().__init__(scope, id, execute_role_arn=execute_role_arn, **kwargs)

        # Traer VPC predeterminada
        vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)

        # Grupo de seguridad para puertos 22 y 80
        sg = ec2.SecurityGroup(self, "SG",
            vpc=vpc,
            description="Permitir SSH y HTTP",
            allow_all_outbound=True
        )
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "SSH")
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "HTTP")

        # AMI Ubuntu 22.04 (us-east-1) - reemplaza si tienes otra
        ami = ec2.MachineImage.generic_linux({
            "us-east-1": "ami-0c8e5b591b8537909"
        })

        # Crear instancia EC2
        ec2.Instance(self, "Instance-CDK",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ami,
            vpc=vpc,
            security_group=sg,
            key_name="vockey",  # Asegúrate de que ya exista en EC2 > Key Pairs
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(20)
                )
            ]
        )
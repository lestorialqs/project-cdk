from aws_cdk import core
import aws_cdk.aws_ec2 as ec2

class VmStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Obtener VPC predeterminada
        vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)

        # Obtener una subnet pública de esa VPC
        subnet_id = vpc.public_subnets[0].subnet_id

        # Crear grupo de seguridad
        sg = ec2.SecurityGroup(self, "SG",
            vpc=vpc,
            description="Permitir SSH y HTTP",
            allow_all_outbound=True
        )
        # Permitir el acceso SSH y HTTP
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "SSH")
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "HTTP")

        # Crear instancia EC2 usando ec2.Instance
        instancia = ec2.Instance(self, "EC2Instance-aws-cdk-stack",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.generic_linux({
                "us-east-1": "ami-0f2d4b21b93e88520"  # ID de la imagen AMI
            }),
            vpc=vpc,
            vpc_subnets={"subnet_id": subnet_id},
            security_group=sg,
            key_name="vockey",
            instance_name="Prueba-Instance-CDK"  # Asignar nombre a la instancia
        )

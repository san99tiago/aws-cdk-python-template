# External imports
from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ssm,
)
from constructs import Construct


class ExampleStack(Stack):
    """
    Class to create the infrastructure on AWS.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        main_resources_name_id: str,
        deployment_environment: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Input parameters
        self.construct_id = construct_id
        self.main_resources_name_id = main_resources_name_id
        self.deployment_environment = deployment_environment

        # Main methods for the deployment
        self.import_resources()
        self.create_ssm_parameter()

        # Create CloudFormation outputs
        self.generate_cloudformation_outputs()

    def import_resources(self):
        """
        Import the necessary AWS resources to the stack, for referencing them
        towards other resources/configurations.
        """
        # TODO: Only populate if needed (params, secrets, config, etc)
        pass

    def create_ssm_parameter(self):
        """
        Example method to create an AWS SSM Parameter.
        """
        self.example_ssm_parameter: aws_ssm.StringParameter = aws_ssm.StringParameter(
            self,
            "Parameter",
            description=f"Example parameter for {self.main_resources_name_id} in {self.deployment_environment} env",
            parameter_name=f"/{self.deployment_environment}/{self.main_resources_name_id}",
            string_value="Template-Value-Santi-Hello-Friend",
        )

    def generate_cloudformation_outputs(self):
        """
        Method to add the relevant CloudFormation outputs.
        """

        CfnOutput(
            self,
            "DeploymentEnvironment",
            value=self.deployment_environment,
            description="Deployment environment",
        )

        CfnOutput(
            self,
            "SSMParameterName",
            value=self.example_ssm_parameter.parameter_name,
            description="Example SSM Parameter Name",
        )

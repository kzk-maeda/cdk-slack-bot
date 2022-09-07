from aws_cdk import (
    # Duration,
    Stack,
    aws_stepfunctions as _sfn,
    aws_apigateway as _apigw,
)
from constructs import Construct

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        invole_state = _sfn.Pass(
            self, "InvokeState",
            result=_sfn.Result("API Gateway Invokes Step Functions")
        )

        success_state = _sfn.Pass(
            self, "SuccessState",
            result=_sfn.Result("Successfully Invoked")
        )

        machine_definition = invole_state.next(success_state)

        state_machine = _sfn.StateMachine(
            self, "StateMachine",
            definition=machine_definition,
            state_machine_name="APIStepFunctions",
            state_machine_type=_sfn.StateMachineType.EXPRESS
        )

        api = _apigw.StepFunctionsRestApi(
            self, "StepFunctionAPI",
            deploy=True,
            state_machine=state_machine
        )

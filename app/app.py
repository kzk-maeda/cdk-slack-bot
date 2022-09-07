#!/usr/bin/env python3
import os
import aws_cdk as cdk
from app.app_stack import AppStack

from dotenv import load_dotenv
load_dotenv()

app = cdk.App()
AppStack(app, "AppStack",
    env=cdk.Environment(account=os.getenv('AWS_ACCOUNT'), region=os.getenv('AWS_REGION')),
)

app.synth()

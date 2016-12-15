#!/usr/bin/env python
import nose
from test_linchpin_invocation import TestLinchPinInvocation
from test_linchpin_creds import TestLinchPinCredentials
from test_linchpin_env import TestLinchPinEnv
from test_linchpin_inventory_filters import TestLinchPinInventoryFilters
from test_linchpin_api import TestLinchPinAPI
from test_linchpin_cli import TestLinchPinCli 
from test_linchpin_inventory_gen import TestLinchPinInventoryGen 
from test_linchpin_module_os_hot_stack import TestLinchPinModuleOSHotStack 
from test_linchpin_module_output_parser import TestLinchPinModuleOutputParser 
from test_linchpin_module_schema_check import TestLinchPinModuleSchemaCheck

nose.run()
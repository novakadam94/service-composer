### Copyright 2014, MTA SZTAKI, www.sztaki.hu
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###    http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.

""" Dummy Configuration Manager module for OCCO

.. moduleauthor:: Adam Novak <novak.adam@sztaki.mta.hu>

"""

from __future__ import absolute_import

__all__ = [ 'DummyConfigManager' ]

from occo.configmanager import ConfigManager, Command
import occo.util as util
import occo.util.factory as factory
import logging

import occo.constants.status as status

PROTOCOL_ID='dummy'

log = logging.getLogger('occo.configmanager.dummy')

class GetNodeState(Command):
    def __init__(self, instance_data):
        Command.__init__(self)
        self.instance_data = instance_data

    def perform(self, sc):
        return 'ready'

class GetNodeAttribute(Command):
    def __init__(self, node_id, atribute):
        Command.__init__(self)
        self.node_id = node_id
        self.atribute = atribute

    def perform(self, sc):
        return 'dummy-value'

class RegisterNode(Command):
    def __init__(self, resolved_node_definition):
        Command.__init__(self)
        self.resolved_node_definition = resolved_node_definition

    def perform(self, sc):
        return None

class DropNode(Command):
    def __init__(self, instance_data):
        Command.__init__(self)
        self.instance_data = instance_data

    def perform(self, sc):
        return None

class InfrastructureExists(Command):
    def __init__(self, infra_id):
        Command.__init__(self)
        self.infra_id = infra_id

    def perform(self, sc):
        return True

class CreateInfrastructure(Command):
    def __init__(self, infra_id):
        Command.__init__(self)
        self.infra_id = infra_id

    def perform(self, sc):
        return None

class DropInfrastructure(Command):
    def __init__(self, infra_id):
        Command.__init__(self)
        self.infra_id = infra_id

    def perform(self, sc):
        return None

@factory.register(ConfigManager, 'dummy')
class DummyConfigManager(ConfigManager):
    def __init__(self, name='dummy', **kwargs):
        self.name = name
    
    def cri_drop_infrastructure(self, infra_id):
        return DropInfrastructure(infra_id)

    def cri_create_infrastructure(self, infra_id):
        return CreateInfrastructure(infra_id)

    def cri_infrastructure_exists(self, infra_id):
        return InfrastructureExists(infra_id)

    def cri_register_node(self, resolved_node_definition):
        return RegisterNode(resolved_node_definition)

    def cri_drop_node(self, instance_data):
        return DropNode(instance_data)

    def cri_get_node_state(self, instance_data):
        return GetNodeState(instance_data)

    def cri_get_node_attribute(self, node_id, attribute):
        return GetNodeAttribute(node_id, attribute)

    def perform(self, instruction):
        instruction.perform(self)

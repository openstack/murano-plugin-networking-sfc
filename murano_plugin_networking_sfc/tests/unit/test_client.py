#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock
import unittest

from murano_plugin_networking_sfc import client


class TestNetworkingSfcClient(unittest.TestCase):

    ALL_FUNCTIONS = [
        'create_flow_classifier',
        'delete_flow_classifier',
        'list_flow_classifiers',
        'show_flow_classifier',
        'update_flow_classifier',

        'create_port_chain',
        'delete_port_chain',
        'list_port_chains',
        'show_port_chain',
        'update_port_chain',

        'create_port_pair',
        'delete_port_pair',
        'list_port_pairs',
        'show_port_pair',
        'update_port_pair',

        'create_port_pair_group',
        'delete_port_pair_group',
        'list_port_pair_groups',
        'show_port_pair_group',
        'update_port_pair_group',
    ]

    def setUp(self):
        patcher = mock.patch.object(client.NetworkingSfcClient, 'client')
        self.addCleanup(patcher.stop)
        self.n_client = patcher.start()

        self.client = client.NetworkingSfcClient(mock.MagicMock())

    def test_client_function_call(self):
        flow_id = 'flow-id'
        port_pair_group_id = 'port-pair-group-id'
        self.client.create_port_chain(flow_classifiers=[flow_id],
                                      port_pair_groups=[port_pair_group_id])
        self.n_client.create_port_chain.assert_called_once_with({
            'port_chain': {
                'flow_classifiers': [
                    flow_id,
                ],
                'port_pair_groups': [
                    port_pair_group_id
                ]
            }
        })

    def test_client_function_call_unknown(self):
        with self.assertRaises(AttributeError):
            self.client.invalid_function()

    def test_client_api(self):
        for func_name in self.ALL_FUNCTIONS:
            self.assertTrue(hasattr(client.NetworkingSfcClient, func_name))

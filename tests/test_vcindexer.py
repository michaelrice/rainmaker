# Copyright 2014 Michael Rice <michael@michaelrice.org>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import vcr

from pyVmomi import vim

import tests

from rainmaker import vcindexer


class VcIndexerTests(tests.VCRBasedTests):

    @vcr.use_cassette('test_vcindexer_get_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once')
    def test_vcindexer_get_connection(self):
        host = '10.12.254.119'
        password = 'password'
        service_instance = vcindexer.get_connection(host=host, password=password)
        self.assertIsNotNone(service_instance)
        self.assertIsInstance(service_instance, vim.ServiceInstance)

    @vcr.use_cassette('test_vcindexer_get_datacenters.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once')
    def test_vcindexer_get_datacenters(self):
        host = '10.12.254.119'
        password = 'password'
        service_instance = vcindexer.get_connection(host, password=password)
        datacenters = vcindexer.get_datacenters(service_instance)
        self.assertIsInstance(datacenters, list)
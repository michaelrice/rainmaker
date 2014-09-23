# Copyright 2014 Michael Rice <michael@michaelrice.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta
from abc import abstractmethod


class VCenterProvider(object):
    __metaclass__ = ABCMeta

    def __init__(self, datacenter):
        self.datacenter = datacenter

    @abstractmethod
    def get_vcenter(self):
        """
        Returns a dict containing the vCenter and credentials needed
        to connect to it.

        {
            'hostname': 'vs01.homelab.local',
            'ip': '10.12.254.10',
            'username': 'administrator@vsphere.local'
            'password': 'vmware'
        }

        :return dict:
        """
        return

    @abstractmethod
    def get_vcenters(self):
        """
        Returns a list of vCenter dict objects that contain the hostname, ip,
        and credentials needed to connect to it
        [
            {
                'hostname': 'vs01.homelab.local',
                'ip': '10.12.254.10',
                'username': 'administrator@vsphere.local'
                'password': 'vmware'
            }
        ]

        :return list:
        """
        return

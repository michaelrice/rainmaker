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


class VCloudUsageMeterProvider(object):
    """
    Base class for vCenter info providers

    Takes a datacenter
    """
    __metaclass__ = ABCMeta

    def __init__(self, datacenter=None):
        self.datacenter = datacenter

    @abstractmethod
    def get_usage_meter(self):
        """
        Get a single usage meter from a given datacenter
        Useful if you only have 1 vc usage meter server per DC.

        The return should be a dict containing the hostname, ip,
        and token needed to connect to usage meter.
        {
            hostname: usagemeter.home.lab,
            ip: 10.12.254.11,
            token: 555111222333FFER
        }

        :return:
        """
        return

    @abstractmethod
    def get_usage_meters(self):
        """
        Get a list of vCloud Usage Meters to connect to per datacenter

        [
            {
                hostname: usagemeter.home.lab,
                ip: 10.12.254.11,
                token: 555111222333FFER
            }
        ]

        :return list:
        """
        return

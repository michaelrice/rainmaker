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

from pyVim import connect
from pyVmomi import vim

from .tools import pchelper


def get_datacenters(service_instance):
    """
    Given a ServiceInstance return all the
    vim.Datacenter objects in a list of dict
    that look like:

    data = get_datacenters(si)

    data:
    [{'moref': 'datacenter-2', u'name': 'DC0'}]

    :param service_instance:
    :return:
    """
    view = pchelper.get_container_view(service_instance,
                                       obj_type=[vim.Datacenter])
    data = pchelper.collect_properties(service_instance, view_ref=view,
                                       obj_type=vim.Datacenter,
                                       path_set=['name'],
                                       include_mors=True)
    return data


def get_connection(host='localhost', user='administrator@vsphere.local',
                   password='vmware', port=443):
    """
    Return a ServiceInstance given the connection info

    service_instance = get_connection(host='10.12.254.100')

    :param host:
    :param user:
    :param password:
    :param port:
    :return:
    """
    service_instance = connect.SmartConnect(host=host,
                                            user=user,
                                            pwd=password,
                                            port=int(port))
    return service_instance

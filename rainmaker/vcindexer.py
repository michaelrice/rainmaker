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

import atexit

from pyVim import connect
from pyVmomi import vim

from tools import pchelper


def get_datacenters(service_instance):
    view = pchelper.get_container_view(service_instance,
                                       obj_type=[vim.Datacenter])
    data = pchelper.collect_properties(service_instance, view_ref=view,
                                       obj_type=vim.Datacenter,
                                       path_set=['name'],
                                       include_mors=True)
    return data


def get_connection(host='localhost', user='administrator@vsphere.local',
                   password='vmware', port=443):
    service_instance = connect.SmartConnect(host=host,
                                            user=user,
                                            pwd=password,
                                            port=int(port))
    atexit.register(connect.Disconnect, service_instance)
    return service_instance

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkelasticsearch.endpoint import endpoint_data

class ListInstanceIndicesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListInstanceIndices','elasticsearch')
		self.set_uri_pattern('/openapi/instances/[InstanceId]/indices')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_all(self):
		return self.get_query_params().get('all')

	def set_all(self,all):
		self.add_query_param('all',all)

	def get_InstanceId(self):
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_path_param('InstanceId',InstanceId)

	def get_isManaged(self):
		return self.get_query_params().get('isManaged')

	def set_isManaged(self,isManaged):
		self.add_query_param('isManaged',isManaged)

	def get_size(self):
		return self.get_query_params().get('size')

	def set_size(self,size):
		self.add_query_param('size',size)

	def get_name(self):
		return self.get_query_params().get('name')

	def set_name(self,name):
		self.add_query_param('name',name)

	def get_page(self):
		return self.get_query_params().get('page')

	def set_page(self,page):
		self.add_query_param('page',page)

	def get_isOpenstore(self):
		return self.get_query_params().get('isOpenstore')

	def set_isOpenstore(self,isOpenstore):
		self.add_query_param('isOpenstore',isOpenstore)
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

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvod.endpoint import endpoint_data

class UnTagVodResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'UnTagVodResources','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_All(self):
		return self.get_query_params().get('All')

	def set_All(self,All):
		self.add_query_param('All',All)

	def get_ResourceIds(self):
		return self.get_query_params().get('ResourceId')

	def set_ResourceIds(self, ResourceIds):
		for depth1 in range(len(ResourceIds)):
			if ResourceIds[depth1] is not None:
				self.add_query_param('ResourceId.' + str(depth1 + 1) , ResourceIds[depth1])

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_TagKeys(self):
		return self.get_query_params().get('TagKey')

	def set_TagKeys(self, TagKeys):
		for depth1 in range(len(TagKeys)):
			if TagKeys[depth1] is not None:
				self.add_query_param('TagKey.' + str(depth1 + 1) , TagKeys[depth1])
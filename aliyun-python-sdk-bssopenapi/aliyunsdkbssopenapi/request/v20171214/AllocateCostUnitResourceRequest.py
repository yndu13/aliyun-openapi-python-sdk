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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class AllocateCostUnitResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'AllocateCostUnitResource')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceInstanceLists(self): # RepeatList
		return self.get_query_params().get('ResourceInstanceList')

	def set_ResourceInstanceLists(self, ResourceInstanceList):  # RepeatList
		for depth1 in range(len(ResourceInstanceList)):
			if ResourceInstanceList[depth1].get('ResourceId') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.ResourceId', ResourceInstanceList[depth1].get('ResourceId'))
			if ResourceInstanceList[depth1].get('CommodityCode') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.CommodityCode', ResourceInstanceList[depth1].get('CommodityCode'))
			if ResourceInstanceList[depth1].get('ApportionCode') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.ApportionCode', ResourceInstanceList[depth1].get('ApportionCode'))
			if ResourceInstanceList[depth1].get('ResourceUserId') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.ResourceUserId', ResourceInstanceList[depth1].get('ResourceUserId'))
	def get_FromUnitId(self): # Long
		return self.get_query_params().get('FromUnitId')

	def set_FromUnitId(self, FromUnitId):  # Long
		self.add_query_param('FromUnitId', FromUnitId)
	def get_ToUnitId(self): # Long
		return self.get_query_params().get('ToUnitId')

	def set_ToUnitId(self, ToUnitId):  # Long
		self.add_query_param('ToUnitId', ToUnitId)
	def get_FromUnitUserId(self): # Long
		return self.get_query_params().get('FromUnitUserId')

	def set_FromUnitUserId(self, FromUnitUserId):  # Long
		self.add_query_param('FromUnitUserId', FromUnitUserId)
	def get_ToUnitUserId(self): # Long
		return self.get_query_params().get('ToUnitUserId')

	def set_ToUnitUserId(self, ToUnitUserId):  # Long
		self.add_query_param('ToUnitUserId', ToUnitUserId)

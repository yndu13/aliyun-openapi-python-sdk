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
from aliyunsdkunimkt.endpoint import endpoint_data

class CreateSlotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'CreateSlot','1.0.0')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Business(self):
		return self.get_query_params().get('Business')

	def set_Business(self,Business):
		self.add_query_param('Business',Business)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_OriginSiteUserId(self):
		return self.get_query_params().get('OriginSiteUserId')

	def set_OriginSiteUserId(self,OriginSiteUserId):
		self.add_query_param('OriginSiteUserId',OriginSiteUserId)

	def get_Environment(self):
		return self.get_query_params().get('Environment')

	def set_Environment(self,Environment):
		self.add_query_param('Environment',Environment)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_TenantId(self):
		return self.get_query_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_query_param('TenantId',TenantId)

	def get_UserSite(self):
		return self.get_query_params().get('UserSite')

	def set_UserSite(self,UserSite):
		self.add_query_param('UserSite',UserSite)

	def get_AdSlot(self):
		return self.get_body_params().get('AdSlot')

	def set_AdSlot(self,AdSlot):
		self.add_body_params('AdSlot', AdSlot)
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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class ListCompanyRegOrdersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'ListCompanyRegOrders')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NotBizStatus(self):
		return self.get_query_params().get('NotBizStatus')

	def set_NotBizStatus(self,NotBizStatus):
		self.add_query_param('NotBizStatus',NotBizStatus)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_BizStatus(self):
		return self.get_query_params().get('BizStatus')

	def set_BizStatus(self,BizStatus):
		self.add_query_param('BizStatus',BizStatus)

	def get_CompanyName(self):
		return self.get_query_params().get('CompanyName')

	def set_CompanyName(self,CompanyName):
		self.add_query_param('CompanyName',CompanyName)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AliyunOrderId(self):
		return self.get_query_params().get('AliyunOrderId')

	def set_AliyunOrderId(self,AliyunOrderId):
		self.add_query_param('AliyunOrderId',AliyunOrderId)

	def get_BizSubCode(self):
		return self.get_query_params().get('BizSubCode')

	def set_BizSubCode(self,BizSubCode):
		self.add_query_param('BizSubCode',BizSubCode)
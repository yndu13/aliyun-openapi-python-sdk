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

class UpdateFeeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'UpdateFee')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Kind(self):
		return self.get_query_params().get('Kind')

	def set_Kind(self,Kind):
		self.add_query_param('Kind',Kind)

	def get_Use(self):
		return self.get_query_params().get('Use')

	def set_Use(self,Use):
		self.add_query_param('Use',Use)

	def get_BaseTotalAmount(self):
		return self.get_query_params().get('BaseTotalAmount')

	def set_BaseTotalAmount(self,BaseTotalAmount):
		self.add_query_param('BaseTotalAmount',BaseTotalAmount)

	def get_Payer(self):
		return self.get_query_params().get('Payer')

	def set_Payer(self,Payer):
		self.add_query_param('Payer',Payer)

	def get_SecondKey(self):
		return self.get_query_params().get('SecondKey')

	def set_SecondKey(self,SecondKey):
		self.add_query_param('SecondKey',SecondKey)

	def get_PayMethod(self):
		return self.get_query_params().get('PayMethod')

	def set_PayMethod(self,PayMethod):
		self.add_query_param('PayMethod',PayMethod)

	def get_FirstKey(self):
		return self.get_query_params().get('FirstKey')

	def set_FirstKey(self,FirstKey):
		self.add_query_param('FirstKey',FirstKey)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_FeeType(self):
		return self.get_query_params().get('FeeType')

	def set_FeeType(self,FeeType):
		self.add_query_param('FeeType',FeeType)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)
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

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'CreateInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SubscriptionType(self): # String
		return self.get_query_params().get('SubscriptionType')

	def set_SubscriptionType(self, SubscriptionType):  # String
		self.add_query_param('SubscriptionType', SubscriptionType)
	def get_Logistics(self): # String
		return self.get_query_params().get('Logistics')

	def set_Logistics(self, Logistics):  # String
		self.add_query_param('Logistics', Logistics)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ProductType(self): # String
		return self.get_query_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_query_param('ProductType', ProductType)
	def get_RenewPeriod(self): # Integer
		return self.get_query_params().get('RenewPeriod')

	def set_RenewPeriod(self, RenewPeriod):  # Integer
		self.add_query_param('RenewPeriod', RenewPeriod)
	def get_RenewalStatus(self): # String
		return self.get_query_params().get('RenewalStatus')

	def set_RenewalStatus(self, RenewalStatus):  # String
		self.add_query_param('RenewalStatus', RenewalStatus)
	def get_Parameters(self): # RepeatList
		return self.get_query_params().get('Parameter')

	def set_Parameters(self, Parameter):  # RepeatList
		for depth1 in range(len(Parameter)):
			if Parameter[depth1].get('Code') is not None:
				self.add_query_param('Parameter.' + str(depth1 + 1) + '.Code', Parameter[depth1].get('Code'))
			if Parameter[depth1].get('Value') is not None:
				self.add_query_param('Parameter.' + str(depth1 + 1) + '.Value', Parameter[depth1].get('Value'))

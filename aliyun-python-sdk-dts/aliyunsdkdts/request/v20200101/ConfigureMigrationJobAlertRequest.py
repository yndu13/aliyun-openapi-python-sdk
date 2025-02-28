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
from aliyunsdkdts.endpoint import endpoint_data

class ConfigureMigrationJobAlertRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'ConfigureMigrationJobAlert','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DelayOverSeconds(self): # String
		return self.get_query_params().get('DelayOverSeconds')

	def set_DelayOverSeconds(self, DelayOverSeconds):  # String
		self.add_query_param('DelayOverSeconds', DelayOverSeconds)
	def get_DelayAlertStatus(self): # String
		return self.get_query_params().get('DelayAlertStatus')

	def set_DelayAlertStatus(self, DelayAlertStatus):  # String
		self.add_query_param('DelayAlertStatus', DelayAlertStatus)
	def get_MigrationJobId(self): # String
		return self.get_query_params().get('MigrationJobId')

	def set_MigrationJobId(self, MigrationJobId):  # String
		self.add_query_param('MigrationJobId', MigrationJobId)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_AccountId(self): # String
		return self.get_query_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_query_param('AccountId', AccountId)
	def get_ErrorAlertPhone(self): # String
		return self.get_query_params().get('ErrorAlertPhone')

	def set_ErrorAlertPhone(self, ErrorAlertPhone):  # String
		self.add_query_param('ErrorAlertPhone', ErrorAlertPhone)
	def get_DelayAlertPhone(self): # String
		return self.get_query_params().get('DelayAlertPhone')

	def set_DelayAlertPhone(self, DelayAlertPhone):  # String
		self.add_query_param('DelayAlertPhone', DelayAlertPhone)
	def get_ErrorAlertStatus(self): # String
		return self.get_query_params().get('ErrorAlertStatus')

	def set_ErrorAlertStatus(self, ErrorAlertStatus):  # String
		self.add_query_param('ErrorAlertStatus', ErrorAlertStatus)

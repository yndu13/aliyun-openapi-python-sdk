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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class UpdateIDEEventResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateIDEEventResult')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CheckResultTip(self):
		return self.get_body_params().get('CheckResultTip')

	def set_CheckResultTip(self,CheckResultTip):
		self.add_body_params('CheckResultTip', CheckResultTip)

	def get_CheckResult(self):
		return self.get_body_params().get('CheckResult')

	def set_CheckResult(self,CheckResult):
		self.add_body_params('CheckResult', CheckResult)

	def get_MessageId(self):
		return self.get_body_params().get('MessageId')

	def set_MessageId(self,MessageId):
		self.add_body_params('MessageId', MessageId)

	def get_ExtensionCode(self):
		return self.get_body_params().get('ExtensionCode')

	def set_ExtensionCode(self,ExtensionCode):
		self.add_body_params('ExtensionCode', ExtensionCode)
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
from aliyunsdkretailcloud.endpoint import endpoint_data

class CreateAppMonitorsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreateAppMonitors','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AppIdss(self):
		return self.get_body_params().get('AppIds')

	def set_AppIdss(self, AppIdss):
		for depth1 in range(len(AppIdss)):
			if AppIdss[depth1] is not None:
				self.add_body_params('AppIds.' + str(depth1 + 1) , AppIdss[depth1])

	def get_MainUserId(self):
		return self.get_query_params().get('MainUserId')

	def set_MainUserId(self,MainUserId):
		self.add_query_param('MainUserId',MainUserId)

	def get_EnvType(self):
		return self.get_query_params().get('EnvType')

	def set_EnvType(self,EnvType):
		self.add_query_param('EnvType',EnvType)

	def get_AlarmTemplateId(self):
		return self.get_query_params().get('AlarmTemplateId')

	def set_AlarmTemplateId(self,AlarmTemplateId):
		self.add_query_param('AlarmTemplateId',AlarmTemplateId)

	def get_SilenceTime(self):
		return self.get_query_params().get('SilenceTime')

	def set_SilenceTime(self,SilenceTime):
		self.add_query_param('SilenceTime',SilenceTime)
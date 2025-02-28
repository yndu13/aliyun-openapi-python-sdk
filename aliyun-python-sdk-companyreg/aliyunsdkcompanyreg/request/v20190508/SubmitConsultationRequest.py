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

class SubmitConsultationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'SubmitConsultation')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Data(self):
		return self.get_query_params().get('Data')

	def set_Data(self,Data):
		self.add_query_param('Data',Data)

	def get_Vcode(self):
		return self.get_query_params().get('Vcode')

	def set_Vcode(self,Vcode):
		self.add_query_param('Vcode',Vcode)

	def get_ConsultRequestId(self):
		return self.get_query_params().get('ConsultRequestId')

	def set_ConsultRequestId(self,ConsultRequestId):
		self.add_query_param('ConsultRequestId',ConsultRequestId)

	def get_BizSubCode(self):
		return self.get_query_params().get('BizSubCode')

	def set_BizSubCode(self,BizSubCode):
		self.add_query_param('BizSubCode',BizSubCode)
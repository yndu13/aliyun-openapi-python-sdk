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
from aliyunsdkccc.endpoint import endpoint_data

class ListAttemptsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'ListAttempts')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ContactId(self):
		return self.get_query_params().get('ContactId')

	def set_ContactId(self,ContactId):
		self.add_query_param('ContactId',ContactId)

	def get_CampaignId(self):
		return self.get_query_params().get('CampaignId')

	def set_CampaignId(self,CampaignId):
		self.add_query_param('CampaignId',CampaignId)

	def get_Callee(self):
		return self.get_query_params().get('Callee')

	def set_Callee(self,Callee):
		self.add_query_param('Callee',Callee)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_QueueId(self):
		return self.get_query_params().get('QueueId')

	def set_QueueId(self,QueueId):
		self.add_query_param('QueueId',QueueId)

	def get_AgentId(self):
		return self.get_query_params().get('AgentId')

	def set_AgentId(self,AgentId):
		self.add_query_param('AgentId',AgentId)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_Caller(self):
		return self.get_query_params().get('Caller')

	def set_Caller(self,Caller):
		self.add_query_param('Caller',Caller)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_CaseId(self):
		return self.get_query_params().get('CaseId')

	def set_CaseId(self,CaseId):
		self.add_query_param('CaseId',CaseId)

	def get_AttemptId(self):
		return self.get_query_params().get('AttemptId')

	def set_AttemptId(self,AttemptId):
		self.add_query_param('AttemptId',AttemptId)
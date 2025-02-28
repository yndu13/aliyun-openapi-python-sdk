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

class ListCallDetailRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'ListCallDetailRecords')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ContactId(self):
		return self.get_query_params().get('ContactId')

	def set_ContactId(self,ContactId):
		self.add_query_param('ContactId',ContactId)

	def get_Criteria(self):
		return self.get_query_params().get('Criteria')

	def set_Criteria(self,Criteria):
		self.add_query_param('Criteria',Criteria)

	def get_OrderByField(self):
		return self.get_query_params().get('OrderByField')

	def set_OrderByField(self,OrderByField):
		self.add_query_param('OrderByField',OrderByField)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_EarlyMediaStateList(self):
		return self.get_query_params().get('EarlyMediaStateList')

	def set_EarlyMediaStateList(self,EarlyMediaStateList):
		self.add_query_param('EarlyMediaStateList',EarlyMediaStateList)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_SatisfactionList(self):
		return self.get_query_params().get('SatisfactionList')

	def set_SatisfactionList(self,SatisfactionList):
		self.add_query_param('SatisfactionList',SatisfactionList)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_SortOrder(self):
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self,SortOrder):
		self.add_query_param('SortOrder',SortOrder)

	def get_SatisfactionDescriptionList(self):
		return self.get_query_params().get('SatisfactionDescriptionList')

	def set_SatisfactionDescriptionList(self,SatisfactionDescriptionList):
		self.add_query_param('SatisfactionDescriptionList',SatisfactionDescriptionList)

	def get_AgentId(self):
		return self.get_query_params().get('AgentId')

	def set_AgentId(self,AgentId):
		self.add_query_param('AgentId',AgentId)

	def get_ContactType(self):
		return self.get_query_params().get('ContactType')

	def set_ContactType(self,ContactType):
		self.add_query_param('ContactType',ContactType)

	def get_SatisfactionSurveyChannel(self):
		return self.get_query_params().get('SatisfactionSurveyChannel')

	def set_SatisfactionSurveyChannel(self,SatisfactionSurveyChannel):
		self.add_query_param('SatisfactionSurveyChannel',SatisfactionSurveyChannel)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_CallingNumber(self):
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumber(self,CallingNumber):
		self.add_query_param('CallingNumber',CallingNumber)

	def get_ContactDisposition(self):
		return self.get_query_params().get('ContactDisposition')

	def set_ContactDisposition(self,ContactDisposition):
		self.add_query_param('ContactDisposition',ContactDisposition)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SkillGroupId(self):
		return self.get_query_params().get('SkillGroupId')

	def set_SkillGroupId(self,SkillGroupId):
		self.add_query_param('SkillGroupId',SkillGroupId)
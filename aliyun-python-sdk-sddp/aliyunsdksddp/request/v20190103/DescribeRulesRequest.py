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
from aliyunsdksddp.endpoint import endpoint_data

class DescribeRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'DescribeRules')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_WarnLevel(self):
		return self.get_query_params().get('WarnLevel')

	def set_WarnLevel(self,WarnLevel):
		self.add_query_param('WarnLevel',WarnLevel)

	def get_ProductCode(self):
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_query_param('ProductCode',ProductCode)

	def get_ProductId(self):
		return self.get_query_params().get('ProductId')

	def set_ProductId(self,ProductId):
		self.add_query_param('ProductId',ProductId)

	def get_RiskLevelId(self):
		return self.get_query_params().get('RiskLevelId')

	def set_RiskLevelId(self,RiskLevelId):
		self.add_query_param('RiskLevelId',RiskLevelId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_KeywordCompatible(self):
		return self.get_query_params().get('KeywordCompatible')

	def set_KeywordCompatible(self,KeywordCompatible):
		self.add_query_param('KeywordCompatible',KeywordCompatible)

	def get_RuleType(self):
		return self.get_query_params().get('RuleType')

	def set_RuleType(self,RuleType):
		self.add_query_param('RuleType',RuleType)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_ContentCategory(self):
		return self.get_query_params().get('ContentCategory')

	def set_ContentCategory(self,ContentCategory):
		self.add_query_param('ContentCategory',ContentCategory)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_CustomType(self):
		return self.get_query_params().get('CustomType')

	def set_CustomType(self,CustomType):
		self.add_query_param('CustomType',CustomType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)
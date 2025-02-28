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

class CreateScanTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'CreateScanTask')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RunHour(self):
		return self.get_query_params().get('RunHour')

	def set_RunHour(self,RunHour):
		self.add_query_param('RunHour',RunHour)

	def get_ScanRangeContent(self):
		return self.get_query_params().get('ScanRangeContent')

	def set_ScanRangeContent(self,ScanRangeContent):
		self.add_query_param('ScanRangeContent',ScanRangeContent)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_DataLimitId(self):
		return self.get_query_params().get('DataLimitId')

	def set_DataLimitId(self,DataLimitId):
		self.add_query_param('DataLimitId',DataLimitId)

	def get_RunMinute(self):
		return self.get_query_params().get('RunMinute')

	def set_RunMinute(self,RunMinute):
		self.add_query_param('RunMinute',RunMinute)

	def get_IntervalDay(self):
		return self.get_query_params().get('IntervalDay')

	def set_IntervalDay(self,IntervalDay):
		self.add_query_param('IntervalDay',IntervalDay)

	def get_ScanRange(self):
		return self.get_query_params().get('ScanRange')

	def set_ScanRange(self,ScanRange):
		self.add_query_param('ScanRange',ScanRange)

	def get_OssScanPath(self):
		return self.get_query_params().get('OssScanPath')

	def set_OssScanPath(self,OssScanPath):
		self.add_query_param('OssScanPath',OssScanPath)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_TaskUserName(self):
		return self.get_query_params().get('TaskUserName')

	def set_TaskUserName(self,TaskUserName):
		self.add_query_param('TaskUserName',TaskUserName)
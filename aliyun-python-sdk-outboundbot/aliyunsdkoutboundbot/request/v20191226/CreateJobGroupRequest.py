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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class CreateJobGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'CreateJobGroup','outboundbot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RecallStrategyJson(self):
		return self.get_query_params().get('RecallStrategyJson')

	def set_RecallStrategyJson(self,RecallStrategyJson):
		self.add_query_param('RecallStrategyJson',RecallStrategyJson)

	def get_JobGroupName(self):
		return self.get_query_params().get('JobGroupName')

	def set_JobGroupName(self,JobGroupName):
		self.add_query_param('JobGroupName',JobGroupName)

	def get_ScriptId(self):
		return self.get_query_params().get('ScriptId')

	def set_ScriptId(self,ScriptId):
		self.add_query_param('ScriptId',ScriptId)

	def get_StrategyJson(self):
		return self.get_query_params().get('StrategyJson')

	def set_StrategyJson(self,StrategyJson):
		self.add_query_param('StrategyJson',StrategyJson)

	def get_RingingDuration(self):
		return self.get_query_params().get('RingingDuration')

	def set_RingingDuration(self,RingingDuration):
		self.add_query_param('RingingDuration',RingingDuration)

	def get_ScenarioId(self):
		return self.get_query_params().get('ScenarioId')

	def set_ScenarioId(self,ScenarioId):
		self.add_query_param('ScenarioId',ScenarioId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_JobGroupDescription(self):
		return self.get_query_params().get('JobGroupDescription')

	def set_JobGroupDescription(self,JobGroupDescription):
		self.add_query_param('JobGroupDescription',JobGroupDescription)

	def get_CallingNumbers(self):
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumbers(self, CallingNumbers):
		for depth1 in range(len(CallingNumbers)):
			if CallingNumbers[depth1] is not None:
				self.add_query_param('CallingNumber.' + str(depth1 + 1) , CallingNumbers[depth1])

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_MinConcurrency(self):
		return self.get_query_params().get('MinConcurrency')

	def set_MinConcurrency(self,MinConcurrency):
		self.add_query_param('MinConcurrency',MinConcurrency)
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
from aliyunsdkvoicenavigator.endpoint import endpoint_data

class DialogueRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'Dialogue','voicebot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConversationId(self):
		return self.get_query_params().get('ConversationId')

	def set_ConversationId(self,ConversationId):
		self.add_query_param('ConversationId',ConversationId)

	def get_CallingNumber(self):
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumber(self,CallingNumber):
		self.add_query_param('CallingNumber',CallingNumber)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_AdditionalContext(self):
		return self.get_query_params().get('AdditionalContext')

	def set_AdditionalContext(self,AdditionalContext):
		self.add_query_param('AdditionalContext',AdditionalContext)

	def get_InstanceOwnerId(self):
		return self.get_query_params().get('InstanceOwnerId')

	def set_InstanceOwnerId(self,InstanceOwnerId):
		self.add_query_param('InstanceOwnerId',InstanceOwnerId)

	def get_Utterance(self):
		return self.get_query_params().get('Utterance')

	def set_Utterance(self,Utterance):
		self.add_query_param('Utterance',Utterance)
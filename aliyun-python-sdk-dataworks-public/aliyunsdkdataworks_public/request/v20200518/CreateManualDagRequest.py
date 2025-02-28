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

class CreateManualDagRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateManualDag')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectEnv(self):
		return self.get_body_params().get('ProjectEnv')

	def set_ProjectEnv(self,ProjectEnv):
		self.add_body_params('ProjectEnv', ProjectEnv)

	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_DagParameters(self):
		return self.get_body_params().get('DagParameters')

	def set_DagParameters(self,DagParameters):
		self.add_body_params('DagParameters', DagParameters)

	def get_IncludeNodeIds(self):
		return self.get_body_params().get('IncludeNodeIds')

	def set_IncludeNodeIds(self,IncludeNodeIds):
		self.add_body_params('IncludeNodeIds', IncludeNodeIds)

	def get_BizDate(self):
		return self.get_body_params().get('BizDate')

	def set_BizDate(self,BizDate):
		self.add_body_params('BizDate', BizDate)

	def get_ExcludeNodeIds(self):
		return self.get_body_params().get('ExcludeNodeIds')

	def set_ExcludeNodeIds(self,ExcludeNodeIds):
		self.add_body_params('ExcludeNodeIds', ExcludeNodeIds)

	def get_FlowName(self):
		return self.get_body_params().get('FlowName')

	def set_FlowName(self,FlowName):
		self.add_body_params('FlowName', FlowName)

	def get_NodeParameters(self):
		return self.get_body_params().get('NodeParameters')

	def set_NodeParameters(self,NodeParameters):
		self.add_body_params('NodeParameters', NodeParameters)
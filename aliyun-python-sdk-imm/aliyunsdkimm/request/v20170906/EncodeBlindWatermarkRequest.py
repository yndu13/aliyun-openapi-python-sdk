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
from aliyunsdkimm.endpoint import endpoint_data

class EncodeBlindWatermarkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'EncodeBlindWatermark','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ImageQuality(self): # String
		return self.get_query_params().get('ImageQuality')

	def set_ImageQuality(self, ImageQuality):  # String
		self.add_query_param('ImageQuality', ImageQuality)
	def get_WatermarkUri(self): # String
		return self.get_query_params().get('WatermarkUri')

	def set_WatermarkUri(self, WatermarkUri):  # String
		self.add_query_param('WatermarkUri', WatermarkUri)
	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_TargetUri(self): # String
		return self.get_query_params().get('TargetUri')

	def set_TargetUri(self, TargetUri):  # String
		self.add_query_param('TargetUri', TargetUri)
	def get_Model(self): # String
		return self.get_query_params().get('Model')

	def set_Model(self, Model):  # String
		self.add_query_param('Model', Model)
	def get_TargetImageType(self): # String
		return self.get_query_params().get('TargetImageType')

	def set_TargetImageType(self, TargetImageType):  # String
		self.add_query_param('TargetImageType', TargetImageType)
	def get_ImageUri(self): # String
		return self.get_query_params().get('ImageUri')

	def set_ImageUri(self, ImageUri):  # String
		self.add_query_param('ImageUri', ImageUri)

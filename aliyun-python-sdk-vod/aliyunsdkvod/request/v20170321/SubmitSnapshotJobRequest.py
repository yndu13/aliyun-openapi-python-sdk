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
from aliyunsdkvod.endpoint import endpoint_data

class SubmitSnapshotJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SubmitSnapshotJob','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_SpecifiedOffsetTime(self):
		return self.get_query_params().get('SpecifiedOffsetTime')

	def set_SpecifiedOffsetTime(self,SpecifiedOffsetTime):
		self.add_query_param('SpecifiedOffsetTime',SpecifiedOffsetTime)

	def get_SpriteSnapshotConfig(self):
		return self.get_query_params().get('SpriteSnapshotConfig')

	def set_SpriteSnapshotConfig(self,SpriteSnapshotConfig):
		self.add_query_param('SpriteSnapshotConfig',SpriteSnapshotConfig)

	def get_SnapshotTemplateId(self):
		return self.get_query_params().get('SnapshotTemplateId')

	def set_SnapshotTemplateId(self,SnapshotTemplateId):
		self.add_query_param('SnapshotTemplateId',SnapshotTemplateId)

	def get_Height(self):
		return self.get_query_params().get('Height')

	def set_Height(self,Height):
		self.add_query_param('Height',Height)

	def get_Count(self):
		return self.get_query_params().get('Count')

	def set_Count(self,Count):
		self.add_query_param('Count',Count)

	def get_VideoId(self):
		return self.get_query_params().get('VideoId')

	def set_VideoId(self,VideoId):
		self.add_query_param('VideoId',VideoId)

	def get_Width(self):
		return self.get_query_params().get('Width')

	def set_Width(self,Width):
		self.add_query_param('Width',Width)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)
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

class CreateUploadVideoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'CreateUploadVideo','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_FileSize(self):
		return self.get_query_params().get('FileSize')

	def set_FileSize(self,FileSize):
		self.add_query_param('FileSize',FileSize)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_StorageLocation(self):
		return self.get_query_params().get('StorageLocation')

	def set_StorageLocation(self,StorageLocation):
		self.add_query_param('StorageLocation',StorageLocation)

	def get_CoverURL(self):
		return self.get_query_params().get('CoverURL')

	def set_CoverURL(self,CoverURL):
		self.add_query_param('CoverURL',CoverURL)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_CateId(self):
		return self.get_query_params().get('CateId')

	def set_CateId(self,CateId):
		self.add_query_param('CateId',CateId)

	def get_WorkflowId(self):
		return self.get_query_params().get('WorkflowId')

	def set_WorkflowId(self,WorkflowId):
		self.add_query_param('WorkflowId',WorkflowId)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_FileName(self):
		return self.get_query_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_query_param('FileName',FileName)

	def get_TemplateGroupId(self):
		return self.get_query_params().get('TemplateGroupId')

	def set_TemplateGroupId(self,TemplateGroupId):
		self.add_query_param('TemplateGroupId',TemplateGroupId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)
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

from aliyunsdkcore.request import RoaRequest

class SyncYaochiLocationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'LRG', '2019-10-10', 'SyncYaochiLocation')
		self.set_uri_pattern('/api/v2/tianji/node/[id]/yaochi-location')
		self.set_method('POST')

	def get_id(self):
		return self.get_path_params().get('id')

	def set_id(self,id):
		self.add_path_param('id',id)
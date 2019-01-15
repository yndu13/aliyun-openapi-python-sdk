# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateNatGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateNatGateway','vpc')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_BandwidthPackages(self):
		return self.get_query_params().get('BandwidthPackages')

	def set_BandwidthPackages(self,BandwidthPackages):
		for i in range(len(BandwidthPackages)):	
			if BandwidthPackages[i].get('Bandwidth') is not None:
				self.add_query_param('BandwidthPackage.' + str(i + 1) + '.Bandwidth' , BandwidthPackages[i].get('Bandwidth'))
			if BandwidthPackages[i].get('Zone') is not None:
				self.add_query_param('BandwidthPackage.' + str(i + 1) + '.Zone' , BandwidthPackages[i].get('Zone'))
			if BandwidthPackages[i].get('InternetChargeType') is not None:
				self.add_query_param('BandwidthPackage.' + str(i + 1) + '.InternetChargeType' , BandwidthPackages[i].get('InternetChargeType'))
			if BandwidthPackages[i].get('ISP') is not None:
				self.add_query_param('BandwidthPackage.' + str(i + 1) + '.ISP' , BandwidthPackages[i].get('ISP'))
			if BandwidthPackages[i].get('IpCount') is not None:
				self.add_query_param('BandwidthPackage.' + str(i + 1) + '.IpCount' , BandwidthPackages[i].get('IpCount'))


	def get_Spec(self):
		return self.get_query_params().get('Spec')

	def set_Spec(self,Spec):
		self.add_query_param('Spec',Spec)
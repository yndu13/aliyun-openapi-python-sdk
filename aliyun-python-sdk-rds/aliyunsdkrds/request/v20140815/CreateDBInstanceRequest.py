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
from aliyunsdkrds.endpoint import endpoint_data

class CreateDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateDBInstance','rds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DBParamGroupId(self):
		return self.get_query_params().get('DBParamGroupId')

	def set_DBParamGroupId(self,DBParamGroupId):
		self.add_query_param('DBParamGroupId',DBParamGroupId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DBInstanceStorage(self):
		return self.get_query_params().get('DBInstanceStorage')

	def set_DBInstanceStorage(self,DBInstanceStorage):
		self.add_query_param('DBInstanceStorage',DBInstanceStorage)

	def get_SystemDBCharset(self):
		return self.get_query_params().get('SystemDBCharset')

	def set_SystemDBCharset(self,SystemDBCharset):
		self.add_query_param('SystemDBCharset',SystemDBCharset)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_TargetDedicatedHostIdForMaster(self):
		return self.get_query_params().get('TargetDedicatedHostIdForMaster')

	def set_TargetDedicatedHostIdForMaster(self,TargetDedicatedHostIdForMaster):
		self.add_query_param('TargetDedicatedHostIdForMaster',TargetDedicatedHostIdForMaster)

	def get_DBInstanceDescription(self):
		return self.get_query_params().get('DBInstanceDescription')

	def set_DBInstanceDescription(self,DBInstanceDescription):
		self.add_query_param('DBInstanceDescription',DBInstanceDescription)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_BusinessInfo(self):
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self,BusinessInfo):
		self.add_query_param('BusinessInfo',BusinessInfo)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_EncryptionKey(self):
		return self.get_query_params().get('EncryptionKey')

	def set_EncryptionKey(self,EncryptionKey):
		self.add_query_param('EncryptionKey',EncryptionKey)

	def get_DBInstanceClass(self):
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self,DBInstanceClass):
		self.add_query_param('DBInstanceClass',DBInstanceClass)

	def get_SecurityIPList(self):
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self,SecurityIPList):
		self.add_query_param('SecurityIPList',SecurityIPList)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_TargetDedicatedHostIdForLog(self):
		return self.get_query_params().get('TargetDedicatedHostIdForLog')

	def set_TargetDedicatedHostIdForLog(self,TargetDedicatedHostIdForLog):
		self.add_query_param('TargetDedicatedHostIdForLog',TargetDedicatedHostIdForLog)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_RoleARN(self):
		return self.get_query_params().get('RoleARN')

	def set_RoleARN(self,RoleARN):
		self.add_query_param('RoleARN',RoleARN)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_StorageAutoScale(self):
		return self.get_query_params().get('StorageAutoScale')

	def set_StorageAutoScale(self,StorageAutoScale):
		self.add_query_param('StorageAutoScale',StorageAutoScale)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)

	def get_ConnectionMode(self):
		return self.get_query_params().get('ConnectionMode')

	def set_ConnectionMode(self,ConnectionMode):
		self.add_query_param('ConnectionMode',ConnectionMode)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TargetDedicatedHostIdForSlave(self):
		return self.get_query_params().get('TargetDedicatedHostIdForSlave')

	def set_TargetDedicatedHostIdForSlave(self,TargetDedicatedHostIdForSlave):
		self.add_query_param('TargetDedicatedHostIdForSlave',TargetDedicatedHostIdForSlave)

	def get_ZoneIdSlave1(self):
		return self.get_query_params().get('ZoneIdSlave1')

	def set_ZoneIdSlave1(self,ZoneIdSlave1):
		self.add_query_param('ZoneIdSlave1',ZoneIdSlave1)

	def get_ZoneIdSlave2(self):
		return self.get_query_params().get('ZoneIdSlave2')

	def set_ZoneIdSlave2(self,ZoneIdSlave2):
		self.add_query_param('ZoneIdSlave2',ZoneIdSlave2)

	def get_DBIsIgnoreCase(self):
		return self.get_query_params().get('DBIsIgnoreCase')

	def set_DBIsIgnoreCase(self,DBIsIgnoreCase):
		self.add_query_param('DBIsIgnoreCase',DBIsIgnoreCase)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_DBTimeZone(self):
		return self.get_query_params().get('DBTimeZone')

	def set_DBTimeZone(self,DBTimeZone):
		self.add_query_param('DBTimeZone',DBTimeZone)

	def get_DBInstanceStorageType(self):
		return self.get_query_params().get('DBInstanceStorageType')

	def set_DBInstanceStorageType(self,DBInstanceStorageType):
		self.add_query_param('DBInstanceStorageType',DBInstanceStorageType)

	def get_DedicatedHostGroupId(self):
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self,DedicatedHostGroupId):
		self.add_query_param('DedicatedHostGroupId',DedicatedHostGroupId)

	def get_CreateStrategy(self):
		return self.get_query_params().get('CreateStrategy')

	def set_CreateStrategy(self,CreateStrategy):
		self.add_query_param('CreateStrategy',CreateStrategy)

	def get_DBInstanceNetType(self):
		return self.get_query_params().get('DBInstanceNetType')

	def set_DBInstanceNetType(self,DBInstanceNetType):
		self.add_query_param('DBInstanceNetType',DBInstanceNetType)

	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_UsedTime(self):
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self,UsedTime):
		self.add_query_param('UsedTime',UsedTime)

	def get_TargetMinorVersion(self):
		return self.get_query_params().get('TargetMinorVersion')

	def set_TargetMinorVersion(self,TargetMinorVersion):
		self.add_query_param('TargetMinorVersion',TargetMinorVersion)

	def get_UserBackupId(self):
		return self.get_query_params().get('UserBackupId')

	def set_UserBackupId(self,UserBackupId):
		self.add_query_param('UserBackupId',UserBackupId)

	def get_StorageUpperBound(self):
		return self.get_query_params().get('StorageUpperBound')

	def set_StorageUpperBound(self,StorageUpperBound):
		self.add_query_param('StorageUpperBound',StorageUpperBound)

	def get_StorageThreshold(self):
		return self.get_query_params().get('StorageThreshold')

	def set_StorageThreshold(self,StorageThreshold):
		self.add_query_param('StorageThreshold',StorageThreshold)

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)
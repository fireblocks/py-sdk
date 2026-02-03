# DelegationBlockchainPositionInfo

Additional fields per blockchain - can be empty or missing if not initialized or no additional info exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stake_account_address** | **str** | The stake account address matching the stakeAccountId. | 
**stake_account_derivation_change_value** | **float** | The value of the change level in the BIP32 path which was used to derive the stake account address. | 
**is_compounding_validator** | **bool** | Is the validator compounding (i.e it was created with compounding validator type). | 
**total_withdrawable_amount** | **str** | The total amount available for withdrawal. | 
**total_inactive_amount** | **str** | The total inactive amount. | 

## Example

```python
from fireblocks.models.delegation_blockchain_position_info import DelegationBlockchainPositionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationBlockchainPositionInfo from a JSON string
delegation_blockchain_position_info_instance = DelegationBlockchainPositionInfo.from_json(json)
# print the JSON string representation of the object
print(DelegationBlockchainPositionInfo.to_json())

# convert the object into a dict
delegation_blockchain_position_info_dict = delegation_blockchain_position_info_instance.to_dict()
# create an instance of DelegationBlockchainPositionInfo from a dict
delegation_blockchain_position_info_from_dict = DelegationBlockchainPositionInfo.from_dict(delegation_blockchain_position_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



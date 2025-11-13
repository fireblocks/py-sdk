# AchAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**bank_name** | **str** | Name of the bank. | [optional] 
**bank_account_number** | **str** | The bank account number for the ACH transfer. | 
**routing_number** | **str** | Routing number identifying the bank account. | 
**account_type** | [**AchAccountType**](AchAccountType.md) |  | 

## Example

```python
from fireblocks.models.ach_address import AchAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AchAddress from a JSON string
ach_address_instance = AchAddress.from_json(json)
# print the JSON string representation of the object
print(AchAddress.to_json())

# convert the object into a dict
ach_address_dict = ach_address_instance.to_dict()
# create an instance of AchAddress from a dict
ach_address_from_dict = AchAddress.from_dict(ach_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



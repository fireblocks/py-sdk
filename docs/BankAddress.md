# BankAddress

Address of the bank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** |  | [optional] 
**building_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**subdivision** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.bank_address import BankAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BankAddress from a JSON string
bank_address_instance = BankAddress.from_json(json)
# print the JSON string representation of the object
print(BankAddress.to_json())

# convert the object into a dict
bank_address_dict = bank_address_instance.to_dict()
# create an instance of BankAddress from a dict
bank_address_from_dict = BankAddress.from_dict(bank_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



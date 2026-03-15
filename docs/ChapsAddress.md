# ChapsAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**sort_code** | **str** | UK bank sort code (format XX-XX-XX) | 
**account_number** | **str** | UK bank account number | 
**bank_name** | **str** | Name of the bank | [optional] 
**bank_account_country** | **str** | CHAPS bank account holder name | 
**bank_account_holder_name** | **str** | CHAPS bank account holder name | 

## Example

```python
from fireblocks.models.chaps_address import ChapsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ChapsAddress from a JSON string
chaps_address_instance = ChapsAddress.from_json(json)
# print the JSON string representation of the object
print(ChapsAddress.to_json())

# convert the object into a dict
chaps_address_dict = chaps_address_instance.to_dict()
# create an instance of ChapsAddress from a dict
chaps_address_from_dict = ChapsAddress.from_dict(chaps_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



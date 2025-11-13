# SpeiAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**bank_name** | **str** | Name of the bank. | [optional] 
**bank_account_number** | **str** | The bank account number for the SPEI transfer. | 

## Example

```python
from fireblocks.models.spei_address import SpeiAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SpeiAddress from a JSON string
spei_address_instance = SpeiAddress.from_json(json)
# print the JSON string representation of the object
print(SpeiAddress.to_json())

# convert the object into a dict
spei_address_dict = spei_address_instance.to_dict()
# create an instance of SpeiAddress from a dict
spei_address_from_dict = SpeiAddress.from_dict(spei_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



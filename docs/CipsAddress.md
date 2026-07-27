# CipsAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**bank_name** | **str** | Name of the recipient&#39;s bank | 
**bank_country** | **str** | ISO 3166-1 alpha-2 country code of the bank | 
**swift_code** | **str** | SWIFT/BIC code of the recipient bank | 
**account_number** | **str** | Recipient bank account number | 

## Example

```python
from fireblocks.models.cips_address import CipsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CipsAddress from a JSON string
cips_address_instance = CipsAddress.from_json(json)
# print the JSON string representation of the object
print(CipsAddress.to_json())

# convert the object into a dict
cips_address_dict = cips_address_instance.to_dict()
# create an instance of CipsAddress from a dict
cips_address_from_dict = CipsAddress.from_dict(cips_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



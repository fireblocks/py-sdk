# PayidAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**value** | **str** | The PayID identifier (email, phone, ABN, or organization ID) | 
**type** | **str** | The type of PayID being used | 
**bsb** | **str** | Bank State Branch (BSB) number (6 digits, format XXX-XXX) | [optional] 
**account_number** | **str** | Australian bank account number | 

## Example

```python
from fireblocks.models.payid_address import PayidAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PayidAddress from a JSON string
payid_address_instance = PayidAddress.from_json(json)
# print the JSON string representation of the object
print(PayidAddress.to_json())

# convert the object into a dict
payid_address_dict = payid_address_instance.to_dict()
# create an instance of PayidAddress from a dict
payid_address_from_dict = PayidAddress.from_dict(payid_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



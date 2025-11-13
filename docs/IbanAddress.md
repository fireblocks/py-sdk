# IbanAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**iban** | **str** |  | 

## Example

```python
from fireblocks.models.iban_address import IbanAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IbanAddress from a JSON string
iban_address_instance = IbanAddress.from_json(json)
# print the JSON string representation of the object
print(IbanAddress.to_json())

# convert the object into a dict
iban_address_dict = iban_address_instance.to_dict()
# create an instance of IbanAddress from a dict
iban_address_from_dict = IbanAddress.from_dict(iban_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



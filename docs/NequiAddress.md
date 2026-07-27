# NequiAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Recipient phone number in E.164 format | 

## Example

```python
from fireblocks.models.nequi_address import NequiAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NequiAddress from a JSON string
nequi_address_instance = NequiAddress.from_json(json)
# print the JSON string representation of the object
print(NequiAddress.to_json())

# convert the object into a dict
nequi_address_dict = nequi_address_instance.to_dict()
# create an instance of NequiAddress from a dict
nequi_address_from_dict = NequiAddress.from_dict(nequi_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



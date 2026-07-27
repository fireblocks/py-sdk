# PesonetAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**bank_name** | **str** | Name of the recipient&#39;s bank | 
**account_number** | **str** | Recipient bank account number | 

## Example

```python
from fireblocks.models.pesonet_address import PesonetAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PesonetAddress from a JSON string
pesonet_address_instance = PesonetAddress.from_json(json)
# print the JSON string representation of the object
print(PesonetAddress.to_json())

# convert the object into a dict
pesonet_address_dict = pesonet_address_instance.to_dict()
# create an instance of PesonetAddress from a dict
pesonet_address_from_dict = PesonetAddress.from_dict(pesonet_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



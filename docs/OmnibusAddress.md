# OmnibusAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index of the deposit address within the omnibus account | 
**address** | **str** | The deposit address | 
**description** | **str** | The caller-supplied label of the address. Absent when no label was set. | [optional] 
**created_at** | **str** | The time the address was created, in epoch milliseconds | 

## Example

```python
from fireblocks.models.omnibus_address import OmnibusAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OmnibusAddress from a JSON string
omnibus_address_instance = OmnibusAddress.from_json(json)
# print the JSON string representation of the object
print(OmnibusAddress.to_json())

# convert the object into a dict
omnibus_address_dict = omnibus_address_instance.to_dict()
# create an instance of OmnibusAddress from a dict
omnibus_address_from_dict = OmnibusAddress.from_dict(omnibus_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



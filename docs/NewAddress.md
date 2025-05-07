# NewAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address string. | 
**index** | **int** | The index of the address in the list. | 
**description** | **str** | A description of the address. | 

## Example

```python
from fireblocks.models.new_address import NewAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NewAddress from a JSON string
new_address_instance = NewAddress.from_json(json)
# print the JSON string representation of the object
print(NewAddress.to_json())

# convert the object into a dict
new_address_dict = new_address_instance.to_dict()
# create an instance of NewAddress from a dict
new_address_from_dict = NewAddress.from_dict(new_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Cosigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | Whether the cosigner is archived | 
**id** | **str** | The unique identifier of the cosigner | 
**name** | **str** | The name of the cosigner | [optional] 

## Example

```python
from fireblocks.models.cosigner import Cosigner

# TODO update the JSON string below
json = "{}"
# create an instance of Cosigner from a JSON string
cosigner_instance = Cosigner.from_json(json)
# print the JSON string representation of the object
print(Cosigner.to_json())

# convert the object into a dict
cosigner_dict = cosigner_instance.to_dict()
# create an instance of Cosigner from a dict
cosigner_from_dict = Cosigner.from_dict(cosigner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



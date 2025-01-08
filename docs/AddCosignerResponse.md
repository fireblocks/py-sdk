# AddCosignerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | The id of the API key to be paired with the cosigner | 
**name** | **str** | The name of the cosigner | 
**existing_cosigner** | **bool** | Whether the cosigner already exists in another workspace | [optional] [default to False]
**pending_cosigner_id** | **str** | The unique identifier of a pending cosigner | 

## Example

```python
from fireblocks.models.add_cosigner_response import AddCosignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCosignerResponse from a JSON string
add_cosigner_response_instance = AddCosignerResponse.from_json(json)
# print the JSON string representation of the object
print(AddCosignerResponse.to_json())

# convert the object into a dict
add_cosigner_response_dict = add_cosigner_response_instance.to_dict()
# create an instance of AddCosignerResponse from a dict
add_cosigner_response_from_dict = AddCosignerResponse.from_dict(add_cosigner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AddCosignerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | The id of the API key to be paired with the cosigner | 
**name** | **str** | The name of the cosigner | 
**existing_cosigner** | **bool** | Whether the cosigner already exists in another workspace | [optional] [default to False]

## Example

```python
from fireblocks.models.add_cosigner_request import AddCosignerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCosignerRequest from a JSON string
add_cosigner_request_instance = AddCosignerRequest.from_json(json)
# print the JSON string representation of the object
print(AddCosignerRequest.to_json())

# convert the object into a dict
add_cosigner_request_dict = add_cosigner_request_instance.to_dict()
# create an instance of AddCosignerRequest from a dict
add_cosigner_request_from_dict = AddCosignerRequest.from_dict(add_cosigner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



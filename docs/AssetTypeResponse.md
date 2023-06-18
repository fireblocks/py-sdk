# AssetTypeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**contract_address** | **str** |  | [optional] 
**native_asset** | **str** |  | [optional] 
**decimals** | **float** |  | [optional] 

## Example

```python
from fireblocks_client.models.asset_type_response import AssetTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeResponse from a JSON string
asset_type_response_instance = AssetTypeResponse.from_json(json)
# print the JSON string representation of the object
print AssetTypeResponse.to_json()

# convert the object into a dict
asset_type_response_dict = asset_type_response_instance.to_dict()
# create an instance of AssetTypeResponse from a dict
asset_type_response_form_dict = asset_type_response.from_dict(asset_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



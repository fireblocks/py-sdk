# ConvertAssetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the conversion was successful | 

## Example

```python
from fireblocks_client.models.convert_assets_response import ConvertAssetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertAssetsResponse from a JSON string
convert_assets_response_instance = ConvertAssetsResponse.from_json(json)
# print the JSON string representation of the object
print ConvertAssetsResponse.to_json()

# convert the object into a dict
convert_assets_response_dict = convert_assets_response_instance.to_dict()
# create an instance of ConvertAssetsResponse from a dict
convert_assets_response_form_dict = convert_assets_response.from_dict(convert_assets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



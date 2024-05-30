# ConvertAssetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_asset** | **str** | Name of the source asset (must be in a currency that is supported for conversions in the selected exchange type that corresponds to your exchange ID) | 
**dest_asset** | **str** | Name of the destination asset (must be in a currency that is supported for conversions in the selected exchange type that corresponds to your exchange ID) | 
**amount** | **float** | The amount to transfer (in the currency of the source asset) | 

## Example

```python
from fireblocks_client.models.convert_assets_request import ConvertAssetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertAssetsRequest from a JSON string
convert_assets_request_instance = ConvertAssetsRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertAssetsRequest.to_json())

# convert the object into a dict
convert_assets_request_dict = convert_assets_request_instance.to_dict()
# create an instance of ConvertAssetsRequest from a dict
convert_assets_request_from_dict = ConvertAssetsRequest.from_dict(convert_assets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



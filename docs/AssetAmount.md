# AssetAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**asset_id** | **str** |  | 

## Example

```python
from fireblocks_client.models.asset_amount import AssetAmount

# TODO update the JSON string below
json = "{}"
# create an instance of AssetAmount from a JSON string
asset_amount_instance = AssetAmount.from_json(json)
# print the JSON string representation of the object
print(AssetAmount.to_json())

# convert the object into a dict
asset_amount_dict = asset_amount_instance.to_dict()
# create an instance of AssetAmount from a dict
asset_amount_from_dict = AssetAmount.from_dict(asset_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



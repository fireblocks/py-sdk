# AssetNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Asset user note | [optional] 

## Example

```python
from fireblocks.models.asset_note_request import AssetNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetNoteRequest from a JSON string
asset_note_request_instance = AssetNoteRequest.from_json(json)
# print the JSON string representation of the object
print(AssetNoteRequest.to_json())

# convert the object into a dict
asset_note_request_dict = asset_note_request_instance.to_dict()
# create an instance of AssetNoteRequest from a dict
asset_note_request_from_dict = AssetNoteRequest.from_dict(asset_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AssetNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Note content | 
**user_id** | **str** | Who updated the note (uuid) | 
**user_name** | **str** | User name | 
**updated_at** | **datetime** | ISO Timestamp when last updated | 

## Example

```python
from fireblocks.models.asset_note import AssetNote

# TODO update the JSON string below
json = "{}"
# create an instance of AssetNote from a JSON string
asset_note_instance = AssetNote.from_json(json)
# print the JSON string representation of the object
print(AssetNote.to_json())

# convert the object into a dict
asset_note_dict = asset_note_instance.to_dict()
# create an instance of AssetNote from a dict
asset_note_from_dict = AssetNote.from_dict(asset_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MediaEntityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Cached accessible URL | 
**content_type** | **str** | Media type | 

## Example

```python
from fireblocks.models.media_entity_response import MediaEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MediaEntityResponse from a JSON string
media_entity_response_instance = MediaEntityResponse.from_json(json)
# print the JSON string representation of the object
print(MediaEntityResponse.to_json())

# convert the object into a dict
media_entity_response_dict = media_entity_response_instance.to_dict()
# create an instance of MediaEntityResponse from a dict
media_entity_response_from_dict = MediaEntityResponse.from_dict(media_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Tag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tag | 
**label** | **str** | The tag label | 
**description** | **str** | Description for the tag | [optional] 
**color** | **str** | The tag color in hex format | [optional] 
**is_protected** | **bool** | Indication if the tag is a protected tag | [default to False]
**updated_at** | **float** | The date and time the tag was last updated | 
**type** | [**TagType**](TagType.md) |  | [optional] 
**allowed_entity_types** | **List[str]** | The entity types this tag may be attached to. Tags created before this field was introduced read back as [&#39;vault_account&#39;]. Known values: vault_account (default), contact. | [optional] 
**pending_approval_request** | [**ApprovalRequest**](ApprovalRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print(Tag.to_json())

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_from_dict = Tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



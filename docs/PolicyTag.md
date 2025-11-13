# PolicyTag

Policy tag for matching

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tag identifier | 

## Example

```python
from fireblocks.models.policy_tag import PolicyTag

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTag from a JSON string
policy_tag_instance = PolicyTag.from_json(json)
# print the JSON string representation of the object
print(PolicyTag.to_json())

# convert the object into a dict
policy_tag_dict = policy_tag_instance.to_dict()
# create an instance of PolicyTag from a dict
policy_tag_from_dict = PolicyTag.from_dict(policy_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



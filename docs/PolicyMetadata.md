# PolicyMetadata

Policy related metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edited_by** | **str** | The user id of the user who last edited the policy | [optional] 
**edited_at** | **str** | The timestamp of the last edit of the policy | [optional] 
**published_by** | **str** | The user id of the user who last published the policy | [optional] 
**published_at** | **str** | The timestamp of the last publish of the policy | [optional] 

## Example

```python
from fireblocks.models.policy_metadata import PolicyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyMetadata from a JSON string
policy_metadata_instance = PolicyMetadata.from_json(json)
# print the JSON string representation of the object
print(PolicyMetadata.to_json())

# convert the object into a dict
policy_metadata_dict = policy_metadata_instance.to_dict()
# create an instance of PolicyMetadata from a dict
policy_metadata_from_dict = PolicyMetadata.from_dict(policy_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



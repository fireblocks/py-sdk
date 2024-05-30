# PublishResult

Response object of the publish policy operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PolicyStatus**](PolicyStatus.md) |  | 
**rules** | [**List[PolicyRule]**](PolicyRule.md) |  | 
**check_result** | [**PolicyCheckResult**](PolicyCheckResult.md) |  | 
**metadata** | [**PolicyMetadata**](PolicyMetadata.md) |  | 

## Example

```python
from fireblocks.models.publish_result import PublishResult

# TODO update the JSON string below
json = "{}"
# create an instance of PublishResult from a JSON string
publish_result_instance = PublishResult.from_json(json)
# print the JSON string representation of the object
print(PublishResult.to_json())

# convert the object into a dict
publish_result_dict = publish_result_instance.to_dict()
# create an instance of PublishResult from a dict
publish_result_from_dict = PublishResult.from_dict(publish_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



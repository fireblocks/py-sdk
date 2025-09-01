# LegacyPublishResult

Response object of the publish policy operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**LegacyPolicyStatus**](LegacyPolicyStatus.md) |  | 
**rules** | [**List[LegacyPolicyRule]**](LegacyPolicyRule.md) |  | 
**check_result** | [**LegacyPolicyCheckResult**](LegacyPolicyCheckResult.md) |  | 
**metadata** | [**LegacyPolicyMetadata**](LegacyPolicyMetadata.md) |  | 

## Example

```python
from fireblocks.models.legacy_publish_result import LegacyPublishResult

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPublishResult from a JSON string
legacy_publish_result_instance = LegacyPublishResult.from_json(json)
# print the JSON string representation of the object
print(LegacyPublishResult.to_json())

# convert the object into a dict
legacy_publish_result_dict = legacy_publish_result_instance.to_dict()
# create an instance of LegacyPublishResult from a dict
legacy_publish_result_from_dict = LegacyPublishResult.from_dict(legacy_publish_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



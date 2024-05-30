# SpamOwnershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | Token spam result | 
**source** | **str** | Source of Token&#39;s Spam status value | 

## Example

```python
from fireblocks.models.spam_ownership_response import SpamOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpamOwnershipResponse from a JSON string
spam_ownership_response_instance = SpamOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print(SpamOwnershipResponse.to_json())

# convert the object into a dict
spam_ownership_response_dict = spam_ownership_response_instance.to_dict()
# create an instance of SpamOwnershipResponse from a dict
spam_ownership_response_from_dict = SpamOwnershipResponse.from_dict(spam_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



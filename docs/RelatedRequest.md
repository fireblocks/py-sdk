# RelatedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the request | 
**in_progress** | **bool** | Indicates whether there is an ongoing action for this position related to this request | 
**amount** | **str** | Amount of tokens to Unstake | 
**tx_id** | **str** | The transaction ID of the ongoing request | [optional] 

## Example

```python
from fireblocks.models.related_request import RelatedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedRequest from a JSON string
related_request_instance = RelatedRequest.from_json(json)
# print the JSON string representation of the object
print(RelatedRequest.to_json())

# convert the object into a dict
related_request_dict = related_request_instance.to_dict()
# create an instance of RelatedRequest from a dict
related_request_from_dict = RelatedRequest.from_dict(related_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RelatedRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RelatedRequestStatusType**](RelatedRequestStatusType.md) |  | 
**in_progress** | **bool** | Indicates whether there is an ongoing action for this position related to this request | 
**amount** | **str** | Amount of tokens to Unstake | 
**tx_id** | **str** | The transaction ID of the ongoing request | [optional] 

## Example

```python
from fireblocks.models.related_request_dto import RelatedRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedRequestDto from a JSON string
related_request_dto_instance = RelatedRequestDto.from_json(json)
# print the JSON string representation of the object
print(RelatedRequestDto.to_json())

# convert the object into a dict
related_request_dto_dict = related_request_dto_instance.to_dict()
# create an instance of RelatedRequestDto from a dict
related_request_dto_from_dict = RelatedRequestDto.from_dict(related_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



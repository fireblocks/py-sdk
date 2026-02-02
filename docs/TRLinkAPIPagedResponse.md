# TRLinkAPIPagedResponse

Generic paginated response wrapper with cursor-based pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TRLinkVaspListDto]**](TRLinkVaspListDto.md) | Array of result items | 
**paging** | [**TRLinkPaging**](TRLinkPaging.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_api_paged_response import TRLinkAPIPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAPIPagedResponse from a JSON string
tr_link_api_paged_response_instance = TRLinkAPIPagedResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkAPIPagedResponse.to_json())

# convert the object into a dict
tr_link_api_paged_response_dict = tr_link_api_paged_response_instance.to_dict()
# create an instance of TRLinkAPIPagedResponse from a dict
tr_link_api_paged_response_from_dict = TRLinkAPIPagedResponse.from_dict(tr_link_api_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



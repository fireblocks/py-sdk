# TRLinkPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor for next page | 

## Example

```python
from fireblocks.models.tr_link_paging import TRLinkPaging

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkPaging from a JSON string
tr_link_paging_instance = TRLinkPaging.from_json(json)
# print the JSON string representation of the object
print(TRLinkPaging.to_json())

# convert the object into a dict
tr_link_paging_dict = tr_link_paging_instance.to_dict()
# create an instance of TRLinkPaging from a dict
tr_link_paging_from_dict = TRLinkPaging.from_dict(tr_link_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



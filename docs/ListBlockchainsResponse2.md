# ListBlockchainsResponse2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Blockchain]**](Blockchain.md) | Blockchains for the current page. | 
**total** | **float** | Total number of items across all pages, matching the current filter. | 
**next** | **str** | Cursor for the next page; absent when the current page is the last. Opaque base64 blob bundling the target pageCursor and current query params (pageSize, search, status, statusExclude, blockchainEnv, sortBy, order). | [optional] 
**prev** | **str** | Cursor for the previous page; absent when the current page is the first. | [optional] 

## Example

```python
from fireblocks.models.list_blockchains_response2 import ListBlockchainsResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of ListBlockchainsResponse2 from a JSON string
list_blockchains_response2_instance = ListBlockchainsResponse2.from_json(json)
# print the JSON string representation of the object
print(ListBlockchainsResponse2.to_json())

# convert the object into a dict
list_blockchains_response2_dict = list_blockchains_response2_instance.to_dict()
# create an instance of ListBlockchainsResponse2 from a dict
list_blockchains_response2_from_dict = ListBlockchainsResponse2.from_dict(list_blockchains_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



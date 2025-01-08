# ListBlockchainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BlockchainResponse]**](BlockchainResponse.md) | The data of the current page | 
**next** | **str** | Cursor to the next page | 

## Example

```python
from fireblocks.models.list_blockchains_response import ListBlockchainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBlockchainsResponse from a JSON string
list_blockchains_response_instance = ListBlockchainsResponse.from_json(json)
# print the JSON string representation of the object
print(ListBlockchainsResponse.to_json())

# convert the object into a dict
list_blockchains_response_dict = list_blockchains_response_instance.to_dict()
# create an instance of ListBlockchainsResponse from a dict
list_blockchains_response_from_dict = ListBlockchainsResponse.from_dict(list_blockchains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



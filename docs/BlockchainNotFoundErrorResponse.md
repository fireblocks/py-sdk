# BlockchainNotFoundErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not found error code | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.blockchain_not_found_error_response import BlockchainNotFoundErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainNotFoundErrorResponse from a JSON string
blockchain_not_found_error_response_instance = BlockchainNotFoundErrorResponse.from_json(json)
# print the JSON string representation of the object
print(BlockchainNotFoundErrorResponse.to_json())

# convert the object into a dict
blockchain_not_found_error_response_dict = blockchain_not_found_error_response_instance.to_dict()
# create an instance of BlockchainNotFoundErrorResponse from a dict
blockchain_not_found_error_response_from_dict = BlockchainNotFoundErrorResponse.from_dict(blockchain_not_found_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



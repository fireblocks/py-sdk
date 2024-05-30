# HttpContractDoesNotExistError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not Found error code | [optional] 
**code** | **str** | Error code | [optional] 

## Example

```python
from fireblocks.models.http_contract_does_not_exist_error import HttpContractDoesNotExistError

# TODO update the JSON string below
json = "{}"
# create an instance of HttpContractDoesNotExistError from a JSON string
http_contract_does_not_exist_error_instance = HttpContractDoesNotExistError.from_json(json)
# print the JSON string representation of the object
print(HttpContractDoesNotExistError.to_json())

# convert the object into a dict
http_contract_does_not_exist_error_dict = http_contract_does_not_exist_error_instance.to_dict()
# create an instance of HttpContractDoesNotExistError from a dict
http_contract_does_not_exist_error_from_dict = HttpContractDoesNotExistError.from_dict(http_contract_does_not_exist_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeployedContractNotFoundError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not Found error message | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.deployed_contract_not_found_error import DeployedContractNotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of DeployedContractNotFoundError from a JSON string
deployed_contract_not_found_error_instance = DeployedContractNotFoundError.from_json(json)
# print the JSON string representation of the object
print(DeployedContractNotFoundError.to_json())

# convert the object into a dict
deployed_contract_not_found_error_dict = deployed_contract_not_found_error_instance.to_dict()
# create an instance of DeployedContractNotFoundError from a dict
deployed_contract_not_found_error_from_dict = DeployedContractNotFoundError.from_dict(deployed_contract_not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



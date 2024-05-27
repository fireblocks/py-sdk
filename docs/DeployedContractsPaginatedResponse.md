# DeployedContractsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LeanDeployedContractResponseDto]**](LeanDeployedContractResponseDto.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks_client.models.deployed_contracts_paginated_response import DeployedContractsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeployedContractsPaginatedResponse from a JSON string
deployed_contracts_paginated_response_instance = DeployedContractsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print DeployedContractsPaginatedResponse.to_json()

# convert the object into a dict
deployed_contracts_paginated_response_dict = deployed_contracts_paginated_response_instance.to_dict()
# create an instance of DeployedContractsPaginatedResponse from a dict
deployed_contracts_paginated_response_form_dict = deployed_contracts_paginated_response.from_dict(deployed_contracts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



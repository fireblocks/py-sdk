# CreateContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the contract&#39;s display name | [optional] 

## Example

```python
from fireblocks_client.models.create_contract_request import CreateContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractRequest from a JSON string
create_contract_request_instance = CreateContractRequest.from_json(json)
# print the JSON string representation of the object
print CreateContractRequest.to_json()

# convert the object into a dict
create_contract_request_dict = create_contract_request_instance.to_dict()
# create an instance of CreateContractRequest from a dict
create_contract_request_form_dict = create_contract_request.from_dict(create_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



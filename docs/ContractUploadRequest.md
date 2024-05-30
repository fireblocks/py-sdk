# ContractUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the contract template | 
**description** | **str** | A short description of the contract template | 
**long_description** | **str** | A full description of the contract template. May contain   to break the lines | [optional] 
**bytecode** | **str** | The compiled artifact of this smart contract. Used for deployment of this contract template | 
**sourcecode** | **str** | The source code of the contract. Optional. | [optional] 
**type** | **str** | The type of the contract template | [optional] 
**docs** | [**ContractDoc**](ContractDoc.md) | A &#x60;natspec&#x60; compliant documentation json. Can be retrieved from the output json after compilation | [optional] 
**abi** | **List[List[AbiFunction]]** |  | 
**attributes** | [**ContractAttributes**](ContractAttributes.md) | The attributes related to this contract template. It will be displayed in the tokenization page | [optional] 

## Example

```python
from fireblocks.models.contract_upload_request import ContractUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContractUploadRequest from a JSON string
contract_upload_request_instance = ContractUploadRequest.from_json(json)
# print the JSON string representation of the object
print(ContractUploadRequest.to_json())

# convert the object into a dict
contract_upload_request_dict = contract_upload_request_instance.to_dict()
# create an instance of ContractUploadRequest from a dict
contract_upload_request_from_dict = ContractUploadRequest.from_dict(contract_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



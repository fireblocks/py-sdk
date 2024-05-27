# ValidatorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;) of the validator | 
**fee_percent** | **float** | The service fee as a percentage out of the earned rewards | 

## Example

```python
from fireblocks_client.models.validator_dto import ValidatorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorDto from a JSON string
validator_dto_instance = ValidatorDto.from_json(json)
# print the JSON string representation of the object
print ValidatorDto.to_json()

# convert the object into a dict
validator_dto_dict = validator_dto_instance.to_dict()
# create an instance of ValidatorDto from a dict
validator_dto_form_dict = validator_dto.from_dict(validator_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



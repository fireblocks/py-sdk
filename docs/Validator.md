# Validator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;) of the validator | 
**fee_percent** | **float** | The service fee as a percentage out of the earned rewards | 
**is_private** | **bool** | Is the validator private, i.e created by the user | [optional] 

## Example

```python
from fireblocks.models.validator import Validator

# TODO update the JSON string below
json = "{}"
# create an instance of Validator from a JSON string
validator_instance = Validator.from_json(json)
# print the JSON string representation of the object
print(Validator.to_json())

# convert the object into a dict
validator_dict = validator_instance.to_dict()
# create an instance of Validator from a dict
validator_from_dict = Validator.from_dict(validator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



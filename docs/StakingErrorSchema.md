# StakingErrorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable error message. | 
**code** | **float** | Numeric error code identifying the type of error. | 
**descriptor** | **str** | Additional structured context about the error. | [optional] 

## Example

```python
from fireblocks.models.staking_error_schema import StakingErrorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StakingErrorSchema from a JSON string
staking_error_schema_instance = StakingErrorSchema.from_json(json)
# print the JSON string representation of the object
print(StakingErrorSchema.to_json())

# convert the object into a dict
staking_error_schema_dict = staking_error_schema_instance.to_dict()
# create an instance of StakingErrorSchema from a dict
staking_error_schema_from_dict = StakingErrorSchema.from_dict(staking_error_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



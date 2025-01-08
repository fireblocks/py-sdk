# StakeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the staking position | 

## Example

```python
from fireblocks.models.stake_response import StakeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StakeResponse from a JSON string
stake_response_instance = StakeResponse.from_json(json)
# print the JSON string representation of the object
print(StakeResponse.to_json())

# convert the object into a dict
stake_response_dict = stake_response_instance.to_dict()
# create an instance of StakeResponse from a dict
stake_response_from_dict = StakeResponse.from_dict(stake_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



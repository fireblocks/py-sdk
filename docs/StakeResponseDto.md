# StakeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the staking position | 

## Example

```python
from fireblocks_client.models.stake_response_dto import StakeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of StakeResponseDto from a JSON string
stake_response_dto_instance = StakeResponseDto.from_json(json)
# print the JSON string representation of the object
print(StakeResponseDto.to_json())

# convert the object into a dict
stake_response_dto_dict = stake_response_dto_instance.to_dict()
# create an instance of StakeResponseDto from a dict
stake_response_dto_from_dict = StakeResponseDto.from_dict(stake_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



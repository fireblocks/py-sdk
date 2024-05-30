# StakeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The source vault account to stake from | 
**provider_id** | **str** | The ID of the provider | 
**stake_amount** | **str** | Amount of tokens to stake | 
**tx_note** | **str** | The note to associate with the stake transactions. | [optional] 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | **str** | Represents the fee level for a transaction, which can be set as slow, medium, or fast. Only one of fee/feeLevel is required. | [optional] 

## Example

```python
from fireblocks_client.models.stake_request_dto import StakeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of StakeRequestDto from a JSON string
stake_request_dto_instance = StakeRequestDto.from_json(json)
# print the JSON string representation of the object
print(StakeRequestDto.to_json())

# convert the object into a dict
stake_request_dto_dict = stake_request_dto_instance.to_dict()
# create an instance of StakeRequestDto from a dict
stake_request_dto_from_dict = StakeRequestDto.from_dict(stake_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



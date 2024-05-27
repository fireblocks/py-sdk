# UnstakeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of position to unstake | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | **str** | Represents the fee level for a transaction, which can be set as slow, medium, or fast. Only one of fee/feeLevel is required. | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 

## Example

```python
from fireblocks_client.models.unstake_request_dto import UnstakeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnstakeRequestDto from a JSON string
unstake_request_dto_instance = UnstakeRequestDto.from_json(json)
# print the JSON string representation of the object
print UnstakeRequestDto.to_json()

# convert the object into a dict
unstake_request_dto_dict = unstake_request_dto_instance.to_dict()
# create an instance of UnstakeRequestDto from a dict
unstake_request_dto_form_dict = unstake_request_dto.from_dict(unstake_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



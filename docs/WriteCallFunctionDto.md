# WriteCallFunctionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account id this contract was deploy from | 
**abi_function** | [**WriteAbiFunction**](WriteAbiFunction.md) |  | 
**amount** | **str** | Amount in base asset. Being used in payable functions | [optional] 
**fee_level** | **str** | Fee level for the write function transaction. interchangeable with the &#39;fee&#39; field | [optional] 
**fee** | **str** | Max fee amount for the write function transaction. interchangeable with the &#39;feeLevel&#39; field | [optional] 
**note** | **str** | Custom note, not sent to the blockchain, that describes the transaction at your Fireblocks workspace | [optional] 

## Example

```python
from fireblocks.models.write_call_function_dto import WriteCallFunctionDto

# TODO update the JSON string below
json = "{}"
# create an instance of WriteCallFunctionDto from a JSON string
write_call_function_dto_instance = WriteCallFunctionDto.from_json(json)
# print the JSON string representation of the object
print(WriteCallFunctionDto.to_json())

# convert the object into a dict
write_call_function_dto_dict = write_call_function_dto_instance.to_dict()
# create an instance of WriteCallFunctionDto from a dict
write_call_function_dto_from_dict = WriteCallFunctionDto.from_dict(write_call_function_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



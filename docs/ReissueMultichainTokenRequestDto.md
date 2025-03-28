# ReissueMultichainTokenRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The id of the vault account that initiated the request to issue the token | 
**chains** | **List[str]** | The base asset identifiers of the blockchains you want to deploy to | 
**use_gasless** | **bool** | Whether to use gasless deployment or not | [optional] 
**fee** | **str** | Max fee amount for the deploy request. Interchangeable with the &#39;feeLevel&#39; field | [optional] 
**fee_level** | **str** | Fee level for the deploy request. Interchangeable with the &#39;fee&#39; field | [optional] 

## Example

```python
from fireblocks.models.reissue_multichain_token_request_dto import ReissueMultichainTokenRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReissueMultichainTokenRequestDto from a JSON string
reissue_multichain_token_request_dto_instance = ReissueMultichainTokenRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReissueMultichainTokenRequestDto.to_json())

# convert the object into a dict
reissue_multichain_token_request_dto_dict = reissue_multichain_token_request_dto_instance.to_dict()
# create an instance of ReissueMultichainTokenRequestDto from a dict
reissue_multichain_token_request_dto_from_dict = ReissueMultichainTokenRequestDto.from_dict(reissue_multichain_token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



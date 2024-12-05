# CreateTokenRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain_id** | **str** | The id of the blockchain the request was initiated on | [optional] 
**asset_id** | **str** | The base asset identifier of the blockchain you want to deploy to | [optional] 
**vault_account_id** | **str** | The id of the vault account that initiated the request to issue the token | 
**create_params** | [**CreateTokenRequestDtoCreateParams**](CreateTokenRequestDtoCreateParams.md) |  | 
**display_name** | **str** |  | [optional] 
**use_gasless** | **bool** | Indicates whether the token should be created in a gasless manner, utilizing the ERC-2771 standard. When set to true, the transaction will be relayed by a designated relayer. The workspace must be configured to use Fireblocks gasless relay. | [optional] 
**fee** | **str** | Max fee amount for the write function transaction. interchangeable with the &#39;feeLevel&#39; field | [optional] 
**fee_level** | **str** | Fee level for the write function transaction. interchangeable with the &#39;fee&#39; field | [optional] 

## Example

```python
from fireblocks.models.create_token_request_dto import CreateTokenRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenRequestDto from a JSON string
create_token_request_dto_instance = CreateTokenRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateTokenRequestDto.to_json())

# convert the object into a dict
create_token_request_dto_dict = create_token_request_dto_instance.to_dict()
# create an instance of CreateTokenRequestDto from a dict
create_token_request_dto_from_dict = CreateTokenRequestDto.from_dict(create_token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



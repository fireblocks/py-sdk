# CreateTokenRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain_id** | **str** | The id of the blockchain the request was initiated on | [optional] 
**asset_id** | **str** | The base asset identifier of the blockchain you want to deploy to | [optional] 
**vault_account_id** | **str** | The id of the vault account that initiated the request to issue the token | 
**create_params** | [**CreateTokenRequestDtoCreateParams**](CreateTokenRequestDtoCreateParams.md) |  | 
**display_name** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.create_token_request_dto import CreateTokenRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenRequestDto from a JSON string
create_token_request_dto_instance = CreateTokenRequestDto.from_json(json)
# print the JSON string representation of the object
print CreateTokenRequestDto.to_json()

# convert the object into a dict
create_token_request_dto_dict = create_token_request_dto_instance.to_dict()
# create an instance of CreateTokenRequestDto from a dict
create_token_request_dto_form_dict = create_token_request_dto.from_dict(create_token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateMultichainTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The id of the vault account that initiated the request to issue the token | 
**create_params** | [**CreateMultichainTokenRequestCreateParams**](CreateMultichainTokenRequestCreateParams.md) |  | 
**salt** | **str** | The salt to calculate the deterministic address. Must be a number between 0 and 2^256 -1, for it to fit in the bytes32 parameter. | [optional] 
**chains** | **List[str]** | The base asset identifiers of the blockchains (legacyId) to calculate deterministic addresses | 
**display_name** | **str** |  | [optional] 
**use_gasless** | **bool** | Indicates whether the token should be created in a gasless manner, utilizing the ERC-2771 standard. When set to true, the transaction will be relayed by a designated relayer. The workspace must be configured to use Fireblocks gasless relay. | [optional] 
**fee** | **str** | Max fee amount for the write function transaction. interchangeable with the &#39;feeLevel&#39; field | [optional] 
**fee_level** | **str** | Fee level for the write function transaction. interchangeable with the &#39;fee&#39; field | [optional] 

## Example

```python
from fireblocks.models.create_multichain_token_request import CreateMultichainTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultichainTokenRequest from a JSON string
create_multichain_token_request_instance = CreateMultichainTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMultichainTokenRequest.to_json())

# convert the object into a dict
create_multichain_token_request_dict = create_multichain_token_request_instance.to_dict()
# create an instance of CreateMultichainTokenRequest from a dict
create_multichain_token_request_from_dict = CreateMultichainTokenRequest.from_dict(create_multichain_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



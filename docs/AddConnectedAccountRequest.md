# AddConnectedAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Integration key identifying the provider (e.g. BINANCE, KINGDOM_BANK, GEMINI_NLV2). | 
**display_name** | **str** | Human-readable account name. Required for non-NLV2 providers. | [optional] 
**creds** | **bytearray** | Base64-encoded RSA-encrypted credential blob. Encrypt using the public key from GET /exchange_accounts/credentials_public_key. | 
**api_key** | **str** | Account-level API key. | 
**main_account_id** | **str** | Parent main account ID for sub-account creation. Not allowed for NLV2 providers. | [optional] 
**account_id** | **str** | Optional provider-side account ID to associate with the created account. | [optional] 
**on_premise_server_id** | **str** | On-premise server ID for self-hosted integrations. | [optional] 

## Example

```python
from fireblocks.models.add_connected_account_request import AddConnectedAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddConnectedAccountRequest from a JSON string
add_connected_account_request_instance = AddConnectedAccountRequest.from_json(json)
# print the JSON string representation of the object
print(AddConnectedAccountRequest.to_json())

# convert the object into a dict
add_connected_account_request_dict = add_connected_account_request_instance.to_dict()
# create an instance of AddConnectedAccountRequest from a dict
add_connected_account_request_from_dict = AddConnectedAccountRequest.from_dict(add_connected_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



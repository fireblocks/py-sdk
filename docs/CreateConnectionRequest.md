# CreateConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **float** | The ID of the vault to connect to the dApp. | 
**fee_level** | **str** | The default fee level. Valid values are &#x60;MEDIUM&#x60; and &#x60;HIGH&#x60;. | 
**uri** | **str** | The WalletConnect uri provided by the dapp. | 
**chain_ids** | **List[str]** | The IDs of the blockchain networks used in the Web3 connection (Currently required in V1 connections only). | [optional] 
**ncw_id** | **str** | The ID of the Non-Custodial Wallet to connect to the dApp. | 
**ncw_account_id** | **float** | The NCW account ID to connect to the dApp. | 

## Example

```python
from fireblocks_client.models.create_connection_request import CreateConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionRequest from a JSON string
create_connection_request_instance = CreateConnectionRequest.from_json(json)
# print the JSON string representation of the object
print CreateConnectionRequest.to_json()

# convert the object into a dict
create_connection_request_dict = create_connection_request_instance.to_dict()
# create an instance of CreateConnectionRequest from a dict
create_connection_request_form_dict = create_connection_request.from_dict(create_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



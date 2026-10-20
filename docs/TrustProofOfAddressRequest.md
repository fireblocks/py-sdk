# TrustProofOfAddressRequest

Request to create a cryptographic proof of address ownership for TRUST network compliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The ID of the vault account. | 
**asset** | **str** | The asset identifier for which proof of address is being created. | 
**prefix** | **str** | The prefix to be used for signing messages. | 
**trust_uuid** | **str** | A unique identifier (UUID) obtained from TRUST (CreateAddressOwnership) | 
**address** | **str** | Optional non-default (derived) address of the vault account to prove. Supported for UTXO assets only (&#x60;BTC&#x60;, &#x60;BTC_TEST&#x60;). The address must belong to the vault account for the given asset. Both SegWit and Legacy address forms are accepted. When omitted, the proof is created for the default (index 0) address of the vault account.  | [optional] 

## Example

```python
from fireblocks.models.trust_proof_of_address_request import TrustProofOfAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrustProofOfAddressRequest from a JSON string
trust_proof_of_address_request_instance = TrustProofOfAddressRequest.from_json(json)
# print the JSON string representation of the object
print(TrustProofOfAddressRequest.to_json())

# convert the object into a dict
trust_proof_of_address_request_dict = trust_proof_of_address_request_instance.to_dict()
# create an instance of TrustProofOfAddressRequest from a dict
trust_proof_of_address_request_from_dict = TrustProofOfAddressRequest.from_dict(trust_proof_of_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



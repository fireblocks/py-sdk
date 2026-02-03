# TrustProofOfAddressRequest

Request to create a cryptographic proof of address ownership for TRUST network compliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The ID of the vault account. | 
**asset** | **str** | The asset identifier for which proof of address is being created. | 
**prefix** | **str** | The prefix to be used for signing messages. | 
**trust_uuid** | **str** | A unique identifier (UUID) obtained from TRUST (CreateAddressOwnership) | 

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



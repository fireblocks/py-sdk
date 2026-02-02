# TrustProofOfAddressResponse

Response containing the TRUST-compatible encoded signature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID from Fireblocks (UUID format) | 
**status** | [**TypedMessageTransactionStatusEnum**](TypedMessageTransactionStatusEnum.md) |  | 
**signature** | **str** | TRUST-compatible encoded signature for proof of address verification.  | 

## Example

```python
from fireblocks.models.trust_proof_of_address_response import TrustProofOfAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrustProofOfAddressResponse from a JSON string
trust_proof_of_address_response_instance = TrustProofOfAddressResponse.from_json(json)
# print the JSON string representation of the object
print(TrustProofOfAddressResponse.to_json())

# convert the object into a dict
trust_proof_of_address_response_dict = trust_proof_of_address_response_instance.to_dict()
# create an instance of TrustProofOfAddressResponse from a dict
trust_proof_of_address_response_from_dict = TrustProofOfAddressResponse.from_dict(trust_proof_of_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



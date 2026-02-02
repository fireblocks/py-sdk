# TrustProofOfAddressCreateResponse

Response from creating a proof of address transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID from Fireblocks (UUID format) | 
**status** | [**TypedMessageTransactionStatusEnum**](TypedMessageTransactionStatusEnum.md) |  | 

## Example

```python
from fireblocks.models.trust_proof_of_address_create_response import TrustProofOfAddressCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrustProofOfAddressCreateResponse from a JSON string
trust_proof_of_address_create_response_instance = TrustProofOfAddressCreateResponse.from_json(json)
# print the JSON string representation of the object
print(TrustProofOfAddressCreateResponse.to_json())

# convert the object into a dict
trust_proof_of_address_create_response_dict = trust_proof_of_address_create_response_instance.to_dict()
# create an instance of TrustProofOfAddressCreateResponse from a dict
trust_proof_of_address_create_response_from_dict = TrustProofOfAddressCreateResponse.from_dict(trust_proof_of_address_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AddressRegistryVerifyProofOfOwnershipResponse

Online verification result. Authenticated calls always return HTTP 200 with this body (`valid: true` or `valid: false`); unknown/expired exports do not use 404.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the stored export matches the supplied verification hash and address within retention. | 
**expires_at** | **str** | Inclusive last UTC calendar day (&#x60;YYYY-MM-DD&#x60;) when &#x60;valid&#x60; is true; empty string when &#x60;valid&#x60; is false. | 

## Example

```python
from fireblocks.models.address_registry_verify_proof_of_ownership_response import AddressRegistryVerifyProofOfOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryVerifyProofOfOwnershipResponse from a JSON string
address_registry_verify_proof_of_ownership_response_instance = AddressRegistryVerifyProofOfOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryVerifyProofOfOwnershipResponse.to_json())

# convert the object into a dict
address_registry_verify_proof_of_ownership_response_dict = address_registry_verify_proof_of_ownership_response_instance.to_dict()
# create an instance of AddressRegistryVerifyProofOfOwnershipResponse from a dict
address_registry_verify_proof_of_ownership_response_from_dict = AddressRegistryVerifyProofOfOwnershipResponse.from_dict(address_registry_verify_proof_of_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



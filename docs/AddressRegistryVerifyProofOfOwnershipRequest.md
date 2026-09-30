# AddressRegistryVerifyProofOfOwnershipRequest

Request body for verifying an Address Registry Proof of Ownership export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_id** | **str** | Export id from create / the PDF. | 
**verification_hash** | **str** | Verification hash from create / the PDF (exact match required). | 
**address** | **str** | Address from the PDF (exact UTF-8 match to the stored export). | 
**expires_at** | **str** | Optional but recommended: the PDF&#39;s \&quot;Online verification available until\&quot; date (&#x60;YYYY-MM-DD&#x60;), which speeds up the lookup. A wrong value yields &#x60;valid: false&#x60; even if the export exists — copy it exactly from the PDF, or omit it. | [optional] 

## Example

```python
from fireblocks.models.address_registry_verify_proof_of_ownership_request import AddressRegistryVerifyProofOfOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryVerifyProofOfOwnershipRequest from a JSON string
address_registry_verify_proof_of_ownership_request_instance = AddressRegistryVerifyProofOfOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryVerifyProofOfOwnershipRequest.to_json())

# convert the object into a dict
address_registry_verify_proof_of_ownership_request_dict = address_registry_verify_proof_of_ownership_request_instance.to_dict()
# create an instance of AddressRegistryVerifyProofOfOwnershipRequest from a dict
address_registry_verify_proof_of_ownership_request_from_dict = AddressRegistryVerifyProofOfOwnershipRequest.from_dict(address_registry_verify_proof_of_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



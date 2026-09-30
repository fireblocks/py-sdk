# AddressRegistryCreateProofOfOwnershipResponse

Address Registry Proof of Ownership PDF export, created successfully.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdf** | **bytearray** | Base64-encoded Proof of Ownership PDF bytes. Fireblocks does not store the PDF: save it immediately, there is no re-download route. | 
**export_id** | **str** | Stable id of the online-verifiable export record. | 
**verification_hash** | **str** | Verification hash bound to the export (also printed on the PDF). | 
**expires_at** | **str** | Inclusive last UTC calendar day online verification is available (&#x60;YYYY-MM-DD&#x60;). | 

## Example

```python
from fireblocks.models.address_registry_create_proof_of_ownership_response import AddressRegistryCreateProofOfOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryCreateProofOfOwnershipResponse from a JSON string
address_registry_create_proof_of_ownership_response_instance = AddressRegistryCreateProofOfOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryCreateProofOfOwnershipResponse.to_json())

# convert the object into a dict
address_registry_create_proof_of_ownership_response_dict = address_registry_create_proof_of_ownership_response_instance.to_dict()
# create an instance of AddressRegistryCreateProofOfOwnershipResponse from a dict
address_registry_create_proof_of_ownership_response_from_dict = AddressRegistryCreateProofOfOwnershipResponse.from_dict(address_registry_create_proof_of_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



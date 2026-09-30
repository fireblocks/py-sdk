# AddressRegistryCreateProofOfOwnershipRequest

Request body for creating an Address Registry Proof of Ownership PDF export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Blockchain address to prove ownership for (must resolve to the caller&#39;s workspace). Same format expectations as the &#x60;address&#x60; path parameter on &#x60;GET /v1/address_registry/legal_entities/{address}&#x60;. | 

## Example

```python
from fireblocks.models.address_registry_create_proof_of_ownership_request import AddressRegistryCreateProofOfOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegistryCreateProofOfOwnershipRequest from a JSON string
address_registry_create_proof_of_ownership_request_instance = AddressRegistryCreateProofOfOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(AddressRegistryCreateProofOfOwnershipRequest.to_json())

# convert the object into a dict
address_registry_create_proof_of_ownership_request_dict = address_registry_create_proof_of_ownership_request_instance.to_dict()
# create an instance of AddressRegistryCreateProofOfOwnershipRequest from a dict
address_registry_create_proof_of_ownership_request_from_dict = AddressRegistryCreateProofOfOwnershipRequest.from_dict(address_registry_create_proof_of_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



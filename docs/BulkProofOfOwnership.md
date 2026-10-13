# BulkProofOfOwnership

Proof that the customer holds the private key. Required for every key, unlike the single key endpoint: bulk registration has no interactive step in which a proof can arrive later.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message to be signed by the key as proof of ownership. 64 to 1024 bytes in hexadecimal format. | 
**signature** | **str** | The signature of the message. 64 bytes in hexadecimal format. | 

## Example

```python
from fireblocks.models.bulk_proof_of_ownership import BulkProofOfOwnership

# TODO update the JSON string below
json = "{}"
# create an instance of BulkProofOfOwnership from a JSON string
bulk_proof_of_ownership_instance = BulkProofOfOwnership.from_json(json)
# print the JSON string representation of the object
print(BulkProofOfOwnership.to_json())

# convert the object into a dict
bulk_proof_of_ownership_dict = bulk_proof_of_ownership_instance.to_dict()
# create an instance of BulkProofOfOwnership from a dict
bulk_proof_of_ownership_from_dict = BulkProofOfOwnership.from_dict(bulk_proof_of_ownership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



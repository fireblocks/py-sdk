# BulkSigningKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_device_key_id** | **str** | The ID, name or label of the key specified on the customer&#39;s signing device. | 
**signed_cert_pem** | **str** | The signed certificate that includes the public key PEM of the signing key, signed by the validation key declared for the request. | 
**agent_user_id** | **str** | Id of user to which this key belongs | 
**proof_of_ownership** | [**BulkProofOfOwnership**](BulkProofOfOwnership.md) |  | 

## Example

```python
from fireblocks.models.bulk_signing_key import BulkSigningKey

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSigningKey from a JSON string
bulk_signing_key_instance = BulkSigningKey.from_json(json)
# print the JSON string representation of the object
print(BulkSigningKey.to_json())

# convert the object into a dict
bulk_signing_key_dict = bulk_signing_key_instance.to_dict()
# create an instance of BulkSigningKey from a dict
bulk_signing_key_from_dict = BulkSigningKey.from_dict(bulk_signing_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



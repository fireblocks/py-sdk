# ApprovalApiPublicKey

The public key material and its signing algorithm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The signature algorithm of the public key. | 
**public_key_pem** | **str** | The PEM-encoded public key. | 

## Example

```python
from fireblocks.models.approval_api_public_key import ApprovalApiPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalApiPublicKey from a JSON string
approval_api_public_key_instance = ApprovalApiPublicKey.from_json(json)
# print the JSON string representation of the object
print(ApprovalApiPublicKey.to_json())

# convert the object into a dict
approval_api_public_key_dict = approval_api_public_key_instance.to_dict()
# create an instance of ApprovalApiPublicKey from a dict
approval_api_public_key_from_dict = ApprovalApiPublicKey.from_dict(approval_api_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



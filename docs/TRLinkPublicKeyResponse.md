# TRLinkPublicKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Partner issuer identifier | 
**public_key** | [**TRLinkJwkPublicKey**](TRLinkJwkPublicKey.md) |  | 

## Example

```python
from fireblocks.models.tr_link_public_key_response import TRLinkPublicKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkPublicKeyResponse from a JSON string
tr_link_public_key_response_instance = TRLinkPublicKeyResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkPublicKeyResponse.to_json())

# convert the object into a dict
tr_link_public_key_response_dict = tr_link_public_key_response_instance.to_dict()
# create an instance of TRLinkPublicKeyResponse from a dict
tr_link_public_key_response_from_dict = TRLinkPublicKeyResponse.from_dict(tr_link_public_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



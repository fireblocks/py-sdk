# SignedMessageSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_sig** | **str** |  | [optional] 
**r** | **str** |  | [optional] 
**s** | **str** |  | [optional] 
**v** | **float** |  | [optional] 

## Example

```python
from fireblocks.models.signed_message_signature import SignedMessageSignature

# TODO update the JSON string below
json = "{}"
# create an instance of SignedMessageSignature from a JSON string
signed_message_signature_instance = SignedMessageSignature.from_json(json)
# print the JSON string representation of the object
print(SignedMessageSignature.to_json())

# convert the object into a dict
signed_message_signature_dict = signed_message_signature_instance.to_dict()
# create an instance of SignedMessageSignature from a dict
signed_message_signature_from_dict = SignedMessageSignature.from_dict(signed_message_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



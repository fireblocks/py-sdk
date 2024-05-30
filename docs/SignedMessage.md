# SignedMessage

A list of signed messages returned for raw signing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**algorithm** | **str** |  | [optional] 
**derivation_path** | **List[float]** |  | [optional] 
**signature** | [**SignedMessageSignature**](SignedMessageSignature.md) |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.signed_message import SignedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SignedMessage from a JSON string
signed_message_instance = SignedMessage.from_json(json)
# print the JSON string representation of the object
print(SignedMessage.to_json())

# convert the object into a dict
signed_message_dict = signed_message_instance.to_dict()
# create an instance of SignedMessage from a dict
signed_message_from_dict = SignedMessage.from_dict(signed_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



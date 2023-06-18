# UnsignedMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**bip44address_index** | **int** |  | [optional] 
**bip44change** | **float** |  | [optional] 
**derivation_path** | **List[float]** |  | [optional] 

## Example

```python
from fireblocks_client.models.unsigned_message import UnsignedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UnsignedMessage from a JSON string
unsigned_message_instance = UnsignedMessage.from_json(json)
# print the JSON string representation of the object
print UnsignedMessage.to_json()

# convert the object into a dict
unsigned_message_dict = unsigned_message_instance.to_dict()
# create an instance of UnsignedMessage from a dict
unsigned_message_form_dict = unsigned_message.from_dict(unsigned_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



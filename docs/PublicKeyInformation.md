# PublicKeyInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Elliptic Curve | [optional] 
**derivation_path** | **List[int]** | BIP44 derivation path | [optional] 
**public_key** | **str** | Compressed/Uncompressed public key value in hex representation | [optional] 

## Example

```python
from fireblocks.models.public_key_information import PublicKeyInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKeyInformation from a JSON string
public_key_information_instance = PublicKeyInformation.from_json(json)
# print the JSON string representation of the object
print(PublicKeyInformation.to_json())

# convert the object into a dict
public_key_information_dict = public_key_information_instance.to_dict()
# create an instance of PublicKeyInformation from a dict
public_key_information_from_dict = PublicKeyInformation.from_dict(public_key_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



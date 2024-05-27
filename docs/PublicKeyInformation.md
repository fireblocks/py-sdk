# PublicKeyInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | [optional] 
**derivation_path** | **List[float]** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.public_key_information import PublicKeyInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKeyInformation from a JSON string
public_key_information_instance = PublicKeyInformation.from_json(json)
# print the JSON string representation of the object
print PublicKeyInformation.to_json()

# convert the object into a dict
public_key_information_dict = public_key_information_instance.to_dict()
# create an instance of PublicKeyInformation from a dict
public_key_information_form_dict = public_key_information.from_dict(public_key_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



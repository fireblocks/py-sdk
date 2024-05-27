# OneTimeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**tag** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.one_time_address import OneTimeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OneTimeAddress from a JSON string
one_time_address_instance = OneTimeAddress.from_json(json)
# print the JSON string representation of the object
print OneTimeAddress.to_json()

# convert the object into a dict
one_time_address_dict = one_time_address_instance.to_dict()
# create an instance of OneTimeAddress from a dict
one_time_address_form_dict = one_time_address.from_dict(one_time_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



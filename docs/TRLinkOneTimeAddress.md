# TRLinkOneTimeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Blockchain address | 
**tag** | **str** | Destination tag (memo, memo ID, etc.) | [optional] 

## Example

```python
from fireblocks.models.tr_link_one_time_address import TRLinkOneTimeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkOneTimeAddress from a JSON string
tr_link_one_time_address_instance = TRLinkOneTimeAddress.from_json(json)
# print the JSON string representation of the object
print(TRLinkOneTimeAddress.to_json())

# convert the object into a dict
tr_link_one_time_address_dict = tr_link_one_time_address_instance.to_dict()
# create an instance of TRLinkOneTimeAddress from a dict
tr_link_one_time_address_from_dict = TRLinkOneTimeAddress.from_dict(tr_link_one_time_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



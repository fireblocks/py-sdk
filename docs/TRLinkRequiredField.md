# TRLinkRequiredField

An IVMS101 field requirement with its type and path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The person type for this field | 
**path** | **str** | IVMS101 field path | 

## Example

```python
from fireblocks.models.tr_link_required_field import TRLinkRequiredField

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkRequiredField from a JSON string
tr_link_required_field_instance = TRLinkRequiredField.from_json(json)
# print the JSON string representation of the object
print(TRLinkRequiredField.to_json())

# convert the object into a dict
tr_link_required_field_dict = tr_link_required_field_instance.to_dict()
# create an instance of TRLinkRequiredField from a dict
tr_link_required_field_from_dict = TRLinkRequiredField.from_dict(tr_link_required_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



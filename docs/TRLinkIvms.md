# TRLinkIvms

IVMS101 data structure containing encrypted PII

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | IVMS version | 
**data** | **str** | Encrypted IVMS101 data containing originator and beneficiary information | 
**filled_fields** | **List[str]** | List of fields that are filled in the IVMS data | 

## Example

```python
from fireblocks.models.tr_link_ivms import TRLinkIvms

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkIvms from a JSON string
tr_link_ivms_instance = TRLinkIvms.from_json(json)
# print the JSON string representation of the object
print(TRLinkIvms.to_json())

# convert the object into a dict
tr_link_ivms_dict = tr_link_ivms_instance.to_dict()
# create an instance of TRLinkIvms from a dict
tr_link_ivms_from_dict = TRLinkIvms.from_dict(tr_link_ivms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



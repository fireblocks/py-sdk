# TRLinkIvmsResponse

IVMS101 data in response format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | IVMS101 version | 
**data** | **str** | Base64 encoded IVMS101 data containing originator and beneficiary information | 
**filled_fields** | **List[str]** | List of fields that are filled in the IVMS101 data | 

## Example

```python
from fireblocks.models.tr_link_ivms_response import TRLinkIvmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkIvmsResponse from a JSON string
tr_link_ivms_response_instance = TRLinkIvmsResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkIvmsResponse.to_json())

# convert the object into a dict
tr_link_ivms_response_dict = tr_link_ivms_response_instance.to_dict()
# create an instance of TRLinkIvmsResponse from a dict
tr_link_ivms_response_from_dict = TRLinkIvmsResponse.from_dict(tr_link_ivms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



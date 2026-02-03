# TRLinkCancelTrmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for cancellation | [optional] 
**cancelled_by** | **str** | User ID who cancelled the TRM | [optional] 

## Example

```python
from fireblocks.models.tr_link_cancel_trm_request import TRLinkCancelTrmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkCancelTrmRequest from a JSON string
tr_link_cancel_trm_request_instance = TRLinkCancelTrmRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkCancelTrmRequest.to_json())

# convert the object into a dict
tr_link_cancel_trm_request_dict = tr_link_cancel_trm_request_instance.to_dict()
# create an instance of TRLinkCancelTrmRequest from a dict
tr_link_cancel_trm_request_from_dict = TRLinkCancelTrmRequest.from_dict(tr_link_cancel_trm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



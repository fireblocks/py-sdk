# TRLinkRedirectTrmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subsidiary_vasp_id** | **str** | ID of the subsidiary VASP to redirect the TRM to | 

## Example

```python
from fireblocks.models.tr_link_redirect_trm_request import TRLinkRedirectTrmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkRedirectTrmRequest from a JSON string
tr_link_redirect_trm_request_instance = TRLinkRedirectTrmRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkRedirectTrmRequest.to_json())

# convert the object into a dict
tr_link_redirect_trm_request_dict = tr_link_redirect_trm_request_instance.to_dict()
# create an instance of TRLinkRedirectTrmRequest from a dict
tr_link_redirect_trm_request_from_dict = TRLinkRedirectTrmRequest.from_dict(tr_link_redirect_trm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TRLinkConnectIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key provided by the Travel Rule partner | 
**secret** | **str** | Secret/password provided by the Travel Rule partner (optional) | [optional] 

## Example

```python
from fireblocks.models.tr_link_connect_integration_request import TRLinkConnectIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkConnectIntegrationRequest from a JSON string
tr_link_connect_integration_request_instance = TRLinkConnectIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkConnectIntegrationRequest.to_json())

# convert the object into a dict
tr_link_connect_integration_request_dict = tr_link_connect_integration_request_instance.to_dict()
# create an instance of TRLinkConnectIntegrationRequest from a dict
tr_link_connect_integration_request_from_dict = TRLinkConnectIntegrationRequest.from_dict(tr_link_connect_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



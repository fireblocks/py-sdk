# TRLinkCreateIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer unique identifier | 
**partner_ident** | **str** | Partner identification code (e.g., \&quot;sumsub\&quot;, \&quot;notabene\&quot;) | 
**customer_integration_id** | **str** | Optional. When supplied and permitted for the tenant (feature flag / CSM arrangement), this value is used as the TRLink integration identifier instead of a server-generated UUID. If omitted, the API generates a UUID. If supplied when the tenant is not permitted to set a custom id, the request fails with 400. Contact your CSM if you need a custom integration id. | [optional] 

## Example

```python
from fireblocks.models.tr_link_create_integration_request import TRLinkCreateIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkCreateIntegrationRequest from a JSON string
tr_link_create_integration_request_instance = TRLinkCreateIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkCreateIntegrationRequest.to_json())

# convert the object into a dict
tr_link_create_integration_request_dict = tr_link_create_integration_request_instance.to_dict()
# create an instance of TRLinkCreateIntegrationRequest from a dict
tr_link_create_integration_request_from_dict = TRLinkCreateIntegrationRequest.from_dict(tr_link_create_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



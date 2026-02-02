# TRLinkCustomerIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_integration_id** | **str** | Customer integration unique identifier | 
**api_key** | **str** | API key for partner integration (censored for security) | [optional] 
**secret** | **str** | Secret for partner integration (censored for security) | [optional] 
**create_date** | **datetime** | Timestamp when the integration was created (ISO 8601 format) | 
**last_update** | **datetime** | Timestamp when the integration was last updated (ISO 8601 format) | 
**partner** | [**TRLinkPartnerResponse**](TRLinkPartnerResponse.md) |  | 
**customer** | [**TRLinkCustomerResponse**](TRLinkCustomerResponse.md) |  | 

## Example

```python
from fireblocks.models.tr_link_customer_integration_response import TRLinkCustomerIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkCustomerIntegrationResponse from a JSON string
tr_link_customer_integration_response_instance = TRLinkCustomerIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkCustomerIntegrationResponse.to_json())

# convert the object into a dict
tr_link_customer_integration_response_dict = tr_link_customer_integration_response_instance.to_dict()
# create an instance of TRLinkCustomerIntegrationResponse from a dict
tr_link_customer_integration_response_from_dict = TRLinkCustomerIntegrationResponse.from_dict(tr_link_customer_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



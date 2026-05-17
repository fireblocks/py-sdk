# TRLinkCustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer unique identifier | 
**discoverable** | [**TRLinkDiscoverableStatus**](TRLinkDiscoverableStatus.md) |  | 
**short_name** | **str** | Short display name | 
**full_legal_name** | **str** | Full legal entity name | 
**geographic_address** | [**TRLinkGeographicAddressRequest**](TRLinkGeographicAddressRequest.md) |  | [optional] 
**country_of_registration** | **str** | ISO 3166-1 alpha-2 country code where the entity is registered | 
**national_identification** | **str** | National identification, returned exactly as stored: a compact, whitespace-free JSON-encoded string with these optional keys (in this order): &#x60;nationalIdentifier&#x60;, &#x60;nationalIdentifierType&#x60; (e.g. &#x60;LEIX&#x60; for an LEI), &#x60;countryOfIssue&#x60; (ISO 3166-1 alpha-2), &#x60;registrationAuthority&#x60;. Maximum length is 240 characters. | [optional] 
**date_of_incorporation** | **date** | Date of entity incorporation (ISO 8601 format) | [optional] 
**vaults** | **List[int]** | Associated Fireblocks vault account IDs | [optional] 
**tr_primary_purpose** | **str** | Primary Travel Rule role for this customer; determines how the customer&#39;s Travel Rule messages are routed. Valid values: &#x60;notabene&#x60;, &#x60;trlink&#x60;. | 
**create_date** | **datetime** | Timestamp when the customer was created (ISO 8601 format) | 
**last_update** | **datetime** | Timestamp when the customer was last updated (ISO 8601 format) | 

## Example

```python
from fireblocks.models.tr_link_customer_response import TRLinkCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkCustomerResponse from a JSON string
tr_link_customer_response_instance = TRLinkCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkCustomerResponse.to_json())

# convert the object into a dict
tr_link_customer_response_dict = tr_link_customer_response_instance.to_dict()
# create an instance of TRLinkCustomerResponse from a dict
tr_link_customer_response_from_dict = TRLinkCustomerResponse.from_dict(tr_link_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



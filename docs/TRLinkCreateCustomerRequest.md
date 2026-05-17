# TRLinkCreateCustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discoverable** | [**TRLinkDiscoverableStatus**](TRLinkDiscoverableStatus.md) |  | [optional] 
**short_name** | **str** | Short display name (required) | 
**full_legal_name** | **str** | Full legal entity name | [optional] 
**geographic_address** | [**TRLinkGeographicAddressRequest**](TRLinkGeographicAddressRequest.md) |  | [optional] 
**country_of_registration** | **str** | ISO 3166-1 alpha-2 country code where the entity is registered | [optional] 
**national_identification** | **str** | National identification, sent as a JSON-encoded string. The server normalizes input into a compact JSON with these optional keys: &#x60;nationalIdentifier&#x60;, &#x60;nationalIdentifierType&#x60; (e.g. &#x60;LEIX&#x60; for an LEI), &#x60;countryOfIssue&#x60; (ISO 3166-1 alpha-2), &#x60;registrationAuthority&#x60;. If the input is not a JSON object, it is wrapped as &#x60;{\&quot;nationalIdentifier\&quot;:\&quot;&lt;value&gt;\&quot;}&#x60;; if the value matches the LEI format, &#x60;nationalIdentifierType&#x60; is set to &#x60;LEIX&#x60; automatically and &#x60;countryOfIssue&#x60; defaults to this request&#39;s &#x60;countryOfRegistration&#x60; if not provided. The compacted JSON must be 240 characters or fewer. On read, the value is returned exactly as stored. | [optional] 
**date_of_incorporation** | **date** | Date of entity incorporation (ISO 8601 format: YYYY-MM-DD) | [optional] 
**vaults** | **List[int]** | Associated Fireblocks vault account IDs | [optional] 
**tr_primary_purpose** | **str** | Primary Travel Rule role for this customer; determines how the customer&#39;s Travel Rule messages are routed. Valid values: &#x60;notabene&#x60;, &#x60;trlink&#x60;. | [optional] [default to 'trlink']

## Example

```python
from fireblocks.models.tr_link_create_customer_request import TRLinkCreateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkCreateCustomerRequest from a JSON string
tr_link_create_customer_request_instance = TRLinkCreateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkCreateCustomerRequest.to_json())

# convert the object into a dict
tr_link_create_customer_request_dict = tr_link_create_customer_request_instance.to_dict()
# create an instance of TRLinkCreateCustomerRequest from a dict
tr_link_create_customer_request_from_dict = TRLinkCreateCustomerRequest.from_dict(tr_link_create_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



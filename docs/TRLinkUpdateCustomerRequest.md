# TRLinkUpdateCustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discoverable** | [**TRLinkDiscoverableStatus**](TRLinkDiscoverableStatus.md) |  | [optional] 
**short_name** | **str** | Short display name | [optional] 
**full_legal_name** | **str** | Full legal entity name | [optional] 
**geographic_address** | [**TRLinkGeographicAddressRequest**](TRLinkGeographicAddressRequest.md) |  | [optional] 
**country_of_registration** | **str** | ISO 3166-1 alpha-2 country code where the entity is registered | [optional] 
**national_identification** | **str** | National identification as JSON string | [optional] 
**date_of_incorporation** | **date** | Date of entity incorporation (ISO 8601 format: YYYY-MM-DD) | [optional] 
**vaults** | **List[int]** | Associated Fireblocks vault account IDs | [optional] 
**tr_primary_purpose** | **str** | Primary purpose for Travel Rule compliance | [optional] 

## Example

```python
from fireblocks.models.tr_link_update_customer_request import TRLinkUpdateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkUpdateCustomerRequest from a JSON string
tr_link_update_customer_request_instance = TRLinkUpdateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkUpdateCustomerRequest.to_json())

# convert the object into a dict
tr_link_update_customer_request_dict = tr_link_update_customer_request_instance.to_dict()
# create an instance of TRLinkUpdateCustomerRequest from a dict
tr_link_update_customer_request_from_dict = TRLinkUpdateCustomerRequest.from_dict(tr_link_update_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



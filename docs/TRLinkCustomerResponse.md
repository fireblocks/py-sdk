# TRLinkCustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer unique identifier | 
**tenant_id** | **str** | Fireblocks tenant ID | 
**discoverable** | [**TRLinkDiscoverableStatus**](TRLinkDiscoverableStatus.md) |  | 
**short_name** | **str** | Short display name | 
**full_legal_name** | **str** | Full legal entity name | 
**geographic_address** | [**TRLinkGeographicAddressRequest**](TRLinkGeographicAddressRequest.md) |  | [optional] 
**country_of_registration** | **str** | ISO 3166-1 alpha-2 country code where the entity is registered | 
**national_identification** | **str** | National identification (serialized as string) | [optional] 
**date_of_incorporation** | **date** | Date of entity incorporation (ISO 8601 format) | [optional] 
**vaults** | **List[int]** | Associated Fireblocks vault account IDs | [optional] 
**tr_primary_purpose** | **str** | Primary purpose for Travel Rule compliance | [optional] 
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



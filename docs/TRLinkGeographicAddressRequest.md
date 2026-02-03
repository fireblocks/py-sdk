# TRLinkGeographicAddressRequest

Geographic address following IVMS101 standard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line** | **List[str]** | Address lines (max 3, each up to 70 characters) | [optional] 
**street_name** | **str** | Street name (required if buildingNumber is provided) | [optional] 
**building_number** | **str** | Building number | [optional] 
**floor** | **str** | Floor number | [optional] 
**post_box** | **str** | Post box number | [optional] 
**post_code** | **str** | Postal code (required if townName is provided) | [optional] 
**town_name** | **str** | City or town name (required if postCode is provided) | [optional] 
**district_name** | **str** | District name | [optional] 
**country_sub_division** | **str** | State or province (validated against country) | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country code (required if town, district, or sub-division provided) | [optional] 

## Example

```python
from fireblocks.models.tr_link_geographic_address_request import TRLinkGeographicAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkGeographicAddressRequest from a JSON string
tr_link_geographic_address_request_instance = TRLinkGeographicAddressRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkGeographicAddressRequest.to_json())

# convert the object into a dict
tr_link_geographic_address_request_dict = tr_link_geographic_address_request_instance.to_dict()
# create an instance of TRLinkGeographicAddressRequest from a dict
tr_link_geographic_address_request_from_dict = TRLinkGeographicAddressRequest.from_dict(tr_link_geographic_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



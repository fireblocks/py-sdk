# TravelRuleValidateGeographicAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | Name of a street or thoroughfare | [optional] 
**town_name** | **str** | Name of a built-up area, with defined boundaries, and a local government | [optional] 
**country** | **str** | Nation with its own government (ISO-3166 Alpha-2 country code) | [optional] 
**building_number** | **str** | Number that identifies the position of a building on a street | [optional] 
**post_code** | **str** | Identifier consisting of a group of letters and/or numbers added to a postal address to assist the sorting of mail | [optional] 
**address_type** | **str** | Specifies the type of address. Acceptable values are: - &#39;HOME&#39;: Residential, the home address - &#39;BIZZ&#39;: Business, the business address - &#39;GEOG&#39;: Geographic, an unspecified physical (geographical) address | [optional] 
**department** | **str** | Identification of a division of a large organisation or building | [optional] 
**sub_department** | **str** | Identification of a sub-division of a large organisation or building | [optional] 
**building_name** | **str** | Name of the building or house | [optional] 
**floor** | **str** | Floor or storey within a building | [optional] 
**post_box** | **str** | Numbered box in a post office | [optional] 
**room** | **str** | Building room number | [optional] 
**town_location_name** | **str** | Specific location name within the town | [optional] 
**district_name** | **str** | Identifies a subdivision within a country subdivision | [optional] 
**country_sub_division** | **str** | Identifies a subdivision of a country such as state, region, or province | [optional] 
**address_line** | **List[str]** | Information that locates and identifies a specific address, presented in free format text | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_geographic_address import TravelRuleValidateGeographicAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateGeographicAddress from a JSON string
travel_rule_validate_geographic_address_instance = TravelRuleValidateGeographicAddress.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateGeographicAddress.to_json())

# convert the object into a dict
travel_rule_validate_geographic_address_dict = travel_rule_validate_geographic_address_instance.to_dict()
# create an instance of TravelRuleValidateGeographicAddress from a dict
travel_rule_validate_geographic_address_from_dict = TravelRuleValidateGeographicAddress.from_dict(travel_rule_validate_geographic_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



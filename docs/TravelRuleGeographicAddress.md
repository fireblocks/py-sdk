# TravelRuleGeographicAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | Name of a street or thoroughfare. The value must be encrypted. | [optional] 
**town_name** | **str** | Name of a built-up area, with defined boundaries, and a local government. The value must be encrypted. | [optional] 
**country** | **str** | Nation with its own government (ISO-3166 Alpha-2 country code). The value must be encrypted. | [optional] 
**building_number** | **str** | Number that identifies the position of a building on a street. The value must be encrypted. | [optional] 
**post_code** | **str** | Identifier consisting of a group of letters and/or numbers added to a postal address to assist the sorting of mail. The value must be encrypted. | [optional] 
**address_type** | **str** | Specifies the type of address. Acceptable values are: - &#39;HOME&#39;: Residential, the home address - &#39;BIZZ&#39;: Business, the business address - &#39;GEOG&#39;: Geographic, an unspecified physical (geographical) address The value must be encrypted. | [optional] 
**department** | **str** | Identification of a division of a large organisation or building. The value must be encrypted. | [optional] 
**sub_department** | **str** | Identification of a sub-division of a large organisation or building. The value must be encrypted. | [optional] 
**building_name** | **str** | Name of the building or house. The value must be encrypted. | [optional] 
**floor** | **str** | Floor or storey within a building. The value must be encrypted. | [optional] 
**post_box** | **str** | Numbered box in a post office. The value must be encrypted. | [optional] 
**room** | **str** | Building room number. The value must be encrypted. | [optional] 
**town_location_name** | **str** | Specific location name within the town. The value must be encrypted. | [optional] 
**district_name** | **str** | Identifies a subdivision within a country subdivision. The value must be encrypted. | [optional] 
**country_sub_division** | **str** | Identifies a subdivision of a country such as state, region, or province. The value must be encrypted. | [optional] 
**address_line** | **List[str]** | Information that locates and identifies a specific address, presented in free format text. Each item must be encrypted. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_geographic_address import TravelRuleGeographicAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleGeographicAddress from a JSON string
travel_rule_geographic_address_instance = TravelRuleGeographicAddress.from_json(json)
# print the JSON string representation of the object
print(TravelRuleGeographicAddress.to_json())

# convert the object into a dict
travel_rule_geographic_address_dict = travel_rule_geographic_address_instance.to_dict()
# create an instance of TravelRuleGeographicAddress from a dict
travel_rule_geographic_address_from_dict = TravelRuleGeographicAddress.from_dict(travel_rule_geographic_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



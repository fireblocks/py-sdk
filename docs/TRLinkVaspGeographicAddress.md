# TRLinkVaspGeographicAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted_address** | **str** | Complete formatted address | [optional] 
**country** | **str** | Country code or name | [optional] 
**street_name** | **str** | Street name | [optional] 
**building_number** | **str** | Building number | [optional] 
**city** | **str** | City name | [optional] 
**postal_code** | **str** | Postal/ZIP code | [optional] 

## Example

```python
from fireblocks.models.tr_link_vasp_geographic_address import TRLinkVaspGeographicAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkVaspGeographicAddress from a JSON string
tr_link_vasp_geographic_address_instance = TRLinkVaspGeographicAddress.from_json(json)
# print the JSON string representation of the object
print(TRLinkVaspGeographicAddress.to_json())

# convert the object into a dict
tr_link_vasp_geographic_address_dict = tr_link_vasp_geographic_address_instance.to_dict()
# create an instance of TRLinkVaspGeographicAddress from a dict
tr_link_vasp_geographic_address_from_dict = TRLinkVaspGeographicAddress.from_dict(tr_link_vasp_geographic_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



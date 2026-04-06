# GleifData

GLEIF (Global Legal Entity Identifier Foundation) data for a legal entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lei** | **str** | Legal Entity Identifier (LEI) code | 
**legal_name** | **str** | Official legal name of the entity | 
**other_names** | **List[str]** | Alternative names for the entity | [optional] 
**legal_address_region** | **str** | Region or state of the legal address | [optional] 
**legal_address_country** | **str** | Country code of the legal address (ISO 3166-1 alpha-2) | 
**next_renewal_date** | **datetime** | Date when the LEI registration must be renewed | [optional] 

## Example

```python
from fireblocks.models.gleif_data import GleifData

# TODO update the JSON string below
json = "{}"
# create an instance of GleifData from a JSON string
gleif_data_instance = GleifData.from_json(json)
# print the JSON string representation of the object
print(GleifData.to_json())

# convert the object into a dict
gleif_data_dict = gleif_data_instance.to_dict()
# create an instance of GleifData from a dict
gleif_data_from_dict = GleifData.from_dict(gleif_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



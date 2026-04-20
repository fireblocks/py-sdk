# GleifOtherLegalEntityName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Alternative name of the legal entity | 
**language** | **str** | Two-letter ISO 639-1 language code | 

## Example

```python
from fireblocks.models.gleif_other_legal_entity_name import GleifOtherLegalEntityName

# TODO update the JSON string below
json = "{}"
# create an instance of GleifOtherLegalEntityName from a JSON string
gleif_other_legal_entity_name_instance = GleifOtherLegalEntityName.from_json(json)
# print the JSON string representation of the object
print(GleifOtherLegalEntityName.to_json())

# convert the object into a dict
gleif_other_legal_entity_name_dict = gleif_other_legal_entity_name_instance.to_dict()
# create an instance of GleifOtherLegalEntityName from a dict
gleif_other_legal_entity_name_from_dict = GleifOtherLegalEntityName.from_dict(gleif_other_legal_entity_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



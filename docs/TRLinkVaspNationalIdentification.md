# TRLinkVaspNationalIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | National identification number | 
**type** | **str** | Type of national identification | [optional] 
**authority** | **str** | Issuing authority | [optional] 

## Example

```python
from fireblocks.models.tr_link_vasp_national_identification import TRLinkVaspNationalIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkVaspNationalIdentification from a JSON string
tr_link_vasp_national_identification_instance = TRLinkVaspNationalIdentification.from_json(json)
# print the JSON string representation of the object
print(TRLinkVaspNationalIdentification.to_json())

# convert the object into a dict
tr_link_vasp_national_identification_dict = tr_link_vasp_national_identification_instance.to_dict()
# create an instance of TRLinkVaspNationalIdentification from a dict
tr_link_vasp_national_identification_from_dict = TRLinkVaspNationalIdentification.from_dict(tr_link_vasp_national_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



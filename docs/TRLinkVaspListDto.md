# TRLinkVaspListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | VASP unique identifier (DID format) | 
**name** | **str** | VASP display name | 
**legal_name** | **str** | Legal entity name | [optional] 
**national_identification** | [**TRLinkVaspNationalIdentification**](TRLinkVaspNationalIdentification.md) |  | [optional] 
**geographic_address** | [**TRLinkVaspGeographicAddress**](TRLinkVaspGeographicAddress.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_vasp_list_dto import TRLinkVaspListDto

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkVaspListDto from a JSON string
tr_link_vasp_list_dto_instance = TRLinkVaspListDto.from_json(json)
# print the JSON string representation of the object
print(TRLinkVaspListDto.to_json())

# convert the object into a dict
tr_link_vasp_list_dto_dict = tr_link_vasp_list_dto_instance.to_dict()
# create an instance of TRLinkVaspListDto from a dict
tr_link_vasp_list_dto_from_dict = TRLinkVaspListDto.from_dict(tr_link_vasp_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



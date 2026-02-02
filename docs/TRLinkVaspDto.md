# TRLinkVaspDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | VASP unique identifier (DID format) | 
**name** | **str** | VASP display name | 
**legal_name** | **str** | Legal entity name | [optional] 
**national_identification** | [**TRLinkVaspNationalIdentification**](TRLinkVaspNationalIdentification.md) |  | [optional] 
**geographic_address** | [**TRLinkVaspGeographicAddress**](TRLinkVaspGeographicAddress.md) |  | [optional] 
**public_key** | **str** | VASP public key for encryption | [optional] 

## Example

```python
from fireblocks.models.tr_link_vasp_dto import TRLinkVaspDto

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkVaspDto from a JSON string
tr_link_vasp_dto_instance = TRLinkVaspDto.from_json(json)
# print the JSON string representation of the object
print(TRLinkVaspDto.to_json())

# convert the object into a dict
tr_link_vasp_dto_dict = tr_link_vasp_dto_instance.to_dict()
# create an instance of TRLinkVaspDto from a dict
tr_link_vasp_dto_from_dict = TRLinkVaspDto.from_dict(tr_link_vasp_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VendorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the vendor of this contract template | 
**name** | **str** | The name of the vendor of this contract template | 

## Example

```python
from fireblocks_client.models.vendor_dto import VendorDto

# TODO update the JSON string below
json = "{}"
# create an instance of VendorDto from a JSON string
vendor_dto_instance = VendorDto.from_json(json)
# print the JSON string representation of the object
print VendorDto.to_json()

# convert the object into a dict
vendor_dto_dict = vendor_dto_instance.to_dict()
# create an instance of VendorDto from a dict
vendor_dto_form_dict = vendor_dto.from_dict(vendor_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



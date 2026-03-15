# PixAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**pix_key** | **str** |  | 
**key_type** | **str** |  | 
**bank_name** | **str** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**qr_code** | **str** | The QR code to be used for the transfer | [optional] 
**expiration_date** | **str** | The expiration date of the QR code | [optional] 

## Example

```python
from fireblocks.models.pix_address import PixAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PixAddress from a JSON string
pix_address_instance = PixAddress.from_json(json)
# print the JSON string representation of the object
print(PixAddress.to_json())

# convert the object into a dict
pix_address_dict = pix_address_instance.to_dict()
# create an instance of PixAddress from a dict
pix_address_from_dict = PixAddress.from_dict(pix_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FpsHkAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_legal_name** | **str** | Full legal name of the recipient | [optional] 
**account_number** | **str** | Recipient bank account number | [optional] 
**bank_code** | **str** | Hong Kong bank code | [optional] 
**phone** | **str** | Recipient phone number in E.164 format | [optional] 
**email** | **str** | Recipient email address | [optional] 
**fps_id** | **str** | Hong Kong FPS identifier | [optional] 

## Example

```python
from fireblocks.models.fps_hk_address import FpsHkAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FpsHkAddress from a JSON string
fps_hk_address_instance = FpsHkAddress.from_json(json)
# print the JSON string representation of the object
print(FpsHkAddress.to_json())

# convert the object into a dict
fps_hk_address_dict = fps_hk_address_instance.to_dict()
# create an instance of FpsHkAddress from a dict
fps_hk_address_from_dict = FpsHkAddress.from_dict(fps_hk_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



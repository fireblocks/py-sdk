# InteracAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**recipient_handle** | [**RecipientHandle**](RecipientHandle.md) |  | 
**message** | **str** | The message to be sent to the recipient | [optional] 

## Example

```python
from fireblocks.models.interac_address import InteracAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InteracAddress from a JSON string
interac_address_instance = InteracAddress.from_json(json)
# print the JSON string representation of the object
print(InteracAddress.to_json())

# convert the object into a dict
interac_address_dict = interac_address_instance.to_dict()
# create an instance of InteracAddress from a dict
interac_address_from_dict = InteracAddress.from_dict(interac_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



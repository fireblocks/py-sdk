# InternalTransferAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_account_id** | **str** | The provider&#39;s identifier for the external account. This enables the user to fund the account externally (outside of Fireblocks) if needed. | [optional] 
**account_id** | **str** | The Fireblocks account ID where the user should deposit the funds. | 

## Example

```python
from fireblocks.models.internal_transfer_address import InternalTransferAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferAddress from a JSON string
internal_transfer_address_instance = InternalTransferAddress.from_json(json)
# print the JSON string representation of the object
print(InternalTransferAddress.to_json())

# convert the object into a dict
internal_transfer_address_dict = internal_transfer_address_instance.to_dict()
# create an instance of InternalTransferAddress from a dict
internal_transfer_address_from_dict = InternalTransferAddress.from_dict(internal_transfer_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



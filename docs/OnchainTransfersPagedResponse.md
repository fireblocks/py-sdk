# OnchainTransfersPagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OnchainTransferEvent]**](OnchainTransferEvent.md) | Array of ERC20 transfer events | 
**next** | **str** | Cursor for next page | [optional] 
**prev** | **str** | Cursor for previous page | [optional] 
**total** | **float** | Total count of items | [optional] 

## Example

```python
from fireblocks.models.onchain_transfers_paged_response import OnchainTransfersPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnchainTransfersPagedResponse from a JSON string
onchain_transfers_paged_response_instance = OnchainTransfersPagedResponse.from_json(json)
# print the JSON string representation of the object
print(OnchainTransfersPagedResponse.to_json())

# convert the object into a dict
onchain_transfers_paged_response_dict = onchain_transfers_paged_response_instance.to_dict()
# create an instance of OnchainTransfersPagedResponse from a dict
onchain_transfers_paged_response_from_dict = OnchainTransfersPagedResponse.from_dict(onchain_transfers_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



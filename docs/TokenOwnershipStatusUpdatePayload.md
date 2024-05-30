# TokenOwnershipStatusUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Token&#39;s asset id | 
**status** | **str** | Token&#39;s ownership new status | 

## Example

```python
from fireblocks.models.token_ownership_status_update_payload import TokenOwnershipStatusUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of TokenOwnershipStatusUpdatePayload from a JSON string
token_ownership_status_update_payload_instance = TokenOwnershipStatusUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(TokenOwnershipStatusUpdatePayload.to_json())

# convert the object into a dict
token_ownership_status_update_payload_dict = token_ownership_status_update_payload_instance.to_dict()
# create an instance of TokenOwnershipStatusUpdatePayload from a dict
token_ownership_status_update_payload_from_dict = TokenOwnershipStatusUpdatePayload.from_dict(token_ownership_status_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



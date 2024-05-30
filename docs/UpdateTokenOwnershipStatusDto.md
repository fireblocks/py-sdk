# UpdateTokenOwnershipStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from fireblocks_client.models.update_token_ownership_status_dto import UpdateTokenOwnershipStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTokenOwnershipStatusDto from a JSON string
update_token_ownership_status_dto_instance = UpdateTokenOwnershipStatusDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTokenOwnershipStatusDto.to_json())

# convert the object into a dict
update_token_ownership_status_dto_dict = update_token_ownership_status_dto_instance.to_dict()
# create an instance of UpdateTokenOwnershipStatusDto from a dict
update_token_ownership_status_dto_from_dict = UpdateTokenOwnershipStatusDto.from_dict(update_token_ownership_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



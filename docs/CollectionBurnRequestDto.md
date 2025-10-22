# CollectionBurnRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The id of the vault account that initiates the burn function | 
**token_id** | **str** | The token id | 
**amount** | **str** | For ERC721, amount is optional or should always be 1 and for ERC1155, amount should be 1 or greater | [optional] 
**external_id** | **str** | External id that can be used to identify the transaction in your system. The unique identifier of the transaction outside of Fireblocks with max length of 255 characters | [optional] 

## Example

```python
from fireblocks.models.collection_burn_request_dto import CollectionBurnRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionBurnRequestDto from a JSON string
collection_burn_request_dto_instance = CollectionBurnRequestDto.from_json(json)
# print the JSON string representation of the object
print(CollectionBurnRequestDto.to_json())

# convert the object into a dict
collection_burn_request_dto_dict = collection_burn_request_dto_instance.to_dict()
# create an instance of CollectionBurnRequestDto from a dict
collection_burn_request_dto_from_dict = CollectionBurnRequestDto.from_dict(collection_burn_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



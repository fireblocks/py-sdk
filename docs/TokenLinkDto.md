# TokenLinkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The token link id | 
**status** | **str** | The token status | 
**type** | **str** | The type of token | [optional] 
**ref_id** | **str** | The Fireblocks&#39; reference id | [optional] 
**display_name** | **str** | The token display name. If was not provided, would be taken from the contract template | [optional] 
**token_metadata** | [**TokenLinkDtoTokenMetadata**](TokenLinkDtoTokenMetadata.md) |  | [optional] 

## Example

```python
from fireblocks.models.token_link_dto import TokenLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkDto from a JSON string
token_link_dto_instance = TokenLinkDto.from_json(json)
# print the JSON string representation of the object
print(TokenLinkDto.to_json())

# convert the object into a dict
token_link_dto_dict = token_link_dto_instance.to_dict()
# create an instance of TokenLinkDto from a dict
token_link_dto_from_dict = TokenLinkDto.from_dict(token_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



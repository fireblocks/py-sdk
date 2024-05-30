# TokenLinkRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of token being linked | 
**ref_id** | **str** | The Fireblocks&#39; token link reference id. For example, &#39;BQ5R_BDESC_ABC&#39; if it&#39;s a fungible       asset | 
**display_name** | **str** | The token display name | [optional] 

## Example

```python
from fireblocks.models.token_link_request_dto import TokenLinkRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkRequestDto from a JSON string
token_link_request_dto_instance = TokenLinkRequestDto.from_json(json)
# print the JSON string representation of the object
print(TokenLinkRequestDto.to_json())

# convert the object into a dict
token_link_request_dto_dict = token_link_request_dto_instance.to_dict()
# create an instance of TokenLinkRequestDto from a dict
token_link_request_dto_from_dict = TokenLinkRequestDto.from_dict(token_link_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



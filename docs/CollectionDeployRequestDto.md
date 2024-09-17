# CollectionDeployRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_id** | **str** | The blockchain base assetId | 
**vault_account_id** | **str** | The id of the vault account that initiated the request to issue the token | 
**type** | [**CollectionType**](CollectionType.md) |  | 
**name** | **str** | A string that represents the name of the collection | 
**symbol** | **str** | A string that represents the symbol of the collection | 
**admin_address** | **str** | The EVM address of the user that will be set as the admin user of the collection | 
**display_name** | **str** | A string to display as a name of the collection | [optional] 

## Example

```python
from fireblocks.models.collection_deploy_request_dto import CollectionDeployRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDeployRequestDto from a JSON string
collection_deploy_request_dto_instance = CollectionDeployRequestDto.from_json(json)
# print the JSON string representation of the object
print(CollectionDeployRequestDto.to_json())

# convert the object into a dict
collection_deploy_request_dto_dict = collection_deploy_request_dto_instance.to_dict()
# create an instance of CollectionDeployRequestDto from a dict
collection_deploy_request_dto_from_dict = CollectionDeployRequestDto.from_dict(collection_deploy_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



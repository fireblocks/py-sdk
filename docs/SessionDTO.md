# SessionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the connection | 
**user_id** | **str** | Id of the user that created the connection | 
**session_metadata** | [**SessionMetadata**](SessionMetadata.md) | Metadata of the connection (provided by the dapp) | 
**vault_account_id** | **float** | The vault to connect | 
**fee_level** | **str** | The default fee level | 
**chain_ids** | **List[str]** | The chains approved for the connection | 
**connection_type** | **str** | The connection&#39;s type | 
**connection_method** | **str** | The method through which the connection was established | 
**creation_date** | **datetime** | Timestamp of the session&#39;s creation | 

## Example

```python
from fireblocks_client.models.session_dto import SessionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SessionDTO from a JSON string
session_dto_instance = SessionDTO.from_json(json)
# print the JSON string representation of the object
print SessionDTO.to_json()

# convert the object into a dict
session_dto_dict = session_dto_instance.to_dict()
# create an instance of SessionDTO from a dict
session_dto_form_dict = session_dto.from_dict(session_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



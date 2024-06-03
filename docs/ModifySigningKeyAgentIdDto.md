# ModifySigningKeyAgentIdDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_user_id** | **str** | Id of user that represent agent servers which signs with the key | 

## Example

```python
from fireblocks.models.modify_signing_key_agent_id_dto import ModifySigningKeyAgentIdDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySigningKeyAgentIdDto from a JSON string
modify_signing_key_agent_id_dto_instance = ModifySigningKeyAgentIdDto.from_json(json)
# print the JSON string representation of the object
print(ModifySigningKeyAgentIdDto.to_json())

# convert the object into a dict
modify_signing_key_agent_id_dto_dict = modify_signing_key_agent_id_dto_instance.to_dict()
# create an instance of ModifySigningKeyAgentIdDto from a dict
modify_signing_key_agent_id_dto_from_dict = ModifySigningKeyAgentIdDto.from_dict(modify_signing_key_agent_id_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



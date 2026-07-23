# GetBlockchainByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | [**Blockchain**](Blockchain.md) |  | 

## Example

```python
from fireblocks.models.get_blockchain_by_id_response import GetBlockchainByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockchainByIdResponse from a JSON string
get_blockchain_by_id_response_instance = GetBlockchainByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetBlockchainByIdResponse.to_json())

# convert the object into a dict
get_blockchain_by_id_response_dict = get_blockchain_by_id_response_instance.to_dict()
# create an instance of GetBlockchainByIdResponse from a dict
get_blockchain_by_id_response_from_dict = GetBlockchainByIdResponse.from_dict(get_blockchain_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



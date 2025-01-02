# MpcKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**user_id** | **str** | The user id that owns the key | 
**algorithm** | **float** | The algorithm of the key | 
**players** | [**List[Players]**](Players.md) | The players that are associated with the key | 
**last_preprocessed_index** | **float** | The last index used on this key | [optional] 

## Example

```python
from fireblocks.models.mpc_key import MpcKey

# TODO update the JSON string below
json = "{}"
# create an instance of MpcKey from a JSON string
mpc_key_instance = MpcKey.from_json(json)
# print the JSON string representation of the object
print(MpcKey.to_json())

# convert the object into a dict
mpc_key_dict = mpc_key_instance.to_dict()
# create an instance of MpcKey from a dict
mpc_key_from_dict = MpcKey.from_dict(mpc_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



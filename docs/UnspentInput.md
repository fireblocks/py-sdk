# UnspentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** |  | [optional] 
**index** | **float** |  | [optional] 

## Example

```python
from fireblocks.models.unspent_input import UnspentInput

# TODO update the JSON string below
json = "{}"
# create an instance of UnspentInput from a JSON string
unspent_input_instance = UnspentInput.from_json(json)
# print the JSON string representation of the object
print(UnspentInput.to_json())

# convert the object into a dict
unspent_input_dict = unspent_input_instance.to_dict()
# create an instance of UnspentInput from a dict
unspent_input_from_dict = UnspentInput.from_dict(unspent_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



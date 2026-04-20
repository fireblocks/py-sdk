# Apy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native** | **float** | APY in native format (before fees), as a percentage (e.g. 4.25 means 4.25%, not 0.0425). | [optional] 
**gross** | **float** | Gross APY before fees, as a percentage (e.g. 4.25 means 4.25%, not 0.0425). | [optional] 
**net** | **float** | Net APY after fees, as a percentage (e.g. 4.25 means 4.25%, not 0.0425). | [optional] 

## Example

```python
from fireblocks.models.apy import Apy

# TODO update the JSON string below
json = "{}"
# create an instance of Apy from a JSON string
apy_instance = Apy.from_json(json)
# print the JSON string representation of the object
print(Apy.to_json())

# convert the object into a dict
apy_dict = apy_instance.to_dict()
# create an instance of Apy from a dict
apy_from_dict = Apy.from_dict(apy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



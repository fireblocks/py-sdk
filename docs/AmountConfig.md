# AmountConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**AmountRangeMinMax2**](AmountRangeMinMax2.md) |  | 
**currency** | [**PolicyCurrency**](PolicyCurrency.md) |  | [optional] 

## Example

```python
from fireblocks.models.amount_config import AmountConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AmountConfig from a JSON string
amount_config_instance = AmountConfig.from_json(json)
# print the JSON string representation of the object
print(AmountConfig.to_json())

# convert the object into a dict
amount_config_dict = amount_config_instance.to_dict()
# create an instance of AmountConfig from a dict
amount_config_from_dict = AmountConfig.from_dict(amount_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



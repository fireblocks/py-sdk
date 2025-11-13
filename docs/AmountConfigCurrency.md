# AmountConfigCurrency

Currency property for amount configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**PolicyCurrency**](PolicyCurrency.md) |  | [optional] 

## Example

```python
from fireblocks.models.amount_config_currency import AmountConfigCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of AmountConfigCurrency from a JSON string
amount_config_currency_instance = AmountConfigCurrency.from_json(json)
# print the JSON string representation of the object
print(AmountConfigCurrency.to_json())

# convert the object into a dict
amount_config_currency_dict = amount_config_currency_instance.to_dict()
# create an instance of AmountConfigCurrency from a dict
amount_config_currency_from_dict = AmountConfigCurrency.from_dict(amount_config_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



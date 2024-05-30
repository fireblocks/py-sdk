# GetMaxSpendableAmountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_spendable_amount** | **str** | The maximum amount that can be spent from the vault account | [optional] 

## Example

```python
from fireblocks_client.models.get_max_spendable_amount_response import GetMaxSpendableAmountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMaxSpendableAmountResponse from a JSON string
get_max_spendable_amount_response_instance = GetMaxSpendableAmountResponse.from_json(json)
# print the JSON string representation of the object
print(GetMaxSpendableAmountResponse.to_json())

# convert the object into a dict
get_max_spendable_amount_response_dict = get_max_spendable_amount_response_instance.to_dict()
# create an instance of GetMaxSpendableAmountResponse from a dict
get_max_spendable_amount_response_from_dict = GetMaxSpendableAmountResponse.from_dict(get_max_spendable_amount_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



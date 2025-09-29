# FeePayerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_payer_account_id** | **str** | The account ID of the fee payer | [optional] 

## Example

```python
from fireblocks.models.fee_payer_info import FeePayerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeePayerInfo from a JSON string
fee_payer_info_instance = FeePayerInfo.from_json(json)
# print the JSON string representation of the object
print(FeePayerInfo.to_json())

# convert the object into a dict
fee_payer_info_dict = fee_payer_info_instance.to_dict()
# create an instance of FeePayerInfo from a dict
fee_payer_info_from_dict = FeePayerInfo.from_dict(fee_payer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DisbursementOperationConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_account** | [**Account**](Account.md) |  | [optional] 
**instruction_set** | [**List[DisbursementInstruction]**](DisbursementInstruction.md) |  | 

## Example

```python
from fireblocks_client.models.disbursement_operation_config_params import DisbursementOperationConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementOperationConfigParams from a JSON string
disbursement_operation_config_params_instance = DisbursementOperationConfigParams.from_json(json)
# print the JSON string representation of the object
print(DisbursementOperationConfigParams.to_json())

# convert the object into a dict
disbursement_operation_config_params_dict = disbursement_operation_config_params_instance.to_dict()
# create an instance of DisbursementOperationConfigParams from a dict
disbursement_operation_config_params_from_dict = DisbursementOperationConfigParams.from_dict(disbursement_operation_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TransferValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_validation_failure import TransferValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of TransferValidationFailure from a JSON string
transfer_validation_failure_instance = TransferValidationFailure.from_json(json)
# print the JSON string representation of the object
print(TransferValidationFailure.to_json())

# convert the object into a dict
transfer_validation_failure_dict = transfer_validation_failure_instance.to_dict()
# create an instance of TransferValidationFailure from a dict
transfer_validation_failure_from_dict = TransferValidationFailure.from_dict(transfer_validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



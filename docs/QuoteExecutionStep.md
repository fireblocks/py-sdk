# QuoteExecutionStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExecutionStepType**](ExecutionStepType.md) |  | 
**fee** | [**Fee**](Fee.md) |  | [optional] 

## Example

```python
from fireblocks.models.quote_execution_step import QuoteExecutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteExecutionStep from a JSON string
quote_execution_step_instance = QuoteExecutionStep.from_json(json)
# print the JSON string representation of the object
print(QuoteExecutionStep.to_json())

# convert the object into a dict
quote_execution_step_dict = quote_execution_step_instance.to_dict()
# create an instance of QuoteExecutionStep from a dict
quote_execution_step_from_dict = QuoteExecutionStep.from_dict(quote_execution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



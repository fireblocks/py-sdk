# EstimatedFeeDetails

Optional detailed fee breakdown for high/medium/low estimates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low** | [**FeeBreakdown**](FeeBreakdown.md) |  | [optional] 
**medium** | [**FeeBreakdown**](FeeBreakdown.md) |  | [optional] 
**high** | [**FeeBreakdown**](FeeBreakdown.md) |  | [optional] 

## Example

```python
from fireblocks.models.estimated_fee_details import EstimatedFeeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedFeeDetails from a JSON string
estimated_fee_details_instance = EstimatedFeeDetails.from_json(json)
# print the JSON string representation of the object
print(EstimatedFeeDetails.to_json())

# convert the object into a dict
estimated_fee_details_dict = estimated_fee_details_instance.to_dict()
# create an instance of EstimatedFeeDetails from a dict
estimated_fee_details_from_dict = EstimatedFeeDetails.from_dict(estimated_fee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



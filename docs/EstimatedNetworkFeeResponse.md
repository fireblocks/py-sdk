# EstimatedNetworkFeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low** | [**NetworkFee**](NetworkFee.md) |  | 
**medium** | [**NetworkFee**](NetworkFee.md) |  | 
**high** | [**NetworkFee**](NetworkFee.md) |  | 

## Example

```python
from fireblocks.models.estimated_network_fee_response import EstimatedNetworkFeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedNetworkFeeResponse from a JSON string
estimated_network_fee_response_instance = EstimatedNetworkFeeResponse.from_json(json)
# print the JSON string representation of the object
print(EstimatedNetworkFeeResponse.to_json())

# convert the object into a dict
estimated_network_fee_response_dict = estimated_network_fee_response_instance.to_dict()
# create an instance of EstimatedNetworkFeeResponse from a dict
estimated_network_fee_response_from_dict = EstimatedNetworkFeeResponse.from_dict(estimated_network_fee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



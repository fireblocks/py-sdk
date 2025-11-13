# QuotePropertiesDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | [**AccessType**](AccessType.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 
**quote_asset_id** | **str** |  | 
**base_asset_id** | **str** |  | 
**base_amount** | **str** |  | 
**quote_amount** | **str** |  | 
**price_impact** | **float** |  | [optional] 
**quote_min_amount** | **str** |  | [optional] 
**execution_steps** | [**List[ExecutionStepDetails]**](ExecutionStepDetails.md) |  | [optional] 
**general_fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**side** | **str** | Side of the order | 

## Example

```python
from fireblocks.models.quote_properties_details import QuotePropertiesDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuotePropertiesDetails from a JSON string
quote_properties_details_instance = QuotePropertiesDetails.from_json(json)
# print the JSON string representation of the object
print(QuotePropertiesDetails.to_json())

# convert the object into a dict
quote_properties_details_dict = quote_properties_details_instance.to_dict()
# create an instance of QuotePropertiesDetails from a dict
quote_properties_details_from_dict = QuotePropertiesDetails.from_dict(quote_properties_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



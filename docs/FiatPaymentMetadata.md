# FiatPaymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.fiat_payment_metadata import FiatPaymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FiatPaymentMetadata from a JSON string
fiat_payment_metadata_instance = FiatPaymentMetadata.from_json(json)
# print the JSON string representation of the object
print(FiatPaymentMetadata.to_json())

# convert the object into a dict
fiat_payment_metadata_dict = fiat_payment_metadata_instance.to_dict()
# create an instance of FiatPaymentMetadata from a dict
fiat_payment_metadata_from_dict = FiatPaymentMetadata.from_dict(fiat_payment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



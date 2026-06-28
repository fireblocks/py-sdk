# ManifestOrderInfo

Defines requirements for the POST /orders endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_types** | [**List[SettlementTypeEnum]**](SettlementTypeEnum.md) | Supported settlement types when creating an order. If present - settlement is required. If absent - no need to provide settlement.  | [optional] 
**execution_types** | [**List[ExecutionRequestDetailsType]**](ExecutionRequestDetailsType.md) | Supported execution types when creating an order. | 
**requires_reason_for_payment** | **bool** | Information about the source and purpose of the funds being transacted. Used by providers that require additional context for compliance and reporting. Provide this field when the provider manifest indicates it is required.  | [optional] 

## Example

```python
from fireblocks.models.manifest_order_info import ManifestOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestOrderInfo from a JSON string
manifest_order_info_instance = ManifestOrderInfo.from_json(json)
# print the JSON string representation of the object
print(ManifestOrderInfo.to_json())

# convert the object into a dict
manifest_order_info_dict = manifest_order_info_instance.to_dict()
# create an instance of ManifestOrderInfo from a dict
manifest_order_info_from_dict = ManifestOrderInfo.from_dict(manifest_order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



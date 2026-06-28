# ManifestOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | Indicates whether the endpoint is supported by the provider | 
**participants_identification_policy** | [**ParticipantsIdentificationPolicy**](ParticipantsIdentificationPolicy.md) |  | [optional] 
**supported_parties** | [**List[ParticipantRelationshipType]**](ParticipantRelationshipType.md) | The participant party types the provider supports for this endpoint.  | [optional] 
**settlement_types** | [**List[SettlementTypeEnum]**](SettlementTypeEnum.md) | Supported settlement types when creating an order. If present - settlement is required. If absent - no need to provide settlement.  | [optional] 
**execution_types** | [**List[ExecutionRequestDetailsType]**](ExecutionRequestDetailsType.md) | Supported execution types when creating an order. | 
**requires_reason_for_payment** | **bool** | Information about the source and purpose of the funds being transacted. Used by providers that require additional context for compliance and reporting. Provide this field when the provider manifest indicates it is required.  | [optional] 

## Example

```python
from fireblocks.models.manifest_order import ManifestOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestOrder from a JSON string
manifest_order_instance = ManifestOrder.from_json(json)
# print the JSON string representation of the object
print(ManifestOrder.to_json())

# convert the object into a dict
manifest_order_dict = manifest_order_instance.to_dict()
# create an instance of ManifestOrder from a dict
manifest_order_from_dict = ManifestOrder.from_dict(manifest_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PolicyRule

V2 Policy rule which is enforced on transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the policy rule | 
**id** | **str** | Unique identifier for the policy rule | 
**policy_engine_version** | **str** | Policy engine version | 
**type** | [**PolicyType**](PolicyType.md) |  | 
**sub_type** | [**PolicyType**](PolicyType.md) |  | [optional] 
**initiator** | [**InitiatorConfigPattern**](InitiatorConfigPattern.md) |  | 
**asset** | [**AssetConfig**](AssetConfig.md) |  | 
**source** | [**AccountConfig**](AccountConfig.md) |  | 
**destination** | [**DestinationConfig**](DestinationConfig.md) |  | [optional] 
**account** | [**AccountConfig**](AccountConfig.md) |  | [optional] 
**verdict** | [**VerdictConfig**](VerdictConfig.md) |  | 
**amount_over_time** | [**AmountOverTimeConfig**](AmountOverTimeConfig.md) |  | [optional] 
**amount** | [**AmountRange**](AmountRange.md) |  | [optional] 
**external_descriptor** | **str** | External descriptor for the rule | [optional] 
**method** | [**ContractMethodPattern**](ContractMethodPattern.md) |  | [optional] 
**is_global_policy** | **bool** | Whether this is a global policy | [optional] 
**program_call** | [**ProgramCallConfig**](ProgramCallConfig.md) |  | [optional] 
**screening_metadata** | [**ScreeningMetadataConfig**](ScreeningMetadataConfig.md) |  | [optional] 
**quote_asset** | [**AssetConfig**](AssetConfig.md) |  | [optional] 
**base_asset** | [**AssetConfig**](AssetConfig.md) |  | [optional] 
**quote_amount** | [**AmountRange**](AmountRange.md) |  | [optional] 
**base_amount** | [**AmountRange**](AmountRange.md) |  | [optional] 
**derivation_path** | [**DerivationPathConfig**](DerivationPathConfig.md) |  | [optional] 
**index** | **float** | Index for the policy rule | [optional] 

## Example

```python
from fireblocks.models.policy_rule import PolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRule from a JSON string
policy_rule_instance = PolicyRule.from_json(json)
# print the JSON string representation of the object
print(PolicyRule.to_json())

# convert the object into a dict
policy_rule_dict = policy_rule_instance.to_dict()
# create an instance of PolicyRule from a dict
policy_rule_from_dict = PolicyRule.from_dict(policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AmlScreeningResult

The result of the AML screening. Mirrors the output of the developer-api transaction formatter (IFormattedAmlResult). Not all fields are present in every response — the set depends on the AML provider and screening flow. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The AML provider name. Known values: CHAINALYSIS, ELLIPTIC, CHAINALYSIS_V2, ELLIPTIC_HOLISTIC, BYORK_SLITE, BYORK_LITE, NONE.  | [optional] 
**payload** | **Dict[str, object]** | The raw, unmodified screening response from the provider. Structure varies per provider.  | [optional] 
**verdict** | [**ScreeningVerdictEnum**](ScreeningVerdictEnum.md) |  | [optional] 
**screening_status** | [**ScreeningStatusEnum**](ScreeningStatusEnum.md) |  | [optional] 
**bypass_reason** | [**AmlBypassReasonEnum**](AmlBypassReasonEnum.md) |  | [optional] 
**timestamp** | **float** | Unix timestamp in milliseconds when the screening result was generated. | [optional] 
**customer_ref_id** | **str** | Customer-provided reference identifier for tracking. | [optional] 
**external_id** | **str** | External identifier for the screening (provider-specific). | [optional] 
**category** | **str** | Risk category classification. The available categories are subject to change depending on the provider.  | [optional] 
**category_id** | **float** | Numeric identifier for the risk category. | [optional] 
**risk** | **str** | Provider-specific risk level. Values vary by provider. | [optional] 
**dest_address** | **str** | The destination blockchain address associated with the screening. | [optional] 
**matched_rule** | [**AmlMatchedRule**](AmlMatchedRule.md) |  | [optional] 
**matched_prescreening_rule** | [**AmlMatchedRule**](AmlMatchedRule.md) |  | [optional] 
**matched_alert** | [**AmlAlert**](AmlAlert.md) |  | [optional] 

## Example

```python
from fireblocks.models.aml_screening_result import AmlScreeningResult

# TODO update the JSON string below
json = "{}"
# create an instance of AmlScreeningResult from a JSON string
aml_screening_result_instance = AmlScreeningResult.from_json(json)
# print the JSON string representation of the object
print(AmlScreeningResult.to_json())

# convert the object into a dict
aml_screening_result_dict = aml_screening_result_instance.to_dict()
# create an instance of AmlScreeningResult from a dict
aml_screening_result_from_dict = AmlScreeningResult.from_dict(aml_screening_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ComplianceScreeningResultFullPayload

The result of the AML/Travel Rule screening. This unified schema contains all fields that may be returned for both AML and Travel Rule screening results. Not all fields will be present in every response - the actual fields depend on the screening type and provider. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The AML/Travel Rule provider name. For AML: ELLIPTIC, CHAINALYSIS, etc. For Travel Rule: NOTABENE, SUMSUB, or any TRLink provider name  | [optional] 
**payload** | **object** | The raw payload of the screening result from the provider. The payload is a JSON object that contains the screening result. The payload structure is different for each screening provider. This field contains the complete, unmodified response from the screening service.  | [optional] 
**timestamp** | **float** | Unix timestamp in milliseconds when the screening result was generated | [optional] 
**screening_status** | **str** | Current status of the screening process | [optional] 
**bypass_reason** | **str** | Reason for bypassing the screening, if applicable. For AML: SANCTIONS_SCREENING_BYPASS, SANCTIONS_RECIPIENT_BYPASS, etc. For Travel Rule: BELOW_THRESHOLD, NO_TRM_AVAILABLE, etc.  | [optional] 
**status** | [**AmlStatusEnum**](AmlStatusEnum.md) |  | [optional] 
**prev_status** | [**AmlStatusEnum**](AmlStatusEnum.md) |  | [optional] 
**prev_bypass_reason** | **str** | Previous bypass reason before the current bypass reason change | [optional] 
**verdict** | [**ScreeningVerdictEnum**](ScreeningVerdictEnum.md) |  | [optional] 
**risk** | [**ScreeningRiskLevelEnum**](ScreeningRiskLevelEnum.md) |  | [optional] 
**extended_risk** | [**ScreeningRiskLevelEnum**](ScreeningRiskLevelEnum.md) |  | [optional] 
**external_id** | **str** | External identifier for the screening (provider-specific) | [optional] 
**customer_ref_id** | **str** | Customer-provided reference identifier for tracking | [optional] 
**ref_id** | **str** | Internal reference identifier | [optional] 
**category** | **str** | Risk category classification. Examples: EXCHANGE, GAMBLING, MIXER, DARKNET_SERVICE, SANCTIONED_ENTITY  | [optional] 
**category_id** | **float** | Numeric identifier for the risk category | [optional] 
**dest_address** | **str** | The destination blockchain address associated with the screening | [optional] 
**dest_tag** | **str** | Destination tag or memo (for chains that support it like XRP, XLM) | [optional] 
**dest_record_id** | **str** | The destination record identifier used by the screening provider | [optional] 
**address_resolution_signature** | **str** | Cryptographic signature for address resolution verification | [optional] 
**aml_result** | [**ScreeningAmlResult**](ScreeningAmlResult.md) |  | [optional] 
**result** | [**ScreeningTravelRuleResult**](ScreeningTravelRuleResult.md) |  | [optional] 
**details_message** | **str** | Additional human-readable details or message about the screening result | [optional] 
**matched_alert** | **object** | Information about the AML alert that was matched, if any. Contains details about the specific alert that triggered during screening.  | [optional] 
**matched_rule** | **object** | The matched rule information for this screening result. Contains details about which screening rule was applied and matched.  | [optional] 
**matched_prescreening_rule** | [**ScreeningTravelRulePrescreeningRule**](ScreeningTravelRulePrescreeningRule.md) |  | [optional] 
**matched_no_trm_screening_rule** | **object** | Matched no-TRM (Travel Rule Message) screening rule details. Used when TRLink screening detects a missing TRM scenario.  | [optional] 
**customer_integration_id** | **str** | Customer integration identifier used by Travel Rule providers | [optional] 
**customer_short_name** | **str** | Customer short name registered with Travel Rule providers | [optional] 
**travel_rule_message_id** | **str** | Travel rule message identifier for linking and tracking across providers | [optional] 

## Example

```python
from fireblocks.models.compliance_screening_result_full_payload import ComplianceScreeningResultFullPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceScreeningResultFullPayload from a JSON string
compliance_screening_result_full_payload_instance = ComplianceScreeningResultFullPayload.from_json(json)
# print the JSON string representation of the object
print(ComplianceScreeningResultFullPayload.to_json())

# convert the object into a dict
compliance_screening_result_full_payload_dict = compliance_screening_result_full_payload_instance.to_dict()
# create an instance of ComplianceScreeningResultFullPayload from a dict
compliance_screening_result_full_payload_from_dict = ComplianceScreeningResultFullPayload.from_dict(compliance_screening_result_full_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



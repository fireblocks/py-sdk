# ScreeningAmlResult

Detailed AML screening result information. Contains alerts, risk scores, and other AML-specific data from provider-specific responses. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[ScreeningAmlAlert]**](ScreeningAmlAlert.md) | List of AML alerts triggered during screening | [optional] 
**provider_response** | **Dict[str, object]** | Complete response from the AML provider. This is a dynamic object that varies significantly between different AML providers (Chainalysis, Elliptic, etc.). Each provider has their own proprietary response format and schema.  Examples of provider-specific structures: - Chainalysis: Contains cluster info, risk scores, sanctions data - Elliptic: Includes risk assessment, entity types, compliance flags  The structure is provider-dependent and cannot be standardized as each vendor implements their own proprietary data models and response formats.  | [optional] 
**matched_rule** | [**ScreeningAmlMatchedRule**](ScreeningAmlMatchedRule.md) |  | [optional] 
**matched_alert** | [**ScreeningAmlAlert**](ScreeningAmlAlert.md) |  | [optional] 

## Example

```python
from fireblocks.models.screening_aml_result import ScreeningAmlResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningAmlResult from a JSON string
screening_aml_result_instance = ScreeningAmlResult.from_json(json)
# print the JSON string representation of the object
print(ScreeningAmlResult.to_json())

# convert the object into a dict
screening_aml_result_dict = screening_aml_result_instance.to_dict()
# create an instance of ScreeningAmlResult from a dict
screening_aml_result_from_dict = ScreeningAmlResult.from_dict(screening_aml_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



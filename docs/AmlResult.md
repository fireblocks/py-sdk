# AmlResult

Detailed AML screening result information. Contains alerts, risk scores, and other AML-specific data from provider-specific responses. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[AmlAlert]**](AmlAlert.md) | List of AML alerts triggered during screening | [optional] 
**provider_response** | **Dict[str, object]** | Complete response from the AML provider. This is a dynamic object that varies significantly between different AML providers (Chainalysis, Elliptic, etc.). Each provider has their own proprietary response format and schema.  Examples of provider-specific structures: - Chainalysis: Contains cluster info, risk scores, sanctions data - Elliptic: Includes risk assessment, entity types, compliance flags  The structure is provider-dependent and cannot be standardized as each vendor implements their own proprietary data models and response formats.  | [optional] 
**matched_rule** | [**AmlMatchedRule**](AmlMatchedRule.md) |  | [optional] 
**matched_alert** | [**AmlAlert**](AmlAlert.md) |  | [optional] 

## Example

```python
from fireblocks.models.aml_result import AmlResult

# TODO update the JSON string below
json = "{}"
# create an instance of AmlResult from a JSON string
aml_result_instance = AmlResult.from_json(json)
# print the JSON string representation of the object
print(AmlResult.to_json())

# convert the object into a dict
aml_result_dict = aml_result_instance.to_dict()
# create an instance of AmlResult from a dict
aml_result_from_dict = AmlResult.from_dict(aml_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



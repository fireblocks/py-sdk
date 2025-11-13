# TRLinkRegistrationResult

TRLink registration result containing status and metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TRLinkRegistrationStatus**](TRLinkRegistrationStatus.md) |  | 
**provider** | **str** | The TRLink provider name | [optional] 
**success** | **bool** | Whether the registration was successful | [optional] 
**timestamp** | **float** | Unix timestamp of the registration | 
**dest_record_id** | **str** | Destination record identifier | [optional] 
**travel_rule_message_id** | **str** | Travel rule message identifier for linking | [optional] 
**customer_integration_id** | **str** | Customer integration identifier | [optional] 
**customer_short_name** | **str** | Customer short name | [optional] 
**result** | [**TRLinkProviderResult**](TRLinkProviderResult.md) |  | [optional] 
**matched_prescreening_rule** | [**TRLinkPreScreeningRule**](TRLinkPreScreeningRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_registration_result import TRLinkRegistrationResult

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkRegistrationResult from a JSON string
tr_link_registration_result_instance = TRLinkRegistrationResult.from_json(json)
# print the JSON string representation of the object
print(TRLinkRegistrationResult.to_json())

# convert the object into a dict
tr_link_registration_result_dict = tr_link_registration_result_instance.to_dict()
# create an instance of TRLinkRegistrationResult from a dict
tr_link_registration_result_from_dict = TRLinkRegistrationResult.from_dict(tr_link_registration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TRLinkRegistrationResultFullPayload

TRLink registration result containing status and metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TRLinkRegistrationStatusEnum**](TRLinkRegistrationStatusEnum.md) |  | 
**provider** | **str** | The TRLink provider name | [optional] 
**success** | **bool** | Whether the registration was successful | [optional] 
**timestamp** | **float** | Unix timestamp of the registration | 
**dest_record_id** | **str** | Destination record identifier | [optional] 
**travel_rule_message_id** | **str** | Travel rule message identifier for linking | [optional] 
**customer_integration_id** | **str** | Customer integration identifier | [optional] 
**customer_short_name** | **str** | Customer short name | [optional] 
**result** | [**TRLinkProviderResult**](TRLinkProviderResult.md) |  | [optional] 
**matched_prescreening_rule** | [**ScreeningTRLinkPrescreeningRule**](ScreeningTRLinkPrescreeningRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_registration_result_full_payload import TRLinkRegistrationResultFullPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkRegistrationResultFullPayload from a JSON string
tr_link_registration_result_full_payload_instance = TRLinkRegistrationResultFullPayload.from_json(json)
# print the JSON string representation of the object
print(TRLinkRegistrationResultFullPayload.to_json())

# convert the object into a dict
tr_link_registration_result_full_payload_dict = tr_link_registration_result_full_payload_instance.to_dict()
# create an instance of TRLinkRegistrationResultFullPayload from a dict
tr_link_registration_result_full_payload_from_dict = TRLinkRegistrationResultFullPayload.from_dict(tr_link_registration_result_full_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



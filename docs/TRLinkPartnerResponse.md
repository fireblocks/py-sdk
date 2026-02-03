# TRLinkPartnerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Partner unique identifier | 
**ident** | **str** | Partner identification code | 
**name** | **str** | Partner display name | 
**description** | **str** | Partner description | [optional] 
**base_url** | **str** | Partner API base URL | 
**active** | **bool** | Whether the partner is active | 
**is_test** | **bool** | Whether this is a test/sandbox partner | 

## Example

```python
from fireblocks.models.tr_link_partner_response import TRLinkPartnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkPartnerResponse from a JSON string
tr_link_partner_response_instance = TRLinkPartnerResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkPartnerResponse.to_json())

# convert the object into a dict
tr_link_partner_response_dict = tr_link_partner_response_instance.to_dict()
# create an instance of TRLinkPartnerResponse from a dict
tr_link_partner_response_from_dict = TRLinkPartnerResponse.from_dict(tr_link_partner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



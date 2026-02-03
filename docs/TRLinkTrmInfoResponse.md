# TRLinkTrmInfoResponse

Travel Rule Message information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | TRM message ID | 
**version** | **str** | TRM version | [optional] 
**status** | [**TRLinkTrmStatus**](TRLinkTrmStatus.md) |  | [optional] 
**reason** | **str** | Human readable reason for the current status | [optional] 
**external_id** | **str** | External ID (e.g., Fireblocks ID) | 
**asset** | [**TRLinkAsset**](TRLinkAsset.md) |  | 
**amount** | **str** | Transaction amount in asset units | 
**fiat_value** | [**TRLinkFiatValue**](TRLinkFiatValue.md) |  | [optional] 
**direction** | [**TRLinkTrmDirection**](TRLinkTrmDirection.md) |  | 
**originator_vasp_id** | **str** | ID of the originator VASP | [optional] 
**beneficiary_vasp_id** | **str** | ID of the beneficiary VASP | [optional] 
**txn_info** | [**TRLinkTxnInfo**](TRLinkTxnInfo.md) |  | 
**ivms101** | [**TRLinkIvmsResponse**](TRLinkIvmsResponse.md) |  | 
**provider_data** | [**TRLinkProviderData**](TRLinkProviderData.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_trm_info_response import TRLinkTrmInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkTrmInfoResponse from a JSON string
tr_link_trm_info_response_instance = TRLinkTrmInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkTrmInfoResponse.to_json())

# convert the object into a dict
tr_link_trm_info_response_dict = tr_link_trm_info_response_instance.to_dict()
# create an instance of TRLinkTrmInfoResponse from a dict
tr_link_trm_info_response_from_dict = TRLinkTrmInfoResponse.from_dict(tr_link_trm_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



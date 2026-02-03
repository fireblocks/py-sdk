# TRLinkAssessTravelRuleRequest

Request to assess whether Travel Rule compliance is required for a transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | Fireblocks transaction ID (optional) - RECOMMENDED for inbound transactions | [optional] 
**amount** | **str** | Transaction amount (required when txId not provided) | [optional] 
**amount_usd** | **str** | Transaction amount in USD (optional) | [optional] 
**destination** | [**TRLinkDestinationTransferPeerPath**](TRLinkDestinationTransferPeerPath.md) |  | [optional] 
**dest_address** | **str** | Destination address (optional) | [optional] 
**dest_tag** | **str** | Destination tag (optional) | [optional] 
**source** | [**TRLinkSourceTransferPeerPath**](TRLinkSourceTransferPeerPath.md) |  | [optional] 
**src_address** | **str** | Source address (optional) | [optional] 
**asset_id** | **str** | Asset identifier (e.g., ETH, BTC, USDC) | [optional] 
**direction** | [**TRLinkTransactionDirection**](TRLinkTransactionDirection.md) |  | [optional] 
**tx_hash** | **str** | Transaction hash (optional) | [optional] 
**originator_vasp_id** | **str** | Originator VASP identifier - required for inbound transactions | [optional] 
**beneficiary_vasp_id** | **str** | Beneficiary VASP identifier - required for outbound transactions | [optional] 

## Example

```python
from fireblocks.models.tr_link_assess_travel_rule_request import TRLinkAssessTravelRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAssessTravelRuleRequest from a JSON string
tr_link_assess_travel_rule_request_instance = TRLinkAssessTravelRuleRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkAssessTravelRuleRequest.to_json())

# convert the object into a dict
tr_link_assess_travel_rule_request_dict = tr_link_assess_travel_rule_request_instance.to_dict()
# create an instance of TRLinkAssessTravelRuleRequest from a dict
tr_link_assess_travel_rule_request_from_dict = TRLinkAssessTravelRuleRequest.from_dict(tr_link_assess_travel_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TRLinkCreateTrmRequest

Request to create a Travel Rule Message with IVMS101 PII data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Asset identifier (required when txId not provided) | [optional] 
**amount** | **str** | Transaction amount (required when txId not provided) | [optional] 
**amount_usd** | **str** | Amount in USD (optional) | [optional] 
**source** | [**TRLinkSourceTransferPeerPath**](TRLinkSourceTransferPeerPath.md) |  | [optional] 
**src_address** | **str** | Source address (optional) | [optional] 
**destination** | [**TRLinkDestinationTransferPeerPath**](TRLinkDestinationTransferPeerPath.md) |  | [optional] 
**dest_address** | **str** | Destination address (optional) | [optional] 
**dest_tag** | **str** | Destination tag (optional) | [optional] 
**tx_id** | **str** | Fireblocks transaction ID (optional) - RECOMMENDED for inbound transactions | [optional] 
**tx_hash** | **str** | Transaction hash (optional) | [optional] 
**direction** | [**TRLinkTransactionDirection**](TRLinkTransactionDirection.md) |  | [optional] 
**originator_vasp_id** | **str** | Originator VASP identifier - required for inbound transactions | [optional] 
**beneficiary_vasp_id** | **str** | Beneficiary VASP identifier - required for outbound transactions | [optional] 
**ivms101** | [**TRLinkIvms**](TRLinkIvms.md) |  | 

## Example

```python
from fireblocks.models.tr_link_create_trm_request import TRLinkCreateTrmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkCreateTrmRequest from a JSON string
tr_link_create_trm_request_instance = TRLinkCreateTrmRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkCreateTrmRequest.to_json())

# convert the object into a dict
tr_link_create_trm_request_dict = tr_link_create_trm_request_instance.to_dict()
# create an instance of TRLinkCreateTrmRequest from a dict
tr_link_create_trm_request_from_dict = TRLinkCreateTrmRequest.from_dict(tr_link_create_trm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ExtraParameters

Additional protocol / operation specific key-value parameters:  For UTXO-based blockchain input selection, add the key `inputsSelection` with the value set to the [input selection structure.](https://developers.fireblocks.com/reference/transaction-objects#inputsselection) The inputs can be retrieved from the [Retrieve Unspent Inputs endpoint.](https://developers.fireblocks.com/reference/getunspentinputs)  For `RAW` operations, add the key `rawMessageData` with the value set to the [raw message data structure.](https://developers.fireblocks.com/reference/raw-signing-objects#rawmessagedata)  For `CONTRACT_CALL` operations, add the key `contractCallData` with the value set to the Ethereum smart contract Application Binary Interface (ABI) payload. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions. For **exchange compliance (e.g., Binance) and Travel Rule purposes**, include the key `piiData` containing a **custom JSON structure** with Personally Identifiable Information (PII) relevant to the transaction. This data must be fully **encrypted by the sender** before being submitted to the Fireblocks API. The recommended encryption method is **hybrid encryption** using AES-256-GCM for the payload and RSA-OAEP for key exchange, with the recipient exchange's public key. [development libraries](https://developers.fireblocks.com/docs/a-developers-guide-to-constructing-encrypted-pii-messages-for-binance-via-fireblocks)  **Note:** `rawMessageData`, `contractCallData`, and `inputsSelection` cannot be used together in the same call. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_controls** | **Dict[str, object]** |  | [optional] 
**raw_message_data** | **Dict[str, object]** |  | [optional] 
**contract_call_data** | **str** |  | [optional] 
**program_call_data** | **str** |  | [optional] 
**inputs_selection** | **Dict[str, object]** |  | [optional] 
**allow_base_asset_address** | **bool** |  | [optional] 
**pii_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks.models.extra_parameters import ExtraParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraParameters from a JSON string
extra_parameters_instance = ExtraParameters.from_json(json)
# print the JSON string representation of the object
print(ExtraParameters.to_json())

# convert the object into a dict
extra_parameters_dict = extra_parameters_instance.to_dict()
# create an instance of ExtraParameters from a dict
extra_parameters_from_dict = ExtraParameters.from_dict(extra_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



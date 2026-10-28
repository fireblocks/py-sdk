# SorobanCallData

The Soroban contract invocation to execute, for `SOROBAN_CALL` operations.  Fireblocks decodes the submitted envelope, determines the footprint, resource fee, sequence number and authorization entries from its own simulation, and signs a transaction it rebuilt from the invocation. Only the contract invocation itself is carried through unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envelope_xdr** | **bytearray** | A base64 encoded, unsigned Stellar &#x60;TransactionEnvelope&#x60; carrying exactly one &#x60;invokeHostFunction&#x60; operation that invokes a contract.  The API only checks that the value is present. The envelope is decoded and validated after the transaction is created, and a transaction whose envelope fails validation is not signed and ends as &#x60;FAILED&#x60;. An envelope is rejected if it carries signatures or authorization entries, a memo or a fee-bump wrapper, if its source account is not the Stellar address of the vault account, or if it has no bounded time window.  A Stellar transaction cannot exceed 132096 bytes, about 176128 base64 characters. | 

## Example

```python
from fireblocks.models.soroban_call_data import SorobanCallData

# TODO update the JSON string below
json = "{}"
# create an instance of SorobanCallData from a JSON string
soroban_call_data_instance = SorobanCallData.from_json(json)
# print the JSON string representation of the object
print(SorobanCallData.to_json())

# convert the object into a dict
soroban_call_data_dict = soroban_call_data_instance.to_dict()
# create an instance of SorobanCallData from a dict
soroban_call_data_from_dict = SorobanCallData.from_dict(soroban_call_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



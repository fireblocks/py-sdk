# fireblocks_client.model.payout_response.PayoutResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**[instructionSet](#instructionSet)** | list, tuple,  | tuple,  |  | 
**state** | [**PayoutState**](PayoutState.md) | [**PayoutState**](PayoutState.md) |  | 
**payoutId** | str,  | str,  |  | 
**paymentAccount** | [**PaymentAccountResponse**](PaymentAccountResponse.md) | [**PaymentAccountResponse**](PaymentAccountResponse.md) |  | 
**status** | [**PayoutStatus**](PayoutStatus.md) | [**PayoutStatus**](PayoutStatus.md) |  | 
**reasonOfFailure** | str,  | str,  | &lt;ul&gt;  &lt;li&gt; INSUFFICIENT_BALANCE&lt;/li&gt; &lt;li&gt; SOURCE_TRANSLATION&lt;/li&gt; &lt;li&gt; SOURCE_NOT_UNIQUE&lt;/li&gt; &lt;li&gt; SOURCE_NOT_FOUND&lt;/li&gt; &lt;li&gt; SOURCE_TYPE_NOT_SUPPORTED&lt;/li&gt; &lt;li&gt; EMPTY_SOURCE&lt;/li&gt; &lt;li&gt; DESTINATION_TRANSLATION&lt;/li&gt; &lt;li&gt; DESTINATION_NOT_UNIQUE&lt;/li&gt; &lt;li&gt; DESTINATION_NOT_FOUND&lt;/li&gt; &lt;li&gt; EMPTY_DESTINATION&lt;/li&gt; &lt;li&gt; PARSING &lt;/li&gt; &lt;li&gt; UNKNOWN&lt;/li&gt; &lt;li&gt; FIREBLOCKS_CLIENT&lt;/li&gt; &lt;li&gt; TRANSACTION_SUBMISSION&lt;/li&gt; &lt;/ul&gt;  | [optional] 
**initMethod** | [**PayoutInitMethod**](PayoutInitMethod.md) | [**PayoutInitMethod**](PayoutInitMethod.md) |  | [optional] 
**reportUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instructionSet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PayoutInstructionResponse**](PayoutInstructionResponse.md) | [**PayoutInstructionResponse**](PayoutInstructionResponse.md) | [**PayoutInstructionResponse**](PayoutInstructionResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


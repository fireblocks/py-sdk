# PayoutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** |  | 
**payment_account** | [**PaymentAccountResponse**](PaymentAccountResponse.md) |  | 
**created_at** | **float** |  | 
**state** | [**PayoutState**](PayoutState.md) |  | 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**reason_of_failure** | **str** | &lt;ul&gt;  &lt;li&gt; INSUFFICIENT_BALANCE&lt;/li&gt; &lt;li&gt; SOURCE_TRANSLATION&lt;/li&gt; &lt;li&gt; SOURCE_NOT_UNIQUE&lt;/li&gt; &lt;li&gt; SOURCE_NOT_FOUND&lt;/li&gt; &lt;li&gt; SOURCE_TYPE_NOT_SUPPORTED&lt;/li&gt; &lt;li&gt; EMPTY_SOURCE&lt;/li&gt; &lt;li&gt; DESTINATION_TRANSLATION&lt;/li&gt; &lt;li&gt; DESTINATION_NOT_UNIQUE&lt;/li&gt; &lt;li&gt; DESTINATION_NOT_FOUND&lt;/li&gt; &lt;li&gt; EMPTY_DESTINATION&lt;/li&gt; &lt;li&gt; PARSING &lt;/li&gt; &lt;li&gt; UNKNOWN&lt;/li&gt; &lt;li&gt; FIREBLOCKS_CLIENT&lt;/li&gt; &lt;li&gt; TRANSACTION_SUBMISSION&lt;/li&gt; &lt;/ul&gt;  | [optional] 
**init_method** | [**PayoutInitMethod**](PayoutInitMethod.md) |  | [optional] 
**instruction_set** | [**List[PayoutInstructionResponse]**](PayoutInstructionResponse.md) |  | 
**report_url** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.payout_response import PayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutResponse from a JSON string
payout_response_instance = PayoutResponse.from_json(json)
# print the JSON string representation of the object
print PayoutResponse.to_json()

# convert the object into a dict
payout_response_dict = payout_response_instance.to_dict()
# create an instance of PayoutResponse from a dict
payout_response_form_dict = payout_response.from_dict(payout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



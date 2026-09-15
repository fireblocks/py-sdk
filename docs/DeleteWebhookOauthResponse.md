# DeleteWebhookOauthResponse

The deleted OAuth credential set, plus the ids of any webhooks the delete detached from it. Webhooks are only detached by `forceDelete=true`; without it a delete is refused with `409` while anything still references the credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the OAuth credentials. Pass this as a webhook&#39;s &#x60;webhookOauthId&#x60; to attach them. | 
**name** | **str** | The label given to this credential set. | 
**client_id** | **str** | OAuth client ID used to authenticate with the token endpoint. | 
**url** | **str** | Token endpoint URL. | 
**auth_method** | **str** | How the client credentials are presented to the token endpoint: &#x60;client_secret_basic&#x60;, &#x60;client_secret_post&#x60; or &#x60;client_secret_jwt&#x60;. Credentials created without this field report &#x60;client_secret_basic&#x60;, which is what they use. | [default to 'client_secret_basic']
**custom_jwt_claims** | **List[str]** | Names of the additional claims placed in the JWT assertion. Claim values are write-only and are never returned. Absent when no custom claims are configured. | [optional] 
**custom_body_params** | **List[str]** | Names of the additional parameters added to the token request body. Parameter values are write-only and are never returned. Absent when no custom parameters are configured. | [optional] 
**custom_headers** | **List[str]** | Names of the additional HTTP headers added to **the token request sent to the authorization server** — not to the webhook delivery, which has its own separate &#x60;customHeaders&#x60;. Header values are write-only and are never returned. Absent when no custom headers are configured. | [optional] 
**mtls_client_signed_cert** | **str** | PEM-encoded client certificate used for mTLS when fetching OAuth tokens. | [optional] 
**created_at** | **int** | The date and time the OAuth credentials were created, in milliseconds. | 
**updated_at** | **int** | The date and time the OAuth credentials were last updated, in milliseconds. | 
**detached_webhook_ids** | **List[str]** | Webhooks whose &#x60;webhookOauthId&#x60; was cleared. The webhooks themselves are not deleted and keep delivering, just without an &#x60;Authorization&#x60; header. Empty unless &#x60;forceDelete&#x3D;true&#x60; detached something. | 

## Example

```python
from fireblocks.models.delete_webhook_oauth_response import DeleteWebhookOauthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWebhookOauthResponse from a JSON string
delete_webhook_oauth_response_instance = DeleteWebhookOauthResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteWebhookOauthResponse.to_json())

# convert the object into a dict
delete_webhook_oauth_response_dict = delete_webhook_oauth_response_instance.to_dict()
# create an instance of DeleteWebhookOauthResponse from a dict
delete_webhook_oauth_response_from_dict = DeleteWebhookOauthResponse.from_dict(delete_webhook_oauth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



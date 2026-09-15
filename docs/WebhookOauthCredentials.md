# WebhookOauthCredentials

A stored OAuth 2.0 client credential set, referenced by webhooks through their `webhookOauthId`. When a webhook references one, the dispatcher fetches a bearer token from `url` before each delivery and attaches it as `Authorization: Bearer {token}`. Secret material is never returned: `clientSecret` is absent from this schema entirely, and the `customJwtClaims`, `customBodyParams` and `customHeaders` fields are reduced to their names, without the configured values.

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

## Example

```python
from fireblocks.models.webhook_oauth_credentials import WebhookOauthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOauthCredentials from a JSON string
webhook_oauth_credentials_instance = WebhookOauthCredentials.from_json(json)
# print the JSON string representation of the object
print(WebhookOauthCredentials.to_json())

# convert the object into a dict
webhook_oauth_credentials_dict = webhook_oauth_credentials_instance.to_dict()
# create an instance of WebhookOauthCredentials from a dict
webhook_oauth_credentials_from_dict = WebhookOauthCredentials.from_dict(webhook_oauth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



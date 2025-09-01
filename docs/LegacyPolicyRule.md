# LegacyPolicyRule

Policy rule which is enforced on transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | (deprecated - replaced by \&quot;operators\&quot;)  | Defines users who can initiate the type of transaction to which the rule applies. options are * \&quot;*\&quot; - All users are allowed * Specific User id | [optional] 
**operators** | [**LegacyPolicyRuleOperators**](LegacyPolicyRuleOperators.md) |  | [optional] 
**transaction_type** | **str** | Defines the type of transaction to which the rule applies.   * TRANSFER - Default. Transfers funds from one account to another   * CONTRACT_CALL - Calls a smart contract, mainly for DeFi operations.   * APPROVE - Allows a smart contract to withdraw from a designated wallet.   * MINT - Perform a mint operation (increase supply) on a supported token   * BURN - Perform a burn operation (reduce supply) on a supported token   * SUPPLY - Use for DeFi to lend assets   * REDEEM - Use for DeFi to get lending back   * STAKE - Allows you to allocate and lock certain assets for earning staking rewards.   * RAW - An off-chain message with no predefined format, use it to sign any message with your private key.   * TYPED_MESSAGE - An off-chain message type that follows a predefined format, used to sign specific messages that are not actual transactions.   * PROGRAM_CALL - In Solana refers to invoking on-chain programs (smart contracts) to execute transactions and interact with the blockchain.  | [optional] 
**designated_signer** | **str** | (deprecated - replaced by \&quot;designatedSigners\&quot;) Id representing the user who signs transactions that match a specific rule | [optional] 
**designated_signers** | [**LegacyPolicyRuleDesignatedSigners**](LegacyPolicyRuleDesignatedSigners.md) |  | [optional] 
**type** | **str** | Policy rule type | 
**action** | **str** | Defines what occurs when a transaction meets the rule&#39;s criteria * ALLOW - The transaction goes through and can be signed without requiring additional approvals * BLOCK - The transaction is automatically blocked * 2-TIER - Only these users or user groups can approve             If any of them reject the transaction before the required approval threshold is met, the transaction doesn&#39;t go through            The list of entities are set is \&quot;authorizationGroups\&quot; field  | 
**asset** | **str** | Defines the type of asset being transacted, options are * \&quot;*\&quot; - All assets * Specific asset  | 
**src_type** | [**LegacyPolicySrcOrDestType**](LegacyPolicySrcOrDestType.md) | (deprecated - replaced by \&quot;src\&quot;) source account type | [optional] 
**src_sub_type** | [**LegacyPolicySrcOrDestSubType**](LegacyPolicySrcOrDestSubType.md) | (deprecated - replaced by \&quot;src\&quot;) source sub account type | [optional] 
**src_id** | **str** | (deprecated - replaced by \&quot;src\&quot;) source account id | [optional] 
**src** | [**LegacyPolicyRuleSrc**](LegacyPolicyRuleSrc.md) |  | [optional] 
**dst_type** | [**LegacyPolicySrcOrDestType**](LegacyPolicySrcOrDestType.md) | (deprecated - replaced by \&quot;dst\&quot;) destination account type | [optional] 
**dst_sub_type** | [**LegacyPolicySrcOrDestSubType**](LegacyPolicySrcOrDestSubType.md) | (deprecated - replaced by \&quot;dst\&quot;) destination sub account type | [optional] 
**dst_id** | **str** | (deprecated - replaced by \&quot;dst\&quot;) destination account id | [optional] 
**dst** | [**LegacyPolicyRuleDst**](LegacyPolicyRuleDst.md) |  | [optional] 
**dst_address_type** | **str** | Defines whether the destination to which you are sending funds must be whitelisted, to allow one-time transfers to non-whitelisted external addresses, or both. By default, you can only transfer to an external address after it’s whitelisted.   * WHITELISTED - Can only be sent to whitelisted addresses.   * ONE_TIME - Can only be sent to non-whitelisted external addresses.   * \&quot;*\&quot; - can be sent to whitelisted addresses or non-whitelisted external  | [optional] 
**amount_currency** | **str** | * USD - Limits the amount of any asset users can transfer based on the USD equivalent of the asset. * EUR - Limits the amount of any asset users can transfer based on the EURO equivalent of the asset. * NATIVE - Limits the amount of an asset a user can transfer when using a specific asset.  | 
**amount_scope** | **str** | * SINGLE_TX - limit applies to a single transaction * TIMEFRAME - limit applies to all transactions within the defined time period  | 
**amount** | [**LegacyPolicyRuleAmount**](LegacyPolicyRuleAmount.md) |  | 
**period_sec** | **float** | Time period in seconds applied by the amountScope field to accumulate transferred amounts in transactions that match the rule, until the total exceeds the value you specify under Minimum. When the specified amount is reached within that period, whether by one or many transactions, further transactions in that period either fail or require more approvals.  | 
**authorizers** | **List[str]** | (deprecated - replaced by \&quot;authorizationGroups\&quot;) Allowed entities which can approves a transaction | [optional] 
**authorizers_count** | **float** | (deprecated - replaced by \&quot;authorizationGroups\&quot;) Min amount of entities which are needed to approve a transaction | [optional] 
**authorization_groups** | [**LegacyPolicyRuleAuthorizationGroups**](LegacyPolicyRuleAuthorizationGroups.md) |  | [optional] 
**amount_aggregation** | [**LegacyPolicyRuleAmountAggregation**](LegacyPolicyRuleAmountAggregation.md) |  | [optional] 
**raw_message_signing** | [**LegacyPolicyRuleRawMessageSigning**](LegacyPolicyRuleRawMessageSigning.md) |  | [optional] 
**apply_for_approve** | **bool** | Applying this rule over APPROVE type transactions (can only be enabled when rule&#39;s transaction type is TRANSFER) | [optional] 
**apply_for_typed_message** | **bool** | Applying this rule over TYPED_MESSAGE type transactions (can only be enabled when rule&#39;s transaction type is CONTRACT_CALL) | [optional] 
**external_descriptor** | **str** | A unique id identifying the rule | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule import LegacyPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRule from a JSON string
legacy_policy_rule_instance = LegacyPolicyRule.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRule.to_json())

# convert the object into a dict
legacy_policy_rule_dict = legacy_policy_rule_instance.to_dict()
# create an instance of LegacyPolicyRule from a dict
legacy_policy_rule_from_dict = LegacyPolicyRule.from_dict(legacy_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TransactionOperation

* `TRANSFER` - The default value for an operation. Transfers funds from one account to another. UTXO blockchains allow multi-input and multi-output transfers. All other blockchains allow transfers with one source address and one destination address. * `MINT` - Mints new tokens. Supported for Stellar, Ripple and EVM-based blockchains. * `BURN` - Burns tokens. Supported for Stellar, Ripple and EVM-based blockchains. * `CONTRACT_CALL` - Calls a smart contract method for web3 operations on any EVM blockchain. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions. * `PROGRAM_CALL` - Execute multiple instructions on Solana blockchain. The @solana/web3.js library is recommended for building program call transactions. Currently in beta and disabled * `TYPED_MESSAGE` - An off-chain message in either Ethereum Personal Message or EIP712 format. Use it to sign specific readable messages that are not actual transactions. [Learn more about typed messages](https://developers.fireblocks.com/docs/typed-message-signing). * `RAW` - An off-chain message with no predefined format. Use it to sign any message with your private key, including protocols such as blockchains and custom transaction types that are not natively supported by Fireblocks. [Learn more about raw signing transactions.](https://developers.fireblocks.com/docs/raw-message-signing) * `APPROVE` - Enables the approve function for a smart contract or wallet to  withdraw from a designated wallet. [Learn more](https://support.fireblocks.io/hc/en-us/articles/4404616097426-Amount-Cap-for-Approve-transactions). * `ENABLE_ASSET` - Algorand, DigitalBits, Solana, and Stellar require an on-chain transaction to create an asset wallet and enable the deposit address. This transaction is automatically created when adding assets on these blockchains at a vault account. 

## Enum

* `TRANSFER` (value: `'TRANSFER'`)

* `BURN` (value: `'BURN'`)

* `CONTRACT_CALL` (value: `'CONTRACT_CALL'`)

* `PROGRAM_CALL` (value: `'PROGRAM_CALL'`)

* `MINT` (value: `'MINT'`)

* `RAW` (value: `'RAW'`)

* `TYPED_MESSAGE` (value: `'TYPED_MESSAGE'`)

* `APPROVE` (value: `'APPROVE'`)

* `ENABLE_ASSET` (value: `'ENABLE_ASSET'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



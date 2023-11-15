# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireblocks_client import schemas  # noqa: F401


class TransactionOperation(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    * `TRANSFER` - The default value for an operation. Transfers funds from one account to another. UTXO blockchains allow multi-input and multi-output transfers. All other blockchains allow transfers with one source address and one destination address.
* `MINT` - Mints new tokens. Supported for Stellar, Ripple and EVM-based blockchains.
* `BURN` - Burns tokens. Supported for Stellar, Ripple and EVM-based blockchains.
* `CONTRACT_CALL` - Calls a smart contract method for web3 operations on any EVM blockchain. The Fireblocks [development libraries](https://developers.fireblocks.com/docs/ethereum-development#convenience-libraries) are recommended for building contract call transactions.
* `TYPED_MESSAGE` - An off-chain message in either Ethereum Personal Message or EIP712 format. Use it to sign specific readable messages that are not actual transactions. [Learn more about typed messages](https://developers.fireblocks.com/docs/typed-message-signing).
* `RAW` - An off-chain message with no predefined format. Use it to sign any message with your private key, including protocols such as blockchains and custom transaction types that are not natively supported by Fireblocks. [Learn more about raw signing transactions.](https://developers.fireblocks.com/docs/raw-message-signing)

    """
    
    @schemas.classproperty
    def TRANSFER(cls):
        return cls("TRANSFER")
    
    @schemas.classproperty
    def BURN(cls):
        return cls("BURN")
    
    @schemas.classproperty
    def CONTRACT_CALL(cls):
        return cls("CONTRACT_CALL")
    
    @schemas.classproperty
    def MINT(cls):
        return cls("MINT")
    
    @schemas.classproperty
    def RAW(cls):
        return cls("RAW")
    
    @schemas.classproperty
    def TYPED_MESSAGE(cls):
        return cls("TYPED_MESSAGE")

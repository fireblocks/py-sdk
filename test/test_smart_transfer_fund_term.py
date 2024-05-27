# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fireblocks_client.models.smart_transfer_fund_term import SmartTransferFundTerm


class TestSmartTransferFundTerm(unittest.TestCase):
    """SmartTransferFundTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTransferFundTerm:
        """Test SmartTransferFundTerm
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SmartTransferFundTerm`
        """
        model = SmartTransferFundTerm()
        if include_optional:
            return SmartTransferFundTerm(
                asset = 'BTC',
                amount = '133.789161216184',
                network_connection_id = '0805153d-e77d-4f9b-8818-e507eeb2d122',
                src_id = '2',
                src_type = 'VAULT_ACCOUNT',
                fee = '0.001',
                fee_level = 'MEDIUM',
                note = 'Transaction note'
            )
        else:
            return SmartTransferFundTerm(
                asset = 'BTC',
                amount = '133.789161216184',
                network_connection_id = '0805153d-e77d-4f9b-8818-e507eeb2d122',
                src_id = '2',
                src_type = 'VAULT_ACCOUNT',
        )
        """

    def testSmartTransferFundTerm(self):
        """Test SmartTransferFundTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

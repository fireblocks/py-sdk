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

from fireblocks.models.smart_transfer_not_found_response import (
    SmartTransferNotFoundResponse,
)


class TestSmartTransferNotFoundResponse(unittest.TestCase):
    """SmartTransferNotFoundResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTransferNotFoundResponse:
        """Test SmartTransferNotFoundResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SmartTransferNotFoundResponse`
        """
        model = SmartTransferNotFoundResponse()
        if include_optional:
            return SmartTransferNotFoundResponse(
                message = 'Requested entity not found',
                code = 'c943bdb8-ada0-4ba6-8645-74fcf188a10f'
            )
        else:
            return SmartTransferNotFoundResponse(
                message = 'Requested entity not found',
                code = 'c943bdb8-ada0-4ba6-8645-74fcf188a10f',
        )
        """

    def testSmartTransferNotFoundResponse(self):
        """Test SmartTransferNotFoundResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

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

from fireblocks.models.add_cosigner_response import AddCosignerResponse


class TestAddCosignerResponse(unittest.TestCase):
    """AddCosignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddCosignerResponse:
        """Test AddCosignerResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AddCosignerResponse`
        """
        model = AddCosignerResponse()
        if include_optional:
            return AddCosignerResponse(
                api_key_id = '123e4567-e89b-12d3-a456-426614174000',
                name = 'My Cosigner 1',
                existing_cosigner = False,
                pending_cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f'
            )
        else:
            return AddCosignerResponse(
                api_key_id = '123e4567-e89b-12d3-a456-426614174000',
                name = 'My Cosigner 1',
                pending_cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f',
        )
        """

    def testAddCosignerResponse(self):
        """Test AddCosignerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

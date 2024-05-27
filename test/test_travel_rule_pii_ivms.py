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

from fireblocks_client.models.travel_rule_pii_ivms import TravelRulePiiIVMS


class TestTravelRulePiiIVMS(unittest.TestCase):
    """TravelRulePiiIVMS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRulePiiIVMS:
        """Test TravelRulePiiIVMS
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRulePiiIVMS`
        """
        model = TravelRulePiiIVMS()
        if include_optional:
            return TravelRulePiiIVMS(
                full_name = '',
                date_of_birth = '',
                place_of_birth = '',
                address = '',
                identification_number = '',
                nationality = '',
                country_of_residence = '',
                tax_identification_number = '',
                customer_number = ''
            )
        else:
            return TravelRulePiiIVMS(
        )
        """

    def testTravelRulePiiIVMS(self):
        """Test TravelRulePiiIVMS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

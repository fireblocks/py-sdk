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

from fireblocks.models.travel_rule_natural_person_name_identifier import (
    TravelRuleNaturalPersonNameIdentifier,
)


class TestTravelRuleNaturalPersonNameIdentifier(unittest.TestCase):
    """TravelRuleNaturalPersonNameIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleNaturalPersonNameIdentifier:
        """Test TravelRuleNaturalPersonNameIdentifier
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleNaturalPersonNameIdentifier`
        """
        model = TravelRuleNaturalPersonNameIdentifier()
        if include_optional:
            return TravelRuleNaturalPersonNameIdentifier(
                name_identifier = [
                    fireblocks.models.travel_rule_natural_name_identifier.TravelRuleNaturalNameIdentifier(
                        primary_identifier = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', 
                        secondary_identifier = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', 
                        name_identifier_type = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', )
                    ],
                local_name_identifier = [
                    fireblocks.models.travel_rule_natural_name_identifier.TravelRuleNaturalNameIdentifier(
                        primary_identifier = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', 
                        secondary_identifier = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', 
                        name_identifier_type = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', )
                    ],
                phonetic_name_identifier = [
                    fireblocks.models.travel_rule_natural_name_identifier.TravelRuleNaturalNameIdentifier(
                        primary_identifier = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', 
                        secondary_identifier = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', 
                        name_identifier_type = 'QmP6wx8bx3SVNG3hd3SZKnS5pDjUan4y9H1VtyRqu7tsAv', )
                    ]
            )
        else:
            return TravelRuleNaturalPersonNameIdentifier(
        )
        """

    def testTravelRuleNaturalPersonNameIdentifier(self):
        """Test TravelRuleNaturalPersonNameIdentifier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

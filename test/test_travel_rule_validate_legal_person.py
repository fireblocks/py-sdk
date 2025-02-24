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

from fireblocks.models.travel_rule_validate_legal_person import (
    TravelRuleValidateLegalPerson,
)


class TestTravelRuleValidateLegalPerson(unittest.TestCase):
    """TravelRuleValidateLegalPerson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleValidateLegalPerson:
        """Test TravelRuleValidateLegalPerson
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleValidateLegalPerson`
        """
        model = TravelRuleValidateLegalPerson()
        if include_optional:
            return TravelRuleValidateLegalPerson(
                name = fireblocks.models.travel_rule_validate_legal_person_name_identifier.TravelRuleValidateLegalPersonNameIdentifier(
                    legal_person_name = 'Acme Corporation', 
                    legal_person_name_identifier_type = 'REGISTERED', ),
                geographic_address = [
                    fireblocks.models.travel_rule_validate_geographic_address.TravelRuleValidateGeographicAddress(
                        street_name = '123 Main St', 
                        town_name = 'New York', 
                        country = 'US', 
                        building_number = '123', 
                        post_code = '12345', 
                        address_type = 'HOME', 
                        department = 'IT', 
                        sub_department = 'Security', 
                        building_name = 'Acme Building', 
                        floor = '1', 
                        post_box = '123', 
                        room = '101', 
                        town_location_name = 'Downtown', 
                        district_name = 'Manhattan', 
                        country_sub_division = 'New York', 
                        address_line = ["123 Main St","New York","NY 12345"], )
                    ],
                national_identification = fireblocks.models.travel_rule_validate_national_identification.TravelRuleValidateNationalIdentification(
                    country_of_issue = 'US', 
                    national_identifier = '123456789', 
                    national_identifier_type = 'NATIONAL_ID', 
                    registration_authority = 'RA123456', ),
                customer_identification = 'CUST987654',
                customer_number = '123456789',
                country_of_registration = 'US'
            )
        else:
            return TravelRuleValidateLegalPerson(
        )
        """

    def testTravelRuleValidateLegalPerson(self):
        """Test TravelRuleValidateLegalPerson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

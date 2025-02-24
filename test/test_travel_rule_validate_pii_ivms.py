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

from fireblocks.models.travel_rule_validate_pii_ivms import TravelRuleValidatePiiIVMS


class TestTravelRuleValidatePiiIVMS(unittest.TestCase):
    """TravelRuleValidatePiiIVMS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleValidatePiiIVMS:
        """Test TravelRuleValidatePiiIVMS
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleValidatePiiIVMS`
        """
        model = TravelRuleValidatePiiIVMS()
        if include_optional:
            return TravelRuleValidatePiiIVMS(
                originator_persons = [
                    fireblocks.models.travel_rule_validate_person.TravelRuleValidatePerson(
                        natural_person = fireblocks.models.travel_rule_validate_natural_person.TravelRuleValidateNaturalPerson(
                            name = [
                                fireblocks.models.travel_rule_validate_natural_person_name_identifier.TravelRuleValidateNaturalPersonNameIdentifier(
                                    name_identifier = [
                                        fireblocks.models.travel_rule_validate_natural_name_identifier.TravelRuleValidateNaturalNameIdentifier(
                                            primary_identifier = 'John', 
                                            secondary_identifier = 'Doe', 
                                            name_identifier_type = 'LEGL', )
                                        ], 
                                    local_name_identifier = [
                                        fireblocks.models.travel_rule_validate_natural_name_identifier.TravelRuleValidateNaturalNameIdentifier(
                                            primary_identifier = 'John', 
                                            secondary_identifier = 'Doe', 
                                            name_identifier_type = 'LEGL', )
                                        ], 
                                    phonetic_name_identifier = [
                                        
                                        ], )
                                ], 
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
                            date_and_place_of_birth = fireblocks.models.travel_rule_validate_date_and_place_of_birth.TravelRuleValidateDateAndPlaceOfBirth(
                                date_of_birth = '1990-01-01', 
                                place_of_birth = 'New York, USA', ), 
                            customer_identification = 'CUST123456', 
                            country_of_residence = 'US', 
                            customer_number = '123456789', ), 
                        legal_person = fireblocks.models.travel_rule_validate_legal_person.TravelRuleValidateLegalPerson(
                            customer_identification = 'CUST987654', 
                            customer_number = '123456789', 
                            country_of_registration = 'US', ), )
                    ],
                beneficiary_persons = [
                    fireblocks.models.travel_rule_validate_person.TravelRuleValidatePerson(
                        natural_person = fireblocks.models.travel_rule_validate_natural_person.TravelRuleValidateNaturalPerson(
                            name = [
                                fireblocks.models.travel_rule_validate_natural_person_name_identifier.TravelRuleValidateNaturalPersonNameIdentifier(
                                    name_identifier = [
                                        fireblocks.models.travel_rule_validate_natural_name_identifier.TravelRuleValidateNaturalNameIdentifier(
                                            primary_identifier = 'John', 
                                            secondary_identifier = 'Doe', 
                                            name_identifier_type = 'LEGL', )
                                        ], 
                                    local_name_identifier = [
                                        fireblocks.models.travel_rule_validate_natural_name_identifier.TravelRuleValidateNaturalNameIdentifier(
                                            primary_identifier = 'John', 
                                            secondary_identifier = 'Doe', 
                                            name_identifier_type = 'LEGL', )
                                        ], 
                                    phonetic_name_identifier = [
                                        
                                        ], )
                                ], 
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
                            date_and_place_of_birth = fireblocks.models.travel_rule_validate_date_and_place_of_birth.TravelRuleValidateDateAndPlaceOfBirth(
                                date_of_birth = '1990-01-01', 
                                place_of_birth = 'New York, USA', ), 
                            customer_identification = 'CUST123456', 
                            country_of_residence = 'US', 
                            customer_number = '123456789', ), 
                        legal_person = fireblocks.models.travel_rule_validate_legal_person.TravelRuleValidateLegalPerson(
                            customer_identification = 'CUST987654', 
                            customer_number = '123456789', 
                            country_of_registration = 'US', ), )
                    ],
                account_number = [
                    ''
                    ]
            )
        else:
            return TravelRuleValidatePiiIVMS(
        )
        """

    def testTravelRuleValidatePiiIVMS(self):
        """Test TravelRuleValidatePiiIVMS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

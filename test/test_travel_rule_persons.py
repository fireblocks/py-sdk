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

from fireblocks.models.travel_rule_persons import TravelRulePersons


class TestTravelRulePersons(unittest.TestCase):
    """TravelRulePersons unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRulePersons:
        """Test TravelRulePersons
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRulePersons`
        """
        model = TravelRulePersons()
        if include_optional:
            return TravelRulePersons(
                natural_person = fireblocks.models.travel_rule_natural_person.TravelRuleNaturalPerson(
                    name = [
                        fireblocks.models.travel_rule_natural_person_name_identifier.TravelRuleNaturalPersonNameIdentifier(
                            name_identifier = [
                                fireblocks.models.travel_rule_natural_name_identifier.TravelRuleNaturalNameIdentifier()
                                ], 
                            local_name_identifier = [
                                fireblocks.models.travel_rule_natural_name_identifier.TravelRuleNaturalNameIdentifier()
                                ], 
                            phonetic_name_identifier = [
                                fireblocks.models.travel_rule_natural_name_identifier.TravelRuleNaturalNameIdentifier()
                                ], )
                        ], 
                    geographic_address = [
                        fireblocks.models.travel_rule_geographic_address.TravelRuleGeographicAddress(
                            street_name = '', 
                            town_name = '', 
                            country = '', 
                            building_number = '', 
                            post_code = '', 
                            address_type = '', 
                            department = '', 
                            sub_department = '', 
                            building_name = '', 
                            floor = '', 
                            post_box = '', 
                            room = '', 
                            town_location_name = '', 
                            district_name = '', 
                            country_sub_division = '', 
                            address_line = [
                                ''
                                ], )
                        ], 
                    national_identification = [
                        fireblocks.models.travel_rule_national_identification.TravelRuleNationalIdentification(
                            country_of_issue = '', 
                            national_identifier = '', 
                            national_identifier_type = '', 
                            registration_authority = '', )
                        ], 
                    date_and_place_of_birth = [
                        fireblocks.models.travel_rule_date_and_place_of_birth.TravelRuleDateAndPlaceOfBirth(
                            date_of_birth = '', 
                            place_of_birth = '', )
                        ], 
                    customer_identification = '', 
                    country_of_residence = '', 
                    customer_number = '', 
                    country_of_registration = '', ),
                legal_person = fireblocks.models.travel_rule_legal_person.TravelRuleLegalPerson(
                    name = fireblocks.models.name.name(), 
                    geographic_address = [
                        fireblocks.models.travel_rule_geographic_address.TravelRuleGeographicAddress(
                            street_name = '', 
                            town_name = '', 
                            country = '', 
                            building_number = '', 
                            post_code = '', 
                            address_type = '', 
                            department = '', 
                            sub_department = '', 
                            building_name = '', 
                            floor = '', 
                            post_box = '', 
                            room = '', 
                            town_location_name = '', 
                            district_name = '', 
                            country_sub_division = '', 
                            address_line = [
                                ''
                                ], )
                        ], 
                    national_identification = [
                        fireblocks.models.travel_rule_national_identification.TravelRuleNationalIdentification(
                            country_of_issue = '', 
                            national_identifier = '', 
                            national_identifier_type = '', 
                            registration_authority = '', )
                        ], 
                    customer_identification = '', 
                    customer_number = '', 
                    country_of_registration = '', )
            )
        else:
            return TravelRulePersons(
        )
        """

    def testTravelRulePersons(self):
        """Test TravelRulePersons"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

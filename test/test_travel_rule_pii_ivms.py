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

from fireblocks.models.travel_rule_pii_ivms import TravelRulePiiIVMS


class TestTravelRulePiiIVMS(unittest.TestCase):
    """TravelRulePiiIVMS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRulePiiIVMS:
        """Test TravelRulePiiIVMS
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRulePiiIVMS`
        """
        model = TravelRulePiiIVMS()
        if include_optional:
            return TravelRulePiiIVMS(
                originator_persons = [
                    fireblocks.models.travel_rule_person.TravelRulePerson(
                        natural_person = fireblocks.models.travel_rule_natural_person.TravelRuleNaturalPerson(
                            name = [
                                fireblocks.models.travel_rule_natural_person_name_identifier.TravelRuleNaturalPersonNameIdentifier(
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
                                        
                                        ], )
                                ], 
                            geographic_address = [
                                fireblocks.models.travel_rule_geographic_address.TravelRuleGeographicAddress(
                                    street_name = 'QmZGXXsKPk5iPS97LLjXB5e8Qs555ocdzcpbPMXvt84Ji9', 
                                    town_name = 'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt', 
                                    country = 'QmRGHdoxQfSi6tevyvaYGzs8BVStfqJqEyrMYqUfzXxkmm', 
                                    building_number = 'QmUFpNkxdsVtebDSUz5eP51kzoysXmqj2gBgeH11PD7SVP', 
                                    post_code = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', 
                                    address_type = 'Qmdr9LcChZsoivS6uAhe7Qk7cGLDAx73wBZTVvq4WoU71H', 
                                    department = 'QmN7fb65x5MyA7RKyhbXaUKvJ7U4Y9eqpEZTmJYpNyEG8', 
                                    sub_department = 'QmTkfyGh54tXNqFxyEGK9NyTJZYpQ6RZ9zpNykxykME8s', 
                                    building_name = 'QmXJfGk85t6RKyhbXaEK9Nz4MEeMKypq6EY9zpJyC9nM9', 
                                    floor = 'QmZP5G7fhZpMyQxXnT9KyR6ybXaEM9zpJy4ME9MkTJGE1', 
                                    post_box = 'QmTkfYRGK54xFqXyJYNZyE9kY9zpMKytJnXy5z9EME9sJ', 
                                    room = 'QmRYXnT9KyhbXaEMZpMyxMkZ9zpYNYTJ4ME5kCGE7fhMJ', 
                                    town_location_name = 'QmNpZTyXJXnT9K6EYZpQxYNYMkC5p4kGEfhnkMJzpYT9Jm', 
                                    district_name = 'QmT9p6ERKyNYXnTyhbpMYJ4zpYT9kMJZT9QmEMGZ5kMhCy', 
                                    country_sub_division = 'QmK9yTbXaZpMYJYTYp6NT9QmEMGZT9p9kMJfhyGE4Z7k5C', 
                                    address_line = ["QmNp9kMjfhGZ5kMJzpNYXZTy6NQmZYEMGZ4kZT9Y6pNYT"], )
                                ], 
                            national_identification = fireblocks.models.travel_rule_national_identification.TravelRuleNationalIdentification(
                                country_of_issue = 'QmRGHdoxQfSi6tevyvaYGzs8BVStfqJqEyrMYqUfzXxkmm', 
                                national_identifier = 'QmdR6qLnZ7Kwf5cBaXG8QFQenEvRg9JNZeoPranVuGd63z', 
                                national_identifier_type = 'QmUKTg3aFJFhMz1o9gPqA3MgTRwd2LvDLwWTPHYUoMEYVi', 
                                registration_authority = 'QmV9KJMyT9RJzpYfhME5xNCZ4G67fEkzTpRMyJzp9kTNYk', ), 
                            date_and_place_of_birth = fireblocks.models.travel_rule_date_and_place_of_birth.TravelRuleDateAndPlaceOfBirth(
                                date_of_birth = 'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt', 
                                place_of_birth = 'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt', ), 
                            customer_identification = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', 
                            country_of_residence = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', 
                            customer_number = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', ), 
                        legal_person = fireblocks.models.travel_rule_legal_person.TravelRuleLegalPerson(
                            customer_identification = 'QmRY9AA4Uit2JRTxDzfzshrJdTK86Kf5HriA3dXDnihDmy', 
                            customer_number = 'QmXvyML3AJUFpBbJqL5NVp7Vn7xNkuedTsSMk93duLCNW8', 
                            country_of_registration = 'QmeoTk6UPruEAYNbJEAHdQYc53ap9BXmpnPMcuvs8wutdr', ), )
                    ],
                beneficiary_persons = [
                    fireblocks.models.travel_rule_person.TravelRulePerson(
                        natural_person = fireblocks.models.travel_rule_natural_person.TravelRuleNaturalPerson(
                            name = [
                                fireblocks.models.travel_rule_natural_person_name_identifier.TravelRuleNaturalPersonNameIdentifier(
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
                                        
                                        ], )
                                ], 
                            geographic_address = [
                                fireblocks.models.travel_rule_geographic_address.TravelRuleGeographicAddress(
                                    street_name = 'QmZGXXsKPk5iPS97LLjXB5e8Qs555ocdzcpbPMXvt84Ji9', 
                                    town_name = 'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt', 
                                    country = 'QmRGHdoxQfSi6tevyvaYGzs8BVStfqJqEyrMYqUfzXxkmm', 
                                    building_number = 'QmUFpNkxdsVtebDSUz5eP51kzoysXmqj2gBgeH11PD7SVP', 
                                    post_code = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', 
                                    address_type = 'Qmdr9LcChZsoivS6uAhe7Qk7cGLDAx73wBZTVvq4WoU71H', 
                                    department = 'QmN7fb65x5MyA7RKyhbXaUKvJ7U4Y9eqpEZTmJYpNyEG8', 
                                    sub_department = 'QmTkfyGh54tXNqFxyEGK9NyTJZYpQ6RZ9zpNykxykME8s', 
                                    building_name = 'QmXJfGk85t6RKyhbXaEK9Nz4MEeMKypq6EY9zpJyC9nM9', 
                                    floor = 'QmZP5G7fhZpMyQxXnT9KyR6ybXaEM9zpJy4ME9MkTJGE1', 
                                    post_box = 'QmTkfYRGK54xFqXyJYNZyE9kY9zpMKytJnXy5z9EME9sJ', 
                                    room = 'QmRYXnT9KyhbXaEMZpMyxMkZ9zpYNYTJ4ME5kCGE7fhMJ', 
                                    town_location_name = 'QmNpZTyXJXnT9K6EYZpQxYNYMkC5p4kGEfhnkMJzpYT9Jm', 
                                    district_name = 'QmT9p6ERKyNYXnTyhbpMYJ4zpYT9kMJZT9QmEMGZ5kMhCy', 
                                    country_sub_division = 'QmK9yTbXaZpMYJYTYp6NT9QmEMGZT9p9kMJfhyGE4Z7k5C', 
                                    address_line = ["QmNp9kMjfhGZ5kMJzpNYXZTy6NQmZYEMGZ4kZT9Y6pNYT"], )
                                ], 
                            national_identification = fireblocks.models.travel_rule_national_identification.TravelRuleNationalIdentification(
                                country_of_issue = 'QmRGHdoxQfSi6tevyvaYGzs8BVStfqJqEyrMYqUfzXxkmm', 
                                national_identifier = 'QmdR6qLnZ7Kwf5cBaXG8QFQenEvRg9JNZeoPranVuGd63z', 
                                national_identifier_type = 'QmUKTg3aFJFhMz1o9gPqA3MgTRwd2LvDLwWTPHYUoMEYVi', 
                                registration_authority = 'QmV9KJMyT9RJzpYfhME5xNCZ4G67fEkzTpRMyJzp9kTNYk', ), 
                            date_and_place_of_birth = fireblocks.models.travel_rule_date_and_place_of_birth.TravelRuleDateAndPlaceOfBirth(
                                date_of_birth = 'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt', 
                                place_of_birth = 'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt', ), 
                            customer_identification = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', 
                            country_of_residence = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', 
                            customer_number = 'QmTJsK3sc3fPEVwvAp97UUiVoFhjzQhYX3sCda1JxuCnXj', ), 
                        legal_person = fireblocks.models.travel_rule_legal_person.TravelRuleLegalPerson(
                            customer_identification = 'QmRY9AA4Uit2JRTxDzfzshrJdTK86Kf5HriA3dXDnihDmy', 
                            customer_number = 'QmXvyML3AJUFpBbJqL5NVp7Vn7xNkuedTsSMk93duLCNW8', 
                            country_of_registration = 'QmeoTk6UPruEAYNbJEAHdQYc53ap9BXmpnPMcuvs8wutdr', ), )
                    ],
                account_number = [
                    'QmNkEt9VdnhjefQMXo3ZaZAs765ugoWiazaqcY9skHMjCt'
                    ]
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

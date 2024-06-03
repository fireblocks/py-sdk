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

from fireblocks.models.smart_transfer_create_ticket import SmartTransferCreateTicket


class TestSmartTransferCreateTicket(unittest.TestCase):
    """SmartTransferCreateTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTransferCreateTicket:
        """Test SmartTransferCreateTicket
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SmartTransferCreateTicket`
        """
        model = SmartTransferCreateTicket()
        if include_optional:
            return SmartTransferCreateTicket(
                created_by_network_id = '',
                type = 'ASYNC',
                expires_in = 1,
                terms = [
                    fireblocks.models.smart_transfer_create_ticket_term.SmartTransferCreateTicketTerm(
                        asset = 'BTC', 
                        amount = '133.789161216184', 
                        from_network_id = '947c6115-1f5f-4fb4-9fd6-a1f9dee14670', 
                        to_network_id = '5d009697-c29b-48e0-aff8-1f4305d19dc2', )
                    ],
                external_ref_id = '',
                note = '',
                submit = True
            )
        else:
            return SmartTransferCreateTicket(
                created_by_network_id = '',
                type = 'ASYNC',
        )
        """

    def testSmartTransferCreateTicket(self):
        """Test SmartTransferCreateTicket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

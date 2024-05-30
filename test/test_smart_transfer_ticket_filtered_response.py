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

from fireblocks_client.models.smart_transfer_ticket_filtered_response import (
    SmartTransferTicketFilteredResponse,
)


class TestSmartTransferTicketFilteredResponse(unittest.TestCase):
    """SmartTransferTicketFilteredResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTransferTicketFilteredResponse:
        """Test SmartTransferTicketFilteredResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SmartTransferTicketFilteredResponse`
        """
        model = SmartTransferTicketFilteredResponse()
        if include_optional:
            return SmartTransferTicketFilteredResponse(
                message = 'Success',
                after = '118320d2-761f-46c7-96cf-65e71a370b36',
                data = [
                    fireblocks_client.models.smart_transfer_ticket.SmartTransferTicket(
                        id = '118320d2-761f-46c7-96cf-65e71a370b36', 
                        type = 'ASYNC', 
                        direction = 'EXCHANGE', 
                        status = 'DRAFT', 
                        terms = [{"id":"84601ee2-b10f-4aa8-be9c-dba259a3533a","ticketId":"118320d2-761f-46c7-96cf-65e71a370b36","amount":"10.00","asset":"ETH","fromNetworkId":"947c6115-1f5f-4fb4-9fd6-a1f9dee14670","toNetworkId":"5d009697-c29b-48e0-aff8-1f4305d19dc2","status":"CREATED"},{"id":"84601ee2-b10f-4aa8-be9c-dba259a3533a","ticketId":"118320d2-761f-46c7-96cf-65e71a370b36","amount":"10.00","asset":"ETH","fromNetworkId":"947c6115-1f5f-4fb4-9fd6-a1f9dee14670","fromNetworkIdName":"Source network profile 1","toNetworkId":"5d009697-c29b-48e0-aff8-1f4305d19dc2","toNetworkIdName":"Destination network profile 1","status":"FUNDING","connectionId":"14817440-d5c8-4dbd-a754-ad415683610c","fbTxId":"79075e8c-1fd9-4c97-9575-3bd9229e5c0d","createdAt":"2023-03-01T11:23:00.000Z","updatedAt":"2023-03-01T11:23:00.000Z"},{"id":"84601ee2-b10f-4aa8-be9c-dba259a3533a","ticketId":"118320d2-761f-46c7-96cf-65e71a370b36","amount":"10.00","asset":"ETH","fromNetworkId":"947c6115-1f5f-4fb4-9fd6-a1f9dee14670","fromNetworkIdName":"Source network profile 2","toNetworkId":"5d009697-c29b-48e0-aff8-1f4305d19dc2","toNetworkIdName":"Destination network profile 2","status":"FUNDED","connectionId":"14817440-d5c8-4dbd-a754-ad415683610c","fbTxId":"79075e8c-1fd9-4c97-9575-3bd9229e5c0d","txHash":"0xb5c8bd9430b6cc87a0e2fe110ece6bf527fa4f170a4bc8cd032f768fc5219838","createdAt":"2023-03-01T11:23:00.000Z","updatedAt":"2023-03-01T11:23:00.000Z"}], 
                        expires_in = 13, 
                        expires_at = '2023-03-01T11:23Z', 
                        submitted_at = '2023-03-01T11:23Z', 
                        expired_at = '2023-03-01T11:23Z', 
                        canceled_at = '2023-03-01T11:23Z', 
                        fulfilled_at = '2023-03-01T11:23Z', 
                        external_ref_id = '2631ffb9d8fe47c6b0825b5be28297da', 
                        note = 'Random note', 
                        created_by_network_id = '3eaa94c5-128b-4835-bb08-3111bb6564c7', 
                        created_by_network_id_name = 'Network id name', 
                        canceled_by_network_id_name = 'Network id name', 
                        created_at = '2023-03-01T11:23Z', 
                        updated_at = '2023-03-01T11:23Z', 
                        canceled_by_me = True, 
                        created_by_me = True, )
                    ]
            )
        else:
            return SmartTransferTicketFilteredResponse(
                message = 'Success',
                after = '118320d2-761f-46c7-96cf-65e71a370b36',
                data = [
                    fireblocks_client.models.smart_transfer_ticket.SmartTransferTicket(
                        id = '118320d2-761f-46c7-96cf-65e71a370b36', 
                        type = 'ASYNC', 
                        direction = 'EXCHANGE', 
                        status = 'DRAFT', 
                        terms = [{"id":"84601ee2-b10f-4aa8-be9c-dba259a3533a","ticketId":"118320d2-761f-46c7-96cf-65e71a370b36","amount":"10.00","asset":"ETH","fromNetworkId":"947c6115-1f5f-4fb4-9fd6-a1f9dee14670","toNetworkId":"5d009697-c29b-48e0-aff8-1f4305d19dc2","status":"CREATED"},{"id":"84601ee2-b10f-4aa8-be9c-dba259a3533a","ticketId":"118320d2-761f-46c7-96cf-65e71a370b36","amount":"10.00","asset":"ETH","fromNetworkId":"947c6115-1f5f-4fb4-9fd6-a1f9dee14670","fromNetworkIdName":"Source network profile 1","toNetworkId":"5d009697-c29b-48e0-aff8-1f4305d19dc2","toNetworkIdName":"Destination network profile 1","status":"FUNDING","connectionId":"14817440-d5c8-4dbd-a754-ad415683610c","fbTxId":"79075e8c-1fd9-4c97-9575-3bd9229e5c0d","createdAt":"2023-03-01T11:23:00.000Z","updatedAt":"2023-03-01T11:23:00.000Z"},{"id":"84601ee2-b10f-4aa8-be9c-dba259a3533a","ticketId":"118320d2-761f-46c7-96cf-65e71a370b36","amount":"10.00","asset":"ETH","fromNetworkId":"947c6115-1f5f-4fb4-9fd6-a1f9dee14670","fromNetworkIdName":"Source network profile 2","toNetworkId":"5d009697-c29b-48e0-aff8-1f4305d19dc2","toNetworkIdName":"Destination network profile 2","status":"FUNDED","connectionId":"14817440-d5c8-4dbd-a754-ad415683610c","fbTxId":"79075e8c-1fd9-4c97-9575-3bd9229e5c0d","txHash":"0xb5c8bd9430b6cc87a0e2fe110ece6bf527fa4f170a4bc8cd032f768fc5219838","createdAt":"2023-03-01T11:23:00.000Z","updatedAt":"2023-03-01T11:23:00.000Z"}], 
                        expires_in = 13, 
                        expires_at = '2023-03-01T11:23Z', 
                        submitted_at = '2023-03-01T11:23Z', 
                        expired_at = '2023-03-01T11:23Z', 
                        canceled_at = '2023-03-01T11:23Z', 
                        fulfilled_at = '2023-03-01T11:23Z', 
                        external_ref_id = '2631ffb9d8fe47c6b0825b5be28297da', 
                        note = 'Random note', 
                        created_by_network_id = '3eaa94c5-128b-4835-bb08-3111bb6564c7', 
                        created_by_network_id_name = 'Network id name', 
                        canceled_by_network_id_name = 'Network id name', 
                        created_at = '2023-03-01T11:23Z', 
                        updated_at = '2023-03-01T11:23Z', 
                        canceled_by_me = True, 
                        created_by_me = True, )
                    ],
        )
        """

    def testSmartTransferTicketFilteredResponse(self):
        """Test SmartTransferTicketFilteredResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

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

from fireblocks.models.update_webhook_request import UpdateWebhookRequest


class TestUpdateWebhookRequest(unittest.TestCase):
    """UpdateWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWebhookRequest:
        """Test UpdateWebhookRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdateWebhookRequest`
        """
        model = UpdateWebhookRequest()
        if include_optional:
            return UpdateWebhookRequest(
                url = 'https://example.com/webhook',
                description = 'This webhook is used for transactions notifications',
                events = ["transaction.created","transaction.status.updated"],
                enabled = False
            )
        else:
            return UpdateWebhookRequest(
        )
        """

    def testUpdateWebhookRequest(self):
        """Test UpdateWebhookRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

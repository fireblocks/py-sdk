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

from fireblocks_client.models.job import Job


class TestJob(unittest.TestCase):
    """Job unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Job:
        """Test Job
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Job`
        """
        model = Job()
        if include_optional:
            return Job(
                id = '',
                tenant_id = '',
                type = '',
                user_id = '',
                created = 1.337,
                updated = 1.337,
                state = '',
                tasks = [
                    fireblocks_client.models.task.Task(
                        id = '', 
                        job_id = '', 
                        type = '', 
                        tenant_id = '', 
                        created = 1.337, 
                        updated = 1.337, 
                        state = '', )
                    ]
            )
        else:
            return Job(
        )
        """

    def testJob(self):
        """Test Job"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_role_application_request import CreateRoleApplicationRequest

class TestCreateRoleApplicationRequest(unittest.TestCase):
    """CreateRoleApplicationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRoleApplicationRequest:
        """Test CreateRoleApplicationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRoleApplicationRequest`
        """
        model = CreateRoleApplicationRequest()
        if include_optional:
            return CreateRoleApplicationRequest(
                application_ids = [
                    '0'
                    ]
            )
        else:
            return CreateRoleApplicationRequest(
                application_ids = [
                    '0'
                    ],
        )
        """

    def testCreateRoleApplicationRequest(self):
        """Test CreateRoleApplicationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_role_request import CreateRoleRequest

class TestCreateRoleRequest(unittest.TestCase):
    """CreateRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRoleRequest:
        """Test CreateRoleRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRoleRequest`
        """
        model = CreateRoleRequest()
        if include_optional:
            return CreateRoleRequest(
                tenant_id = '',
                name = '0',
                description = '0',
                type = 'User',
                is_default = True,
                scope_ids = [
                    '0'
                    ]
            )
        else:
            return CreateRoleRequest(
                name = '0',
                description = '0',
        )
        """

    def testCreateRoleRequest(self):
        """Test CreateRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

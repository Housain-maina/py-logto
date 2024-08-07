# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.replace_organization_role_resource_scopes_request import ReplaceOrganizationRoleResourceScopesRequest

class TestReplaceOrganizationRoleResourceScopesRequest(unittest.TestCase):
    """ReplaceOrganizationRoleResourceScopesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReplaceOrganizationRoleResourceScopesRequest:
        """Test ReplaceOrganizationRoleResourceScopesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReplaceOrganizationRoleResourceScopesRequest`
        """
        model = ReplaceOrganizationRoleResourceScopesRequest()
        if include_optional:
            return ReplaceOrganizationRoleResourceScopesRequest(
                scope_ids = [
                    '0'
                    ]
            )
        else:
            return ReplaceOrganizationRoleResourceScopesRequest(
                scope_ids = [
                    '0'
                    ],
        )
        """

    def testReplaceOrganizationRoleResourceScopesRequest(self):
        """Test ReplaceOrganizationRoleResourceScopesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

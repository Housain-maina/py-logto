# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource

class TestGetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource(unittest.TestCase):
    """GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource:
        """Test GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource`
        """
        model = GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource()
        if include_optional:
            return GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource(
                tenant_id = '',
                id = '0',
                name = '0',
                indicator = '0',
                is_default = True,
                access_token_ttl = 1.337
            )
        else:
            return GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource(
                tenant_id = '',
                id = '0',
                name = '0',
                indicator = '0',
                is_default = True,
                access_token_ttl = 1.337,
        )
        """

    def testGetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource(self):
        """Test GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

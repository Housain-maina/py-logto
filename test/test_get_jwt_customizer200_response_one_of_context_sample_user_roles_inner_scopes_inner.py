# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_roles_inner_scopes_inner import GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner

class TestGetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner(unittest.TestCase):
    """GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner:
        """Test GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner`
        """
        model = GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner()
        if include_optional:
            return GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner(
                id = '0',
                name = '0',
                description = '',
                resource_id = '0',
                resource = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                    tenant_id = '', 
                    id = '0', 
                    name = '0', 
                    indicator = '0', 
                    is_default = True, 
                    access_token_ttl = 1.337, )
            )
        else:
            return GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner(
                id = '0',
                name = '0',
                description = '',
                resource_id = '0',
                resource = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource.GetJwtCustomizer_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                    tenant_id = '', 
                    id = '0', 
                    name = '0', 
                    indicator = '0', 
                    is_default = True, 
                    access_token_ttl = 1.337, ),
        )
        """

    def testGetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner(self):
        """Test GetJwtCustomizer200ResponseOneOfContextSampleUserRolesInnerScopesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

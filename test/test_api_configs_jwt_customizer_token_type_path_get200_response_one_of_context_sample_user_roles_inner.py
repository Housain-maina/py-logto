# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_roles_inner import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner

class TestApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner(unittest.TestCase):
    """ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner:
        """Test ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner`
        """
        model = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner()
        if include_optional:
            return ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner(
                id = '0',
                name = '0',
                description = '0',
                scopes = [
                    py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner_scopes_inner._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner_scopes_inner(
                        id = '0', 
                        name = '0', 
                        description = '', 
                        resource_id = '0', 
                        resource = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', 
                            is_default = True, 
                            access_token_ttl = 1.337, ), )
                    ]
            )
        else:
            return ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner(
                id = '0',
                name = '0',
                description = '0',
                scopes = [
                    py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner_scopes_inner._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner_scopes_inner(
                        id = '0', 
                        name = '0', 
                        description = '', 
                        resource_id = '0', 
                        resource = py_logto.models._api_configs_jwt_customizer__token_type_path__get_200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource._api_configs_jwt_customizer__tokenTypePath__get_200_response_oneOf_contextSample_user_roles_inner_scopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', 
                            is_default = True, 
                            access_token_ttl = 1.337, ), )
                    ],
        )
        """

    def testApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner(self):
        """Test ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

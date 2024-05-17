# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response import ApiApplicationsApplicationIdUserConsentScopesGet200Response

class TestApiApplicationsApplicationIdUserConsentScopesGet200Response(unittest.TestCase):
    """ApiApplicationsApplicationIdUserConsentScopesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiApplicationsApplicationIdUserConsentScopesGet200Response:
        """Test ApiApplicationsApplicationIdUserConsentScopesGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiApplicationsApplicationIdUserConsentScopesGet200Response`
        """
        model = ApiApplicationsApplicationIdUserConsentScopesGet200Response()
        if include_optional:
            return ApiApplicationsApplicationIdUserConsentScopesGet200Response(
                organization_scopes = [
                    py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_organization_scopes_inner._api_applications__applicationId__user_consent_scopes_get_200_response_organizationScopes_inner(
                        id = '0', 
                        name = '0', 
                        description = '', )
                    ],
                resource_scopes = [
                    py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_resource_scopes_inner._api_applications__applicationId__user_consent_scopes_get_200_response_resourceScopes_inner(
                        resource = py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_resource_scopes_inner_resource._api_applications__applicationId__user_consent_scopes_get_200_response_resourceScopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', ), 
                        scopes = [
                            py_logto.models._api_interaction_consent_get_200_response_missing_resource_scopes_inner_scopes_inner._api_interaction_consent_get_200_response_missingResourceScopes_inner_scopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], )
                    ],
                user_scopes = [
                    'profile'
                    ]
            )
        else:
            return ApiApplicationsApplicationIdUserConsentScopesGet200Response(
                organization_scopes = [
                    py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_organization_scopes_inner._api_applications__applicationId__user_consent_scopes_get_200_response_organizationScopes_inner(
                        id = '0', 
                        name = '0', 
                        description = '', )
                    ],
                resource_scopes = [
                    py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_resource_scopes_inner._api_applications__applicationId__user_consent_scopes_get_200_response_resourceScopes_inner(
                        resource = py_logto.models._api_applications__application_id__user_consent_scopes_get_200_response_resource_scopes_inner_resource._api_applications__applicationId__user_consent_scopes_get_200_response_resourceScopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', ), 
                        scopes = [
                            py_logto.models._api_interaction_consent_get_200_response_missing_resource_scopes_inner_scopes_inner._api_interaction_consent_get_200_response_missingResourceScopes_inner_scopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], )
                    ],
                user_scopes = [
                    'profile'
                    ],
        )
        """

    def testApiApplicationsApplicationIdUserConsentScopesGet200Response(self):
        """Test ApiApplicationsApplicationIdUserConsentScopesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

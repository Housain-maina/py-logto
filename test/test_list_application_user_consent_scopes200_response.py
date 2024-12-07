# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_application_user_consent_scopes200_response import ListApplicationUserConsentScopes200Response

class TestListApplicationUserConsentScopes200Response(unittest.TestCase):
    """ListApplicationUserConsentScopes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplicationUserConsentScopes200Response:
        """Test ListApplicationUserConsentScopes200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplicationUserConsentScopes200Response`
        """
        model = ListApplicationUserConsentScopes200Response()
        if include_optional:
            return ListApplicationUserConsentScopes200Response(
                organization_scopes = [
                    py_logto.models.list_application_user_consent_scopes_200_response_organization_scopes_inner.ListApplicationUserConsentScopes_200_response_organizationScopes_inner(
                        id = '0', 
                        name = '0', 
                        description = '', )
                    ],
                resource_scopes = [
                    py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner(
                        resource = py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_resource.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', ), 
                        scopes = [
                            py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_scopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], )
                    ],
                organization_resource_scopes = [
                    py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner(
                        resource = py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_resource.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', ), 
                        scopes = [
                            py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_scopes_inner(
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
            return ListApplicationUserConsentScopes200Response(
                organization_scopes = [
                    py_logto.models.list_application_user_consent_scopes_200_response_organization_scopes_inner.ListApplicationUserConsentScopes_200_response_organizationScopes_inner(
                        id = '0', 
                        name = '0', 
                        description = '', )
                    ],
                resource_scopes = [
                    py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner(
                        resource = py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_resource.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', ), 
                        scopes = [
                            py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_scopes_inner(
                                id = '0', 
                                name = '0', 
                                description = '', )
                            ], )
                    ],
                organization_resource_scopes = [
                    py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner(
                        resource = py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_resource.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_resource(
                            id = '0', 
                            name = '0', 
                            indicator = '0', ), 
                        scopes = [
                            py_logto.models.list_application_user_consent_scopes_200_response_resource_scopes_inner_scopes_inner.ListApplicationUserConsentScopes_200_response_resourceScopes_inner_scopes_inner(
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

    def testListApplicationUserConsentScopes200Response(self):
        """Test ListApplicationUserConsentScopes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

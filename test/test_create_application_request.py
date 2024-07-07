# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_application_request import CreateApplicationRequest

class TestCreateApplicationRequest(unittest.TestCase):
    """CreateApplicationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateApplicationRequest:
        """Test CreateApplicationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateApplicationRequest`
        """
        model = CreateApplicationRequest()
        if include_optional:
            return CreateApplicationRequest(
                name = '0',
                description = '',
                type = 'Native',
                oidc_client_metadata = py_logto.models.list_applications_200_response_inner_oidc_client_metadata.ListApplications_200_response_inner_oidcClientMetadata(
                    redirect_uris = [
                        null
                        ], 
                    post_logout_redirect_uris = [
                        ''
                        ], 
                    backchannel_logout_uri = '', 
                    backchannel_logout_session_required = True, 
                    logo_uri = '', ),
                custom_client_metadata = py_logto.models.list_applications_200_response_inner_custom_client_metadata.ListApplications_200_response_inner_customClientMetadata(
                    cors_allowed_origins = [
                        '0'
                        ], 
                    id_token_ttl = 1.337, 
                    refresh_token_ttl = 1.337, 
                    refresh_token_ttl_in_days = 1.337, 
                    tenant_id = '', 
                    always_issue_refresh_token = True, 
                    rotate_refresh_token = True, ),
                is_third_party = True,
                protected_app_metadata = py_logto.models.create_application_request_protected_app_metadata.CreateApplication_request_protectedAppMetadata(
                    sub_domain = '', 
                    origin = '', )
            )
        else:
            return CreateApplicationRequest(
                name = '0',
                type = 'Native',
        )
        """

    def testCreateApplicationRequest(self):
        """Test CreateApplicationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
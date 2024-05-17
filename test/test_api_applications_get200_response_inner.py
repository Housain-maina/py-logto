# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_applications_get200_response_inner import ApiApplicationsGet200ResponseInner

class TestApiApplicationsGet200ResponseInner(unittest.TestCase):
    """ApiApplicationsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiApplicationsGet200ResponseInner:
        """Test ApiApplicationsGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiApplicationsGet200ResponseInner`
        """
        model = ApiApplicationsGet200ResponseInner()
        if include_optional:
            return ApiApplicationsGet200ResponseInner(
                id = '0',
                name = '0',
                secret = '0',
                description = '',
                type = 'Native',
                oidc_client_metadata = py_logto.models._api_applications_get_200_response_inner_oidc_client_metadata._api_applications_get_200_response_inner_oidcClientMetadata(
                    redirect_uris = [
                        null
                        ], 
                    post_logout_redirect_uris = [
                        ''
                        ], 
                    logo_uri = '', ),
                custom_client_metadata = py_logto.models._api_applications_get_200_response_inner_custom_client_metadata._api_applications_get_200_response_inner_customClientMetadata(
                    cors_allowed_origins = [
                        '0'
                        ], 
                    id_token_ttl = 1.337, 
                    refresh_token_ttl = 1.337, 
                    refresh_token_ttl_in_days = 1.337, 
                    always_issue_refresh_token = True, 
                    rotate_refresh_token = True, ),
                protected_app_metadata = py_logto.models._api_applications_get_200_response_inner_protected_app_metadata._api_applications_get_200_response_inner_protectedAppMetadata(
                    host = '', 
                    origin = '', 
                    session_duration = 1.337, 
                    page_rules = [
                        py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_page_rules_inner._api_applications_get_200_response_inner_protectedAppMetadata_pageRules_inner(
                            path = '', )
                        ], 
                    custom_domains = [
                        py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner(
                            domain = '', 
                            status = 'PendingVerification', 
                            error_message = '', 
                            dns_records = [
                                py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_dns_records_inner._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_dnsRecords_inner(
                                    name = '', 
                                    type = '', 
                                    value = '', )
                                ], 
                            cloudflare_data = py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData(
                                id = '', 
                                status = '', 
                                ssl = py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl(
                                    status = '', 
                                    validation_errors = [
                                        py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl_validation_errors_inner._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl_validation_errors_inner(
                                            message = '', )
                                        ], ), 
                                verification_errors = [
                                    ''
                                    ], ), )
                        ], ),
                is_third_party = True,
                created_at = 1.337
            )
        else:
            return ApiApplicationsGet200ResponseInner(
                id = '0',
                name = '0',
                secret = '0',
                description = '',
                type = 'Native',
                oidc_client_metadata = py_logto.models._api_applications_get_200_response_inner_oidc_client_metadata._api_applications_get_200_response_inner_oidcClientMetadata(
                    redirect_uris = [
                        null
                        ], 
                    post_logout_redirect_uris = [
                        ''
                        ], 
                    logo_uri = '', ),
                custom_client_metadata = py_logto.models._api_applications_get_200_response_inner_custom_client_metadata._api_applications_get_200_response_inner_customClientMetadata(
                    cors_allowed_origins = [
                        '0'
                        ], 
                    id_token_ttl = 1.337, 
                    refresh_token_ttl = 1.337, 
                    refresh_token_ttl_in_days = 1.337, 
                    always_issue_refresh_token = True, 
                    rotate_refresh_token = True, ),
                protected_app_metadata = py_logto.models._api_applications_get_200_response_inner_protected_app_metadata._api_applications_get_200_response_inner_protectedAppMetadata(
                    host = '', 
                    origin = '', 
                    session_duration = 1.337, 
                    page_rules = [
                        py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_page_rules_inner._api_applications_get_200_response_inner_protectedAppMetadata_pageRules_inner(
                            path = '', )
                        ], 
                    custom_domains = [
                        py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner(
                            domain = '', 
                            status = 'PendingVerification', 
                            error_message = '', 
                            dns_records = [
                                py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_dns_records_inner._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_dnsRecords_inner(
                                    name = '', 
                                    type = '', 
                                    value = '', )
                                ], 
                            cloudflare_data = py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData(
                                id = '', 
                                status = '', 
                                ssl = py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl(
                                    status = '', 
                                    validation_errors = [
                                        py_logto.models._api_applications_get_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl_validation_errors_inner._api_applications_get_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl_validation_errors_inner(
                                            message = '', )
                                        ], ), 
                                verification_errors = [
                                    ''
                                    ], ), )
                        ], ),
                is_third_party = True,
                created_at = 1.337,
        )
        """

    def testApiApplicationsGet200ResponseInner(self):
        """Test ApiApplicationsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

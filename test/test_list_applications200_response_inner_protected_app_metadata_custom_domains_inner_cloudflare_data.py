# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_applications200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data import ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData

class TestListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData(unittest.TestCase):
    """ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData:
        """Test ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData`
        """
        model = ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData()
        if include_optional:
            return ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData(
                id = '',
                status = '',
                ssl = py_logto.models.list_applications_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl.ListApplications_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl(
                    status = '', 
                    validation_errors = [
                        py_logto.models.list_applications_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl_validation_errors_inner.ListApplications_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl_validation_errors_inner(
                            message = '', )
                        ], ),
                verification_errors = [
                    ''
                    ]
            )
        else:
            return ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData(
                id = '',
                status = '',
                ssl = py_logto.models.list_applications_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl.ListApplications_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl(
                    status = '', 
                    validation_errors = [
                        py_logto.models.list_applications_200_response_inner_protected_app_metadata_custom_domains_inner_cloudflare_data_ssl_validation_errors_inner.ListApplications_200_response_inner_protectedAppMetadata_customDomains_inner_cloudflareData_ssl_validation_errors_inner(
                            message = '', )
                        ], ),
        )
        """

    def testListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData(self):
        """Test ListApplications200ResponseInnerProtectedAppMetadataCustomDomainsInnerCloudflareData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

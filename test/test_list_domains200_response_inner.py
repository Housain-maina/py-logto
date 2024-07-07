# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_domains200_response_inner import ListDomains200ResponseInner

class TestListDomains200ResponseInner(unittest.TestCase):
    """ListDomains200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDomains200ResponseInner:
        """Test ListDomains200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDomains200ResponseInner`
        """
        model = ListDomains200ResponseInner()
        if include_optional:
            return ListDomains200ResponseInner(
                id = '0',
                domain = '0',
                status = 'PendingVerification',
                error_message = '',
                dns_records = [
                    py_logto.models.list_applications_200_response_inner_protected_app_metadata_custom_domains_inner_dns_records_inner.ListApplications_200_response_inner_protectedAppMetadata_customDomains_inner_dnsRecords_inner(
                        name = '', 
                        type = '', 
                        value = '', )
                    ]
            )
        else:
            return ListDomains200ResponseInner(
                id = '0',
                domain = '0',
                status = 'PendingVerification',
                error_message = '',
                dns_records = [
                    py_logto.models.list_applications_200_response_inner_protected_app_metadata_custom_domains_inner_dns_records_inner.ListApplications_200_response_inner_protectedAppMetadata_customDomains_inner_dnsRecords_inner(
                        name = '', 
                        type = '', 
                        value = '', )
                    ],
        )
        """

    def testListDomains200ResponseInner(self):
        """Test ListDomains200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_applications200_response_inner_oidc_client_metadata_redirect_uris_inner import ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner

class TestListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner(unittest.TestCase):
    """ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner:
        """Test ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner`
        """
        model = ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner()
        if include_optional:
            return ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner(
            )
        else:
            return ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner(
        )
        """

    def testListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner(self):
        """Test ListApplications200ResponseInnerOidcClientMetadataRedirectUrisInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

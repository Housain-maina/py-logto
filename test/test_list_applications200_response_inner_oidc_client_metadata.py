# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_applications200_response_inner_oidc_client_metadata import ListApplications200ResponseInnerOidcClientMetadata

class TestListApplications200ResponseInnerOidcClientMetadata(unittest.TestCase):
    """ListApplications200ResponseInnerOidcClientMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplications200ResponseInnerOidcClientMetadata:
        """Test ListApplications200ResponseInnerOidcClientMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplications200ResponseInnerOidcClientMetadata`
        """
        model = ListApplications200ResponseInnerOidcClientMetadata()
        if include_optional:
            return ListApplications200ResponseInnerOidcClientMetadata(
                redirect_uris = [
                    null
                    ],
                post_logout_redirect_uris = [
                    ''
                    ],
                backchannel_logout_uri = '',
                backchannel_logout_session_required = True,
                logo_uri = ''
            )
        else:
            return ListApplications200ResponseInnerOidcClientMetadata(
                redirect_uris = [
                    null
                    ],
                post_logout_redirect_uris = [
                    ''
                    ],
        )
        """

    def testListApplications200ResponseInnerOidcClientMetadata(self):
        """Test ListApplications200ResponseInnerOidcClientMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
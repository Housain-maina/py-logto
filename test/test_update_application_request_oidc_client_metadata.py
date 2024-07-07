# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_application_request_oidc_client_metadata import UpdateApplicationRequestOidcClientMetadata

class TestUpdateApplicationRequestOidcClientMetadata(unittest.TestCase):
    """UpdateApplicationRequestOidcClientMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateApplicationRequestOidcClientMetadata:
        """Test UpdateApplicationRequestOidcClientMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateApplicationRequestOidcClientMetadata`
        """
        model = UpdateApplicationRequestOidcClientMetadata()
        if include_optional:
            return UpdateApplicationRequestOidcClientMetadata(
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
            return UpdateApplicationRequestOidcClientMetadata(
        )
        """

    def testUpdateApplicationRequestOidcClientMetadata(self):
        """Test UpdateApplicationRequestOidcClientMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

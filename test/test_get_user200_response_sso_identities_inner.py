# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_user200_response_sso_identities_inner import GetUser200ResponseSsoIdentitiesInner

class TestGetUser200ResponseSsoIdentitiesInner(unittest.TestCase):
    """GetUser200ResponseSsoIdentitiesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUser200ResponseSsoIdentitiesInner:
        """Test GetUser200ResponseSsoIdentitiesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUser200ResponseSsoIdentitiesInner`
        """
        model = GetUser200ResponseSsoIdentitiesInner()
        if include_optional:
            return GetUser200ResponseSsoIdentitiesInner(
                tenant_id = '',
                id = '0',
                user_id = '0',
                issuer = '0',
                identity_id = '0',
                detail = None,
                created_at = 1.337,
                sso_connector_id = '0'
            )
        else:
            return GetUser200ResponseSsoIdentitiesInner(
                tenant_id = '',
                id = '0',
                user_id = '0',
                issuer = '0',
                identity_id = '0',
                detail = None,
                created_at = 1.337,
                sso_connector_id = '0',
        )
        """

    def testGetUser200ResponseSsoIdentitiesInner(self):
        """Test GetUser200ResponseSsoIdentitiesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

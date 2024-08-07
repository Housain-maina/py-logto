# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_jwt_customizer200_response_one_of_token_sample import GetJwtCustomizer200ResponseOneOfTokenSample

class TestGetJwtCustomizer200ResponseOneOfTokenSample(unittest.TestCase):
    """GetJwtCustomizer200ResponseOneOfTokenSample unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetJwtCustomizer200ResponseOneOfTokenSample:
        """Test GetJwtCustomizer200ResponseOneOfTokenSample
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetJwtCustomizer200ResponseOneOfTokenSample`
        """
        model = GetJwtCustomizer200ResponseOneOfTokenSample()
        if include_optional:
            return GetJwtCustomizer200ResponseOneOfTokenSample(
                jti = '',
                aud = None,
                scope = '',
                client_id = '',
                account_id = '',
                expires_with_session = True,
                grant_id = '',
                gty = '',
                session_uid = '',
                sid = '',
                kind = ''
            )
        else:
            return GetJwtCustomizer200ResponseOneOfTokenSample(
        )
        """

    def testGetJwtCustomizer200ResponseOneOfTokenSample(self):
        """Test GetJwtCustomizer200ResponseOneOfTokenSample"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

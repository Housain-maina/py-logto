# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_jwt_customizer200_response_one_of_context_sample_user_sso_identities_inner import GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner

class TestGetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner(unittest.TestCase):
    """GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner:
        """Test GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner`
        """
        model = GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner()
        if include_optional:
            return GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner(
                issuer = '0',
                identity_id = '0',
                detail = None
            )
        else:
            return GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner(
                issuer = '0',
                identity_id = '0',
                detail = None,
        )
        """

    def testGetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner(self):
        """Test GetJwtCustomizer200ResponseOneOfContextSampleUserSsoIdentitiesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

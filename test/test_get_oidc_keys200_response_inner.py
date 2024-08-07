# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_oidc_keys200_response_inner import GetOidcKeys200ResponseInner

class TestGetOidcKeys200ResponseInner(unittest.TestCase):
    """GetOidcKeys200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOidcKeys200ResponseInner:
        """Test GetOidcKeys200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOidcKeys200ResponseInner`
        """
        model = GetOidcKeys200ResponseInner()
        if include_optional:
            return GetOidcKeys200ResponseInner(
                id = '',
                created_at = 1.337,
                signing_key_algorithm = 'RSA'
            )
        else:
            return GetOidcKeys200ResponseInner(
                id = '',
                created_at = 1.337,
        )
        """

    def testGetOidcKeys200ResponseInner(self):
        """Test GetOidcKeys200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

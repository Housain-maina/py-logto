# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.api.authn_api import AuthnApi


class TestAuthnApi(unittest.TestCase):
    """AuthnApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthnApi()

    def tearDown(self) -> None:
        pass

    def test_assert_saml(self) -> None:
        """Test case for assert_saml

        SAML ACS endpoint (social)
        """
        pass

    def test_assert_single_sign_on_saml(self) -> None:
        """Test case for assert_single_sign_on_saml

        SAML ACS endpoint (SSO)
        """
        pass

    def test_get_hasura_auth(self) -> None:
        """Test case for get_hasura_auth

        Hasura auth hook endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_user_mfa_verification_request import CreateUserMfaVerificationRequest

class TestCreateUserMfaVerificationRequest(unittest.TestCase):
    """CreateUserMfaVerificationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUserMfaVerificationRequest:
        """Test CreateUserMfaVerificationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUserMfaVerificationRequest`
        """
        model = CreateUserMfaVerificationRequest()
        if include_optional:
            return CreateUserMfaVerificationRequest(
                type = None
            )
        else:
            return CreateUserMfaVerificationRequest(
                type = None,
        )
        """

    def testCreateUserMfaVerificationRequest(self):
        """Test CreateUserMfaVerificationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

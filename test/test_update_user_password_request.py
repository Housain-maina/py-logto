# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_user_password_request import UpdateUserPasswordRequest

class TestUpdateUserPasswordRequest(unittest.TestCase):
    """UpdateUserPasswordRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserPasswordRequest:
        """Test UpdateUserPasswordRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserPasswordRequest`
        """
        model = UpdateUserPasswordRequest()
        if include_optional:
            return UpdateUserPasswordRequest(
                password = '0'
            )
        else:
            return UpdateUserPasswordRequest(
                password = '0',
        )
        """

    def testUpdateUserPasswordRequest(self):
        """Test UpdateUserPasswordRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

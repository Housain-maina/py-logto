# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.add_user_profile_request_one_of1 import AddUserProfileRequestOneOf1

class TestAddUserProfileRequestOneOf1(unittest.TestCase):
    """AddUserProfileRequestOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddUserProfileRequestOneOf1:
        """Test AddUserProfileRequestOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddUserProfileRequestOneOf1`
        """
        model = AddUserProfileRequestOneOf1()
        if include_optional:
            return AddUserProfileRequestOneOf1(
                type = '',
                value = ''
            )
        else:
            return AddUserProfileRequestOneOf1(
                type = '',
                value = '',
        )
        """

    def testAddUserProfileRequestOneOf1(self):
        """Test AddUserProfileRequestOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

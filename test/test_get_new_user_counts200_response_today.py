# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_new_user_counts200_response_today import GetNewUserCounts200ResponseToday

class TestGetNewUserCounts200ResponseToday(unittest.TestCase):
    """GetNewUserCounts200ResponseToday unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNewUserCounts200ResponseToday:
        """Test GetNewUserCounts200ResponseToday
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNewUserCounts200ResponseToday`
        """
        model = GetNewUserCounts200ResponseToday()
        if include_optional:
            return GetNewUserCounts200ResponseToday(
                count = 1.337,
                delta = 1.337
            )
        else:
            return GetNewUserCounts200ResponseToday(
                count = 1.337,
                delta = 1.337,
        )
        """

    def testGetNewUserCounts200ResponseToday(self):
        """Test GetNewUserCounts200ResponseToday"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

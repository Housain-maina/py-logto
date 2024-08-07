# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_sign_in_exp200_response_language_info import UpdateSignInExp200ResponseLanguageInfo

class TestUpdateSignInExp200ResponseLanguageInfo(unittest.TestCase):
    """UpdateSignInExp200ResponseLanguageInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSignInExp200ResponseLanguageInfo:
        """Test UpdateSignInExp200ResponseLanguageInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSignInExp200ResponseLanguageInfo`
        """
        model = UpdateSignInExp200ResponseLanguageInfo()
        if include_optional:
            return UpdateSignInExp200ResponseLanguageInfo(
                auto_detect = True,
                fallback_language = 'af-ZA'
            )
        else:
            return UpdateSignInExp200ResponseLanguageInfo(
                auto_detect = True,
                fallback_language = 'af-ZA',
        )
        """

    def testUpdateSignInExp200ResponseLanguageInfo(self):
        """Test UpdateSignInExp200ResponseLanguageInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

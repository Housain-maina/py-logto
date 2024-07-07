# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.get_sign_in_experience_config200_response_sso_connectors_inner import GetSignInExperienceConfig200ResponseSsoConnectorsInner

class TestGetSignInExperienceConfig200ResponseSsoConnectorsInner(unittest.TestCase):
    """GetSignInExperienceConfig200ResponseSsoConnectorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSignInExperienceConfig200ResponseSsoConnectorsInner:
        """Test GetSignInExperienceConfig200ResponseSsoConnectorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSignInExperienceConfig200ResponseSsoConnectorsInner`
        """
        model = GetSignInExperienceConfig200ResponseSsoConnectorsInner()
        if include_optional:
            return GetSignInExperienceConfig200ResponseSsoConnectorsInner(
                id = '',
                connector_name = '',
                logo = '',
                dark_logo = ''
            )
        else:
            return GetSignInExperienceConfig200ResponseSsoConnectorsInner(
                id = '',
                connector_name = '',
                logo = '',
        )
        """

    def testGetSignInExperienceConfig200ResponseSsoConnectorsInner(self):
        """Test GetSignInExperienceConfig200ResponseSsoConnectorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
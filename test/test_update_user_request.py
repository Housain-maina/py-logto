# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_user_request import UpdateUserRequest

class TestUpdateUserRequest(unittest.TestCase):
    """UpdateUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserRequest:
        """Test UpdateUserRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserRequest`
        """
        model = UpdateUserRequest()
        if include_optional:
            return UpdateUserRequest(
                username = None,
                primary_email = None,
                primary_phone = None,
                name = None,
                avatar = None,
                custom_data = None,
                profile = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_profile.GetJwtCustomizer_200_response_oneOf_contextSample_user_profile(
                    family_name = '', 
                    given_name = '', 
                    middle_name = '', 
                    nickname = '', 
                    preferred_username = '', 
                    profile = '', 
                    website = '', 
                    gender = '', 
                    birthdate = '', 
                    zoneinfo = '', 
                    locale = '', 
                    address = py_logto.models.get_jwt_customizer_200_response_one_of_context_sample_user_profile_address.GetJwtCustomizer_200_response_oneOf_contextSample_user_profile_address(
                        formatted = '', 
                        street_address = '', 
                        locality = '', 
                        region = '', 
                        postal_code = '', 
                        country = '', ), )
            )
        else:
            return UpdateUserRequest(
        )
        """

    def testUpdateUserRequest(self):
        """Test UpdateUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

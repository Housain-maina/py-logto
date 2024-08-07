# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.update_sign_in_exp_request_color import UpdateSignInExpRequestColor

class TestUpdateSignInExpRequestColor(unittest.TestCase):
    """UpdateSignInExpRequestColor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSignInExpRequestColor:
        """Test UpdateSignInExpRequestColor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSignInExpRequestColor`
        """
        model = UpdateSignInExpRequestColor()
        if include_optional:
            return UpdateSignInExpRequestColor(
                primary_color = '#bf3',
                is_dark_mode_enabled = True,
                dark_primary_color = '#bf3'
            )
        else:
            return UpdateSignInExpRequestColor(
                primary_color = '#bf3',
                is_dark_mode_enabled = True,
                dark_primary_color = '#bf3',
        )
        """

    def testUpdateSignInExpRequestColor(self):
        """Test UpdateSignInExpRequestColor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

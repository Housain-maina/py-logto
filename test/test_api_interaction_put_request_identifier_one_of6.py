# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_put_request_identifier_one_of6 import ApiInteractionPutRequestIdentifierOneOf6

class TestApiInteractionPutRequestIdentifierOneOf6(unittest.TestCase):
    """ApiInteractionPutRequestIdentifierOneOf6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionPutRequestIdentifierOneOf6:
        """Test ApiInteractionPutRequestIdentifierOneOf6
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionPutRequestIdentifierOneOf6`
        """
        model = ApiInteractionPutRequestIdentifierOneOf6()
        if include_optional:
            return ApiInteractionPutRequestIdentifierOneOf6(
                connector_id = '',
                email = ''
            )
        else:
            return ApiInteractionPutRequestIdentifierOneOf6(
                connector_id = '',
                email = '',
        )
        """

    def testApiInteractionPutRequestIdentifierOneOf6(self):
        """Test ApiInteractionPutRequestIdentifierOneOf6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

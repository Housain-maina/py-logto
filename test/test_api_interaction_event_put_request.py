# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.api_interaction_event_put_request import ApiInteractionEventPutRequest

class TestApiInteractionEventPutRequest(unittest.TestCase):
    """ApiInteractionEventPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInteractionEventPutRequest:
        """Test ApiInteractionEventPutRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInteractionEventPutRequest`
        """
        model = ApiInteractionEventPutRequest()
        if include_optional:
            return ApiInteractionEventPutRequest(
                event = 'SignIn'
            )
        else:
            return ApiInteractionEventPutRequest(
                event = 'SignIn',
        )
        """

    def testApiInteractionEventPutRequest(self):
        """Test ApiInteractionEventPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

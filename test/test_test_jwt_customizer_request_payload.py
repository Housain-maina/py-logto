# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.test_jwt_customizer_request_payload import TestJwtCustomizerRequestPayload

class TestTestJwtCustomizerRequestPayload(unittest.TestCase):
    """TestJwtCustomizerRequestPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestJwtCustomizerRequestPayload:
        """Test TestJwtCustomizerRequestPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestJwtCustomizerRequestPayload`
        """
        model = TestJwtCustomizerRequestPayload()
        if include_optional:
            return TestJwtCustomizerRequestPayload(
                script = None,
                environment_variables = None,
                context_sample = None,
                token_sample = None
            )
        else:
            return TestJwtCustomizerRequestPayload(
        )
        """

    def testTestJwtCustomizerRequestPayload(self):
        """Test TestJwtCustomizerRequestPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

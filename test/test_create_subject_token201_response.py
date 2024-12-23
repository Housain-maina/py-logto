# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.create_subject_token201_response import CreateSubjectToken201Response

class TestCreateSubjectToken201Response(unittest.TestCase):
    """CreateSubjectToken201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSubjectToken201Response:
        """Test CreateSubjectToken201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubjectToken201Response`
        """
        model = CreateSubjectToken201Response()
        if include_optional:
            return CreateSubjectToken201Response(
                subject_token = '',
                expires_in = 1.337
            )
        else:
            return CreateSubjectToken201Response(
                subject_token = '',
                expires_in = 1.337,
        )
        """

    def testCreateSubjectToken201Response(self):
        """Test CreateSubjectToken201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_logs200_response_inner_payload_error import ListLogs200ResponseInnerPayloadError

class TestListLogs200ResponseInnerPayloadError(unittest.TestCase):
    """ListLogs200ResponseInnerPayloadError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListLogs200ResponseInnerPayloadError:
        """Test ListLogs200ResponseInnerPayloadError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListLogs200ResponseInnerPayloadError`
        """
        model = ListLogs200ResponseInnerPayloadError()
        if include_optional:
            return ListLogs200ResponseInnerPayloadError(
            )
        else:
            return ListLogs200ResponseInnerPayloadError(
        )
        """

    def testListLogs200ResponseInnerPayloadError(self):
        """Test ListLogs200ResponseInnerPayloadError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

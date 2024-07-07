# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from py_logto.models.list_logs200_response_inner import ListLogs200ResponseInner

class TestListLogs200ResponseInner(unittest.TestCase):
    """ListLogs200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListLogs200ResponseInner:
        """Test ListLogs200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListLogs200ResponseInner`
        """
        model = ListLogs200ResponseInner()
        if include_optional:
            return ListLogs200ResponseInner(
                tenant_id = '',
                id = '0',
                key = '0',
                payload = py_logto.models.list_logs_200_response_inner_payload.ListLogs_200_response_inner_payload(
                    key = '', 
                    result = 'Success', 
                    error = null, 
                    ip = '', 
                    user_agent = '', 
                    user_id = '', 
                    application_id = '', 
                    session_id = '', ),
                created_at = 1.337
            )
        else:
            return ListLogs200ResponseInner(
                tenant_id = '',
                id = '0',
                key = '0',
                payload = py_logto.models.list_logs_200_response_inner_payload.ListLogs_200_response_inner_payload(
                    key = '', 
                    result = 'Success', 
                    error = null, 
                    ip = '', 
                    user_agent = '', 
                    user_id = '', 
                    application_id = '', 
                    session_id = '', ),
                created_at = 1.337,
        )
        """

    def testListLogs200ResponseInner(self):
        """Test ListLogs200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
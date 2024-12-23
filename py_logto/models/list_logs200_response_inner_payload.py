# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_logto.models.list_logs200_response_inner_payload_error import ListLogs200ResponseInnerPayloadError
from typing import Optional, Set
from typing_extensions import Self

class ListLogs200ResponseInnerPayload(BaseModel):
    """
    ListLogs200ResponseInnerPayload
    """ # noqa: E501
    key: StrictStr
    result: StrictStr
    error: Optional[ListLogs200ResponseInnerPayloadError] = None
    ip: Optional[StrictStr] = None
    user_agent: Optional[StrictStr] = Field(default=None, alias="userAgent")
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    application_id: Optional[StrictStr] = Field(default=None, alias="applicationId")
    session_id: Optional[StrictStr] = Field(default=None, alias="sessionId")
    params: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["key", "result", "error", "ip", "userAgent", "userId", "applicationId", "sessionId", "params"]

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Success', 'Error']):
            raise ValueError("must be one of enum values ('Success', 'Error')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListLogs200ResponseInnerPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListLogs200ResponseInnerPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": obj.get("key"),
            "result": obj.get("result"),
            "error": ListLogs200ResponseInnerPayloadError.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "ip": obj.get("ip"),
            "userAgent": obj.get("userAgent"),
            "userId": obj.get("userId"),
            "applicationId": obj.get("applicationId"),
            "sessionId": obj.get("sessionId"),
            "params": obj.get("params")
        })
        return _obj



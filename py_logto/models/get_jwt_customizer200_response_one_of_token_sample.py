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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_logto.models.get_jwt_customizer200_response_one_of_token_sample_aud import GetJwtCustomizer200ResponseOneOfTokenSampleAud
from typing import Optional, Set
from typing_extensions import Self

class GetJwtCustomizer200ResponseOneOfTokenSample(BaseModel):
    """
    GetJwtCustomizer200ResponseOneOfTokenSample
    """ # noqa: E501
    jti: Optional[StrictStr] = None
    aud: Optional[GetJwtCustomizer200ResponseOneOfTokenSampleAud] = None
    scope: Optional[StrictStr] = None
    client_id: Optional[StrictStr] = Field(default=None, alias="clientId")
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    expires_with_session: Optional[StrictBool] = Field(default=None, alias="expiresWithSession")
    grant_id: Optional[StrictStr] = Field(default=None, alias="grantId")
    gty: Optional[StrictStr] = None
    session_uid: Optional[StrictStr] = Field(default=None, alias="sessionUid")
    sid: Optional[StrictStr] = None
    kind: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["jti", "aud", "scope", "clientId", "accountId", "expiresWithSession", "grantId", "gty", "sessionUid", "sid", "kind"]

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
        """Create an instance of GetJwtCustomizer200ResponseOneOfTokenSample from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aud
        if self.aud:
            _dict['aud'] = self.aud.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetJwtCustomizer200ResponseOneOfTokenSample from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jti": obj.get("jti"),
            "aud": GetJwtCustomizer200ResponseOneOfTokenSampleAud.from_dict(obj["aud"]) if obj.get("aud") is not None else None,
            "scope": obj.get("scope"),
            "clientId": obj.get("clientId"),
            "accountId": obj.get("accountId"),
            "expiresWithSession": obj.get("expiresWithSession"),
            "grantId": obj.get("grantId"),
            "gty": obj.get("gty"),
            "sessionUid": obj.get("sessionUid"),
            "sid": obj.get("sid"),
            "kind": obj.get("kind")
        })
        return _obj



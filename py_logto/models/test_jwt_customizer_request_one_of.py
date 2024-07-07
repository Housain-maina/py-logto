# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_logto.models.get_jwt_customizer200_response_one_of_context_sample import GetJwtCustomizer200ResponseOneOfContextSample
from py_logto.models.get_jwt_customizer200_response_one_of_token_sample import GetJwtCustomizer200ResponseOneOfTokenSample
from typing import Optional, Set
from typing_extensions import Self

class TestJwtCustomizerRequestOneOf(BaseModel):
    """
    TestJwtCustomizerRequestOneOf
    """ # noqa: E501
    token_type: StrictStr = Field(alias="tokenType")
    environment_variables: Optional[Dict[str, StrictStr]] = Field(default=None, alias="environmentVariables")
    script: StrictStr
    token: GetJwtCustomizer200ResponseOneOfTokenSample
    context: GetJwtCustomizer200ResponseOneOfContextSample
    __properties: ClassVar[List[str]] = ["tokenType", "environmentVariables", "script", "token", "context"]

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
        """Create an instance of TestJwtCustomizerRequestOneOf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestJwtCustomizerRequestOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tokenType": obj.get("tokenType"),
            "environmentVariables": obj.get("environmentVariables"),
            "script": obj.get("script"),
            "token": GetJwtCustomizer200ResponseOneOfTokenSample.from_dict(obj["token"]) if obj.get("token") is not None else None,
            "context": GetJwtCustomizer200ResponseOneOfContextSample.from_dict(obj["context"]) if obj.get("context") is not None else None
        })
        return _obj



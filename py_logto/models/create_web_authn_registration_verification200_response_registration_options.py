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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_authenticator_selection import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_exclude_credentials_inner import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_extensions import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_pub_key_cred_params_inner import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsPubKeyCredParamsInner
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_rp import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsRp
from py_logto.models.create_web_authn_registration_verification200_response_registration_options_user import CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsUser
from typing import Optional, Set
from typing_extensions import Self

class CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions(BaseModel):
    """
    The WebAuthn registration options that the user needs to create a new WebAuthn credential.
    """ # noqa: E501
    rp: CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsRp
    user: CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsUser
    challenge: StrictStr
    pub_key_cred_params: List[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsPubKeyCredParamsInner] = Field(alias="pubKeyCredParams")
    timeout: Optional[Union[StrictFloat, StrictInt]] = None
    exclude_credentials: Optional[List[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner]] = Field(default=None, alias="excludeCredentials")
    authenticator_selection: Optional[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection] = Field(default=None, alias="authenticatorSelection")
    attestation: Optional[StrictStr] = None
    extensions: Optional[CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions] = None
    __properties: ClassVar[List[str]] = ["rp", "user", "challenge", "pubKeyCredParams", "timeout", "excludeCredentials", "authenticatorSelection", "attestation", "extensions"]

    @field_validator('attestation')
    def attestation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'indirect', 'direct', 'enterprise']):
            raise ValueError("must be one of enum values ('none', 'indirect', 'direct', 'enterprise')")
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
        """Create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rp
        if self.rp:
            _dict['rp'] = self.rp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pub_key_cred_params (list)
        _items = []
        if self.pub_key_cred_params:
            for _item_pub_key_cred_params in self.pub_key_cred_params:
                if _item_pub_key_cred_params:
                    _items.append(_item_pub_key_cred_params.to_dict())
            _dict['pubKeyCredParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in exclude_credentials (list)
        _items = []
        if self.exclude_credentials:
            for _item_exclude_credentials in self.exclude_credentials:
                if _item_exclude_credentials:
                    _items.append(_item_exclude_credentials.to_dict())
            _dict['excludeCredentials'] = _items
        # override the default output from pydantic by calling `to_dict()` of authenticator_selection
        if self.authenticator_selection:
            _dict['authenticatorSelection'] = self.authenticator_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extensions
        if self.extensions:
            _dict['extensions'] = self.extensions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateWebAuthnRegistrationVerification200ResponseRegistrationOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rp": CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsRp.from_dict(obj["rp"]) if obj.get("rp") is not None else None,
            "user": CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "challenge": obj.get("challenge"),
            "pubKeyCredParams": [CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsPubKeyCredParamsInner.from_dict(_item) for _item in obj["pubKeyCredParams"]] if obj.get("pubKeyCredParams") is not None else None,
            "timeout": obj.get("timeout"),
            "excludeCredentials": [CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExcludeCredentialsInner.from_dict(_item) for _item in obj["excludeCredentials"]] if obj.get("excludeCredentials") is not None else None,
            "authenticatorSelection": CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsAuthenticatorSelection.from_dict(obj["authenticatorSelection"]) if obj.get("authenticatorSelection") is not None else None,
            "attestation": obj.get("attestation"),
            "extensions": CreateWebAuthnRegistrationVerification200ResponseRegistrationOptionsExtensions.from_dict(obj["extensions"]) if obj.get("extensions") is not None else None
        })
        return _obj


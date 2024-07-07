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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_authenticator_selection import ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_exclude_credentials_inner import ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_extensions import ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_pub_key_cred_params_inner import ApiInteractionVerificationWebauthnRegistrationPost200ResponsePubKeyCredParamsInner
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_rp import ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp
from py_logto.models.api_interaction_verification_webauthn_registration_post200_response_user import ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser
from typing import Optional, Set
from typing_extensions import Self

class ApiInteractionVerificationWebauthnRegistrationPost200Response(BaseModel):
    """
    ApiInteractionVerificationWebauthnRegistrationPost200Response
    """ # noqa: E501
    rp: ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp
    user: ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser
    challenge: StrictStr
    pub_key_cred_params: List[ApiInteractionVerificationWebauthnRegistrationPost200ResponsePubKeyCredParamsInner] = Field(alias="pubKeyCredParams")
    timeout: Optional[Union[StrictFloat, StrictInt]] = None
    exclude_credentials: Optional[List[ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner]] = Field(default=None, alias="excludeCredentials")
    authenticator_selection: Optional[ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection] = Field(default=None, alias="authenticatorSelection")
    attestation: Optional[StrictStr] = None
    extensions: Optional[ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions] = None
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
        """Create an instance of ApiInteractionVerificationWebauthnRegistrationPost200Response from a JSON string"""
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
            for _item in self.pub_key_cred_params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pubKeyCredParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in exclude_credentials (list)
        _items = []
        if self.exclude_credentials:
            for _item in self.exclude_credentials:
                if _item:
                    _items.append(_item.to_dict())
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
        """Create an instance of ApiInteractionVerificationWebauthnRegistrationPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rp": ApiInteractionVerificationWebauthnRegistrationPost200ResponseRp.from_dict(obj["rp"]) if obj.get("rp") is not None else None,
            "user": ApiInteractionVerificationWebauthnRegistrationPost200ResponseUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "challenge": obj.get("challenge"),
            "pubKeyCredParams": [ApiInteractionVerificationWebauthnRegistrationPost200ResponsePubKeyCredParamsInner.from_dict(_item) for _item in obj["pubKeyCredParams"]] if obj.get("pubKeyCredParams") is not None else None,
            "timeout": obj.get("timeout"),
            "excludeCredentials": [ApiInteractionVerificationWebauthnRegistrationPost200ResponseExcludeCredentialsInner.from_dict(_item) for _item in obj["excludeCredentials"]] if obj.get("excludeCredentials") is not None else None,
            "authenticatorSelection": ApiInteractionVerificationWebauthnRegistrationPost200ResponseAuthenticatorSelection.from_dict(obj["authenticatorSelection"]) if obj.get("authenticatorSelection") is not None else None,
            "attestation": obj.get("attestation"),
            "extensions": ApiInteractionVerificationWebauthnRegistrationPost200ResponseExtensions.from_dict(obj["extensions"]) if obj.get("extensions") is not None else None
        })
        return _obj



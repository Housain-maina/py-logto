# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from py_logto.models.api_interaction_put_request_identifier_one_of import ApiInteractionPutRequestIdentifierOneOf
from py_logto.models.api_interaction_put_request_identifier_one_of1 import ApiInteractionPutRequestIdentifierOneOf1
from py_logto.models.api_interaction_put_request_identifier_one_of2 import ApiInteractionPutRequestIdentifierOneOf2
from py_logto.models.api_interaction_put_request_identifier_one_of3 import ApiInteractionPutRequestIdentifierOneOf3
from py_logto.models.api_interaction_put_request_identifier_one_of4 import ApiInteractionPutRequestIdentifierOneOf4
from py_logto.models.api_interaction_put_request_identifier_one_of5 import ApiInteractionPutRequestIdentifierOneOf5
from py_logto.models.verify_verification_code_request_one_of import VerifyVerificationCodeRequestOneOf
from py_logto.models.verify_verification_code_request_one_of1 import VerifyVerificationCodeRequestOneOf1
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

APIINTERACTIONPUTREQUESTIDENTIFIER_ONE_OF_SCHEMAS = ["ApiInteractionPutRequestIdentifierOneOf", "ApiInteractionPutRequestIdentifierOneOf1", "ApiInteractionPutRequestIdentifierOneOf2", "ApiInteractionPutRequestIdentifierOneOf3", "ApiInteractionPutRequestIdentifierOneOf4", "ApiInteractionPutRequestIdentifierOneOf5", "VerifyVerificationCodeRequestOneOf", "VerifyVerificationCodeRequestOneOf1"]

class ApiInteractionPutRequestIdentifier(BaseModel):
    """
    ApiInteractionPutRequestIdentifier
    """
    # data type: ApiInteractionPutRequestIdentifierOneOf
    oneof_schema_1_validator: Optional[ApiInteractionPutRequestIdentifierOneOf] = None
    # data type: ApiInteractionPutRequestIdentifierOneOf1
    oneof_schema_2_validator: Optional[ApiInteractionPutRequestIdentifierOneOf1] = None
    # data type: ApiInteractionPutRequestIdentifierOneOf2
    oneof_schema_3_validator: Optional[ApiInteractionPutRequestIdentifierOneOf2] = None
    # data type: VerifyVerificationCodeRequestOneOf
    oneof_schema_4_validator: Optional[VerifyVerificationCodeRequestOneOf] = None
    # data type: VerifyVerificationCodeRequestOneOf1
    oneof_schema_5_validator: Optional[VerifyVerificationCodeRequestOneOf1] = None
    # data type: ApiInteractionPutRequestIdentifierOneOf3
    oneof_schema_6_validator: Optional[ApiInteractionPutRequestIdentifierOneOf3] = None
    # data type: ApiInteractionPutRequestIdentifierOneOf4
    oneof_schema_7_validator: Optional[ApiInteractionPutRequestIdentifierOneOf4] = None
    # data type: ApiInteractionPutRequestIdentifierOneOf5
    oneof_schema_8_validator: Optional[ApiInteractionPutRequestIdentifierOneOf5] = None
    actual_instance: Optional[Union[ApiInteractionPutRequestIdentifierOneOf, ApiInteractionPutRequestIdentifierOneOf1, ApiInteractionPutRequestIdentifierOneOf2, ApiInteractionPutRequestIdentifierOneOf3, ApiInteractionPutRequestIdentifierOneOf4, ApiInteractionPutRequestIdentifierOneOf5, VerifyVerificationCodeRequestOneOf, VerifyVerificationCodeRequestOneOf1]] = None
    one_of_schemas: Set[str] = { "ApiInteractionPutRequestIdentifierOneOf", "ApiInteractionPutRequestIdentifierOneOf1", "ApiInteractionPutRequestIdentifierOneOf2", "ApiInteractionPutRequestIdentifierOneOf3", "ApiInteractionPutRequestIdentifierOneOf4", "ApiInteractionPutRequestIdentifierOneOf5", "VerifyVerificationCodeRequestOneOf", "VerifyVerificationCodeRequestOneOf1" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ApiInteractionPutRequestIdentifier.model_construct()
        error_messages = []
        match = 0
        # validate data type: ApiInteractionPutRequestIdentifierOneOf
        if not isinstance(v, ApiInteractionPutRequestIdentifierOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiInteractionPutRequestIdentifierOneOf`")
        else:
            match += 1
        # validate data type: ApiInteractionPutRequestIdentifierOneOf1
        if not isinstance(v, ApiInteractionPutRequestIdentifierOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiInteractionPutRequestIdentifierOneOf1`")
        else:
            match += 1
        # validate data type: ApiInteractionPutRequestIdentifierOneOf2
        if not isinstance(v, ApiInteractionPutRequestIdentifierOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiInteractionPutRequestIdentifierOneOf2`")
        else:
            match += 1
        # validate data type: VerifyVerificationCodeRequestOneOf
        if not isinstance(v, VerifyVerificationCodeRequestOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VerifyVerificationCodeRequestOneOf`")
        else:
            match += 1
        # validate data type: VerifyVerificationCodeRequestOneOf1
        if not isinstance(v, VerifyVerificationCodeRequestOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VerifyVerificationCodeRequestOneOf1`")
        else:
            match += 1
        # validate data type: ApiInteractionPutRequestIdentifierOneOf3
        if not isinstance(v, ApiInteractionPutRequestIdentifierOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiInteractionPutRequestIdentifierOneOf3`")
        else:
            match += 1
        # validate data type: ApiInteractionPutRequestIdentifierOneOf4
        if not isinstance(v, ApiInteractionPutRequestIdentifierOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiInteractionPutRequestIdentifierOneOf4`")
        else:
            match += 1
        # validate data type: ApiInteractionPutRequestIdentifierOneOf5
        if not isinstance(v, ApiInteractionPutRequestIdentifierOneOf5):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiInteractionPutRequestIdentifierOneOf5`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ApiInteractionPutRequestIdentifier with oneOf schemas: ApiInteractionPutRequestIdentifierOneOf, ApiInteractionPutRequestIdentifierOneOf1, ApiInteractionPutRequestIdentifierOneOf2, ApiInteractionPutRequestIdentifierOneOf3, ApiInteractionPutRequestIdentifierOneOf4, ApiInteractionPutRequestIdentifierOneOf5, VerifyVerificationCodeRequestOneOf, VerifyVerificationCodeRequestOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ApiInteractionPutRequestIdentifier with oneOf schemas: ApiInteractionPutRequestIdentifierOneOf, ApiInteractionPutRequestIdentifierOneOf1, ApiInteractionPutRequestIdentifierOneOf2, ApiInteractionPutRequestIdentifierOneOf3, ApiInteractionPutRequestIdentifierOneOf4, ApiInteractionPutRequestIdentifierOneOf5, VerifyVerificationCodeRequestOneOf, VerifyVerificationCodeRequestOneOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ApiInteractionPutRequestIdentifierOneOf
        try:
            instance.actual_instance = ApiInteractionPutRequestIdentifierOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiInteractionPutRequestIdentifierOneOf1
        try:
            instance.actual_instance = ApiInteractionPutRequestIdentifierOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiInteractionPutRequestIdentifierOneOf2
        try:
            instance.actual_instance = ApiInteractionPutRequestIdentifierOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VerifyVerificationCodeRequestOneOf
        try:
            instance.actual_instance = VerifyVerificationCodeRequestOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VerifyVerificationCodeRequestOneOf1
        try:
            instance.actual_instance = VerifyVerificationCodeRequestOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiInteractionPutRequestIdentifierOneOf3
        try:
            instance.actual_instance = ApiInteractionPutRequestIdentifierOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiInteractionPutRequestIdentifierOneOf4
        try:
            instance.actual_instance = ApiInteractionPutRequestIdentifierOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiInteractionPutRequestIdentifierOneOf5
        try:
            instance.actual_instance = ApiInteractionPutRequestIdentifierOneOf5.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ApiInteractionPutRequestIdentifier with oneOf schemas: ApiInteractionPutRequestIdentifierOneOf, ApiInteractionPutRequestIdentifierOneOf1, ApiInteractionPutRequestIdentifierOneOf2, ApiInteractionPutRequestIdentifierOneOf3, ApiInteractionPutRequestIdentifierOneOf4, ApiInteractionPutRequestIdentifierOneOf5, VerifyVerificationCodeRequestOneOf, VerifyVerificationCodeRequestOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiInteractionPutRequestIdentifier with oneOf schemas: ApiInteractionPutRequestIdentifierOneOf, ApiInteractionPutRequestIdentifierOneOf1, ApiInteractionPutRequestIdentifierOneOf2, ApiInteractionPutRequestIdentifierOneOf3, ApiInteractionPutRequestIdentifierOneOf4, ApiInteractionPutRequestIdentifierOneOf5, VerifyVerificationCodeRequestOneOf, VerifyVerificationCodeRequestOneOf1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ApiInteractionPutRequestIdentifierOneOf, ApiInteractionPutRequestIdentifierOneOf1, ApiInteractionPutRequestIdentifierOneOf2, ApiInteractionPutRequestIdentifierOneOf3, ApiInteractionPutRequestIdentifierOneOf4, ApiInteractionPutRequestIdentifierOneOf5, VerifyVerificationCodeRequestOneOf, VerifyVerificationCodeRequestOneOf1]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())



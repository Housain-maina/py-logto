# GetUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**primary_email** | **str** |  | 
**primary_phone** | **str** |  | 
**name** | **str** |  | 
**avatar** | **str** |  | 
**custom_data** | **object** | arbitrary | 
**identities** | [**Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue]**](GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue.md) |  | 
**last_sign_in_at** | **float** |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 
**profile** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md) |  | 
**application_id** | **str** |  | 
**is_suspended** | **bool** |  | 
**has_password** | **bool** |  | [optional] 
**sso_identities** | [**List[GetUser200ResponseSsoIdentitiesInner]**](GetUser200ResponseSsoIdentitiesInner.md) | List of SSO identities associated with the user. Only available when the &#x60;includeSsoIdentities&#x60; query parameter is provided with a truthy value. | [optional] 

## Example

```python
from py_logto.models.get_user200_response import GetUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUser200Response from a JSON string
get_user200_response_instance = GetUser200Response.from_json(json)
# print the JSON string representation of the object
print(GetUser200Response.to_json())

# convert the object into a dict
get_user200_response_dict = get_user200_response_instance.to_dict()
# create an instance of GetUser200Response from a dict
get_user200_response_from_dict = GetUser200Response.from_dict(get_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



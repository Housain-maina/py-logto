# GetUser200ResponseSsoIdentitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**user_id** | **str** |  | 
**issuer** | **str** |  | 
**identity_id** | **str** |  | 
**detail** | **object** | arbitrary | 
**created_at** | **float** |  | 
**sso_connector_id** | **str** |  | 

## Example

```python
from py_logto.models.get_user200_response_sso_identities_inner import GetUser200ResponseSsoIdentitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUser200ResponseSsoIdentitiesInner from a JSON string
get_user200_response_sso_identities_inner_instance = GetUser200ResponseSsoIdentitiesInner.from_json(json)
# print the JSON string representation of the object
print(GetUser200ResponseSsoIdentitiesInner.to_json())

# convert the object into a dict
get_user200_response_sso_identities_inner_dict = get_user200_response_sso_identities_inner_instance.to_dict()
# create an instance of GetUser200ResponseSsoIdentitiesInner from a dict
get_user200_response_sso_identities_inner_from_dict = GetUser200ResponseSsoIdentitiesInner.from_dict(get_user200_response_sso_identities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



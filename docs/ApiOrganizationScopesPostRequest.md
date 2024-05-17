# ApiOrganizationScopesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the organization scope. It must be unique within the organization template. | 
**description** | **str** | The description of the organization scope. | [optional] 

## Example

```python
from py_logto.models.api_organization_scopes_post_request import ApiOrganizationScopesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationScopesPostRequest from a JSON string
api_organization_scopes_post_request_instance = ApiOrganizationScopesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationScopesPostRequest.to_json())

# convert the object into a dict
api_organization_scopes_post_request_dict = api_organization_scopes_post_request_instance.to_dict()
# create an instance of ApiOrganizationScopesPostRequest from a dict
api_organization_scopes_post_request_from_dict = ApiOrganizationScopesPostRequest.from_dict(api_organization_scopes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



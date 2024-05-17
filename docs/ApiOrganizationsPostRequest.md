# ApiOrganizationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the organization. | 
**description** | **str** | The description of the organization. | [optional] 
**created_at** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_organizations_post_request import ApiOrganizationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsPostRequest from a JSON string
api_organizations_post_request_instance = ApiOrganizationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsPostRequest.to_json())

# convert the object into a dict
api_organizations_post_request_dict = api_organizations_post_request_instance.to_dict()
# create an instance of ApiOrganizationsPostRequest from a dict
api_organizations_post_request_from_dict = ApiOrganizationsPostRequest.from_dict(api_organizations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



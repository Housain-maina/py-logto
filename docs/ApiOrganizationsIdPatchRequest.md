# ApiOrganizationsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The updated name of the organization. | [optional] 
**description** | **str** | The updated description of the organization. | [optional] 
**created_at** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_organizations_id_patch_request import ApiOrganizationsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationsIdPatchRequest from a JSON string
api_organizations_id_patch_request_instance = ApiOrganizationsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationsIdPatchRequest.to_json())

# convert the object into a dict
api_organizations_id_patch_request_dict = api_organizations_id_patch_request_instance.to_dict()
# create an instance of ApiOrganizationsIdPatchRequest from a dict
api_organizations_id_patch_request_from_dict = ApiOrganizationsIdPatchRequest.from_dict(api_organizations_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



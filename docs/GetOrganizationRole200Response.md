# GetOrganizationRole200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from py_logto.models.get_organization_role200_response import GetOrganizationRole200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationRole200Response from a JSON string
get_organization_role200_response_instance = GetOrganizationRole200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationRole200Response.to_json())

# convert the object into a dict
get_organization_role200_response_dict = get_organization_role200_response_instance.to_dict()
# create an instance of GetOrganizationRole200Response from a dict
get_organization_role200_response_from_dict = GetOrganizationRole200Response.from_dict(get_organization_role200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



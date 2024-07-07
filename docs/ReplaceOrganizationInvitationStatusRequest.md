# ReplaceOrganizationInvitationStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_user_id** | **str** | The ID of the user who accepted the organization invitation. Required if the status is \&quot;Accepted\&quot;. | [optional] 
**status** | **str** | The status of the organization invitation. | 

## Example

```python
from py_logto.models.replace_organization_invitation_status_request import ReplaceOrganizationInvitationStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceOrganizationInvitationStatusRequest from a JSON string
replace_organization_invitation_status_request_instance = ReplaceOrganizationInvitationStatusRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceOrganizationInvitationStatusRequest.to_json())

# convert the object into a dict
replace_organization_invitation_status_request_dict = replace_organization_invitation_status_request_instance.to_dict()
# create an instance of ReplaceOrganizationInvitationStatusRequest from a dict
replace_organization_invitation_status_request_from_dict = ReplaceOrganizationInvitationStatusRequest.from_dict(replace_organization_invitation_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



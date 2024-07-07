# CreateOrganizationInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inviter_id** | **str** | The ID of the user who is inviting the user to join the organization. | [optional] 
**invitee** | **str** | The email address of the user to invite to join the organization. | 
**organization_id** | **str** | The ID of the organization to invite the user to join. | 
**expires_at** | **float** | The epoch time in milliseconds when the invitation expires. | 
**organization_role_ids** | **List[str]** | The IDs of the organization roles to assign to the user when they accept the invitation. | [optional] 
**message_payload** | [**CreateOrganizationInvitationRequestMessagePayload**](CreateOrganizationInvitationRequestMessagePayload.md) |  | 

## Example

```python
from py_logto.models.create_organization_invitation_request import CreateOrganizationInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationInvitationRequest from a JSON string
create_organization_invitation_request_instance = CreateOrganizationInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationInvitationRequest.to_json())

# convert the object into a dict
create_organization_invitation_request_dict = create_organization_invitation_request_instance.to_dict()
# create an instance of CreateOrganizationInvitationRequest from a dict
create_organization_invitation_request_from_dict = CreateOrganizationInvitationRequest.from_dict(create_organization_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



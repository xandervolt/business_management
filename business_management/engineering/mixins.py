
class FileUploadMixin(object):
    
    def handle_file_upload(file_to_upload):
    
        # Get the authenticated user credentials from python-social-auth
        social = request.user.social_auth.get(provider='office365')
        access_token = social.extra_data['access_token']
    
        # build our header for the api call
        headers = {
            'Authorization' : 'Bearer {0}'.format(access_token),
        }
    
        # build the url for the api call
        # Look at https://dev.onedrive.com/items/upload_put.htm for reference
        url = settings.SHAREPOINT_RESOURCE + '/_api/v2.0/drive/root:/' + file_to_upload.name + ':/content'
    
        # Make the api call
        response = requests.put(url, data=open(file_to_upload, 'rb'), headers=headers)
        
        return response
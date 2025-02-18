# # import requests

# # # Function to fetch Confluence page content using the page ID
# # def fetch_confluence_page_content(content_id, confluence_url, auth_token, username):
# #     url = f"{confluence_url}/wiki/rest/api/content/{content_id}?expand=body.storage"
# #     headers = {
# #         "Authorization": f"Basic {auth_token}",
# #         "Accept": "application/json"
# #     }
# #     response = requests.get(url, headers=headers)
    
# #     if response.status_code == 200:
# #         page_content = response.json()
# #         return page_content['body']['storage']['value']
# #     else:
# #         print(f"Failed to fetch content: {response.status_code}")
# #         return None


# # Function to fetch Confluence page content using the page ID

# import requests
# import base64

# # Function to fetch Confluence page content using the page ID
# def fetch_confluence_page_content(content_id, confluence_url, api_token, username):
#     url = f"{confluence_url}/wiki/rest/api/content/{content_id}?expand=body.view"
    
#     # Encode credentials using Base64
#     auth_string = f"{username}:{api_token}"
#     auth_token = base64.b64encode(auth_string.encode()).decode()
    
#     headers = {
#         "Authorization": f"Basic {auth_token}",
#         "Accept": "application/json"
#     }
#     print(url)
#     # Send GETrequest to fetch content from Confluence
#     response = requests.get(url, headers=headers)
#     print(response)
#     if response.status_code == 200:
#         page_content = response.json()
#         html_content = page_content['body']['view']['value']
#         print('HTML Content:', html_content)
#         return html_content
#     else:
#         print(f"Failed to fetch content: {response.status_code}")
#         return None


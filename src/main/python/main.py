import sys
import requests
from table_extractor import extract_all_tables_from_html_to_excel_and_return
from code_generator import generate_angular_code_from_excel_files
import base64
# Function to fetch Confluence page content
def fetch_confluence_page_content(content_id, confluence_url, auth_token, username):
    url = f"{confluence_url}/wiki/rest/api/content/{content_id}?expand=body.view"
    
    # Encode credentials using Base64
    auth_string = f"{username}:{auth_token}"
    auth_token = base64.b64encode(auth_string.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_token}",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_content = response.json()
        html_content = page_content['body']['view']['value']
        return html_content
    else:
        print(f"Failed to fetch content: {response.status_code}")
        return None

# Main function to run the Angular code generation
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <content_id>")
        sys.exit(1)

    content_id = sys.argv[1]
    confluence_url = "https://igtbworks.atlassian.net"  # Hardcoded Confluence URL
    auth_token = "ATAT0xRD2632Qa3CHShXuwk90fDO8kWPV7y2Aao3MgNCSN-tj8DEmLA2Ihhh8l_kx1vbTq7l0CYzhcSjRdKKinb_-2MTvp59fRbtgXnGeNV965woNXhQZmdq5x0sRCDNMGrh9wPsgT6UzoeaIUV4oijC27ckRgJTx5Q=DBCD1173"  # Replace with your Confluence auth token
    username = "aditya.priyam@intellectdesign.com"
    # Fetch HTML content from Confluence
    html_content = fetch_confluence_page_content(content_id, confluence_url, auth_token, username)
    if html_content:
        # Extract all tables from the HTML content
        tables = extract_all_tables_from_html_to_excel_and_return(html_content)
        print("Tables length: ",len(tables))
        # Iterate through each table, generate Angular code, and print/save the output
        #prompt = input("Enter the prmopt: ")
        # for index, table in enumerate(tables, start=1):
        print("\nGenerating Angular code for all the Tables:\n")
        generate_angular_code_from_excel_files()
            # Optionally, save to a .ts file
            # with open(f"angular_component_table_{index}.ts", "w") as file:
            #     file.write(generated_code)

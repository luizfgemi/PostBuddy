import requests
from requests.auth import HTTPBasicAuth
import re

def execute_requests(requests_text, variables, extract_var_name, extract_var_regex):
    requests_list = requests_text.strip().split("\n\n")

    responses = []
    for request in requests_list:
        lines = request.split("\n")
        method = lines[0].split(": ")[1]
        url = lines[1].split(": ")[1]
        headers = {}
        data = None
        auth = None

        for line in lines[2:]:
            if line.startswith("Headers: "):
                headers_text = line.split(": ", 1)[1].strip()
                for header in headers_text.split("\n"):
                    if ": " in header:
                        key, value = header.split(": ", 1)
                        headers[key] = value
            elif line.startswith("Data: "):
                data = line.split(": ", 1)[1].strip()
            elif line.startswith("Auth Type: "):
                auth_type = line.split(": ")[1].strip()
            elif line.startswith("Auth: "):
                auth_text = line.split(": ", 1)[1].strip()

        if auth_type == "Basic" and auth_text:
            user, pwd = auth_text.split(":")
            auth = HTTPBasicAuth(user, pwd)
        elif auth_type == "Bearer Token" and auth_text:
            headers['Authorization'] = f"Bearer {auth_text}"
        elif auth_type == "API Key" and auth_text:
            key_name, key_value = auth_text.split(":")
            headers[key_name] = key_value

        response = requests.request(method, url, headers=headers, data=data, auth=auth)
        responses.append(f"Request: {request}\nResponse:\nStatus Code: {response.status_code}\n{response.text}\n\n")

        extract_variable(response.text, variables, extract_var_name, extract_var_regex)

    return responses

def extract_variable(response_text, variables, extract_var_name, extract_var_regex):
    if extract_var_name and extract_var_regex:
        match = re.search(extract_var_regex, response_text)
        if match:
            variables[extract_var_name] = match.group(1)

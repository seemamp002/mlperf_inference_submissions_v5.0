# Copyright 2024-25 MLCommons. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================


import json
import os
import time
import sys
sys.path.insert(0, os.path.join("inference", "tools", "submission"))
import submission_checker as checker # noqa

with open('summary_results.json') as f:
    data = json.load(f)
#print(models_all)
#print(platforms)

def get_header():
    css = """
    * {
        box-sizing: border-box;
    }
    html, body, div, span, applet, object, iframe, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
        margin: 0;
        padding: 0;
        border: 0;
        font: inherit;
        vertical-align: baseline;
    }
    body {
        font: 400 15px / 22px Roboto, sans-serif;
        background-color: #212930;
        background-image: radial-gradient(circle at 100% 0%, rgb(230 157 100 / 20%) 0%, #212930 50%);
        color: #040304;
        padding: 0;
        margin: 0;
        overflow-y: scroll;
        overflow-x: hidden;
        text-align: left;
    }
.details-cell {
    text-transform: capitalize;
}

a.button:hover {
    color: white;
    background-color: gray;
    text-decoration: underline;
}
a.button {
display: inline-block; /* Allows background-color to apply */
    text-decoration: none; /* Removes default underline */

    }
        .button-container {
            display: flex;
            width: 100%;
            max-width: 800px; /* Optional: Limit the container width */
            margin: 0 auto;
        }

        .button-container a {
            flex: 1; /* Distribute space evenly */
            text-decoration: none;
        }

        .button {
            padding: 15px 0;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            display: inline-block;
        }


        .button:active {
            background-color: #003f8a;
            transform: scale(0.95);
        }

        /* Add spacing between buttons */
        .button:not(:last-child) {
            margin-right: 10px;
        }

    .topbar {
        /* position: fixed; */
        top: 0;
        left: 0;
        right: 0;
        padding: 1rem;
        height: 66px;
        border-bottom: 1px solid rgb(255 255 255 / 10%);
    }
    .topbar-container {
        max-width: 1350px;
        padding: 0 2rem;
        margin: 0 auto;
    }
    .logo {
        width: max-content;
    }
    .svg-text {
        fill: #9d9d9d;
    }
    .logo:hover .svg-text {
        fill: #ffffff;
        transition: fill .25s ease;
    }
    .resultpage {
        max-width: 1300px;
        padding: 0 2rem;
        margin: 0 auto;
    }

    .welcome-section, .welcome-section .table {
        color: #fff;
    }
    .welcome-section a {
        color: #90bfff;
    }
    .welcome-section-wrapper {
        width: 85%;
        padding: 2rem;
        margin: 0 auto;
    }

    .welcome-section-wrapper2 {
    width: 85%;
    padding-bottom: 2.5rem;
    margin-top: -40px;
    margin-inline: auto;
}
    .titlebarcontainer {
        margin-top: 6vh;
        margin-bottom: 6vh;
    }
    .main-title {
        font-size: 3rem;
        margin: 1rem 0;
    }
    .main-title-description {
        font-size: smaller;
    }
    .submittertitle {
        text-align: center;
    }
    .datebar {
        text-align: inherit;
    }
    .test-details-container {
        grid-template-columns: 30% 30%;
    }
    .details-group {
        margin-bottom: .5rem;
    }
    .details-group .details-cell:first-of-type {
        font-weight: bold;
        margin-right: 6px;
    }
    .titlebar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .date-right {
    font-size: 18px;
    }

    .table-half {
        width: 100%;
        display: grid;
        justify-content: space-around;
        grid-template-columns: 50% 50%;
        margin-left: auto;
        margin-right: auto;
    }
    .test-details-container {
        grid-template-columns: 30% 30%;
    }
    .table-full, .table-half {
        margin-bottom: 2rem;
    }
    .table-wrapper {
        position: relative;
        background-color: #fff;
        padding: 2rem;
        box-shadow: 0 1px 16px 0 rgb(25 27 28), 0 1px 16px 1px rgb(20 20 22);
        border-radius: 8px;
    }
    .table-half .table-wrapper:nth-of-type(even) {
        margin-inline-start: 1rem;
    }
    .table-half .table-wrapper:nth-of-type(odd) {
        margin-inline-end: 1rem;
    }
    .table-wrapper .floater {
        position: absolute;
        right: 10%;
        top: -25px;
    }
    .table-wrapper h3 {
        margin: 0;
        padding: 0rem .3rem .6rem .3rem;
        border-bottom: 2px solid #dee2e6;
    }
    .table {
        border-collapse: collapse;
        width: 100%;
        table-layout: fixed;
        color: #212529;
        word-break: break-word;
    }
    .table-striped tbody tr:nth-of-type(odd) {
        background-color: rgba(0, 0, 0, 0.05);
    }
    .table th, .table td {
        padding: 0.5rem;
        vertical-align: middle;
    }
    .table th {
        font-weight: bold;
        border-bottom: 2px solid #dee2e6;
    }
    .table.datebar th {
        border: none;
    }
    .table-full .table:not(.results-table) th, .table-full .table:not(.results-table) td {
        width: 50%;
    }
    a.button {
    color: black;
    background-color: azure;
    }
    .table th:not(:last-child), .table td:not(:last-child) {
        position: relative;
    }
    .table th:not(:last-child):after, .table td:not(:last-child):after {
        content: "";
        display: block;
        width: 1px;
        height: 65%;
        background-color: #d9d9d9;
        position: absolute;
        right: 0;
        top: 50%;
        transform: translatey(-50%);
    }
    .th-parent,
    .results-table tr:nth-child(n+3) td:nth-child(-n+2) {
        background-color: #dddee3;    }
    /* Apply styling to the first two columns of rows starting from the third row */
.results-table th, .results-table tr:nth-child(n+3) td:nth-child(-n+2) {
    background-color: #dddee3;
    border-bottom: 2px solid #b3b6b9;
}

.perf,.accuracyoff{
    padding-right: 40px!important;
    font-weight: bold;
    text-align: right;  /* Aligns numbers to the right */
}
.units{
text-align: center;
    padding-left: 20px;
}
.na{
text-align: center;
}
.model,.acc-target {
text-align: left;
padding-left: 20px!important;
}


.results-table th:not(:last-child):after, .results-table tr:nth-child(n+3) td:nth-child(-n+2):not(:last-child):after {
    background-color: #b3b6b9;
}

    .footer {
        border-top: 1px solid rgb(255 255 255 / 10%);
        padding: 1rem 1rem 3rem 1rem;
        color: rgb(255 255 255 / 70%);
    }
    .footer-container {
        max-width: 1300px;
        padding: 0 2rem;
        margin: 0 auto;
    }

    @media (max-width:900px) {
        .welcome-section- {
            width: 100%;
        }
        .test-details-container {
            grid-template-columns: 50% 50%;
            text-align: center;
        }
        
        .details-container .table-half {
            display: block;
        }
        .table-half .table-:nth-of-type(odd) {
            margin-inline-end: initial;
            margin-bottom: 2rem;
        }
        .table-half .table-:nth-of-type(even) {
            margin-inline-start: initial;
        }
    }
    @media (max-width:575px) {
        body {
            background-image: radial-gradient(circle at 100% 0%, rgb(230 157 100 / 20%) 0%, #212930 20%);
            font: 400 12px / 19px Roboto, sans-serif;
        }
        .welcome-section- {
            padding: 0;
        }
        .titlebarcontainer {
            margin-top: 8vh;
            margin-bottom: 6vh;
        }
        .main-title {
            font-size: 2rem;
            line-height: normal;
            margin: .5rem 0;
        }
        .submittertitle {
            text-align: initial;
        }
        .test-details-container {
            display: block;
            text-align: initial;
            font-size: small;
        }
        .table-container {
            overflow: auto;
        }
    }
    """

    html_header = f"""
<head>
<title>MLPerf Inference {version}</title>
<meta name="viewport" content="width=device-width, initial-scale=1, interactive-widget=resizes-content">
<style type="text/css">
{css}
</style>
</head>
"""
    return html_header

def get_footer():
    html_footer = f"""
    <footer class="footer">
        <div class="footer-container">
            <div class="copyright">© 2025 MLCommons.</div>
        </div>
    </footer>
    """
    return html_footer

def get_stripe_image():
    html_stripe_svg = f"""<div class="yellow-strip floater" data-speed="0.1" style="transform: translate3d(0px, 19px, 0px);">
<svg role="presentation" aria-hidden="true" width="83" height="21" viewBox="0 0 83 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0 0L0 3.42863L3.24487 0L0 0Z" fill="#FBBC04"></path>
<path d="M8.29399 0L0 8.76368L0 12.202L11.5481 0L8.29399 0Z" fill="#FBBC04"></path>
<path d="M16.5972 0L0 17.5371L0 20.9754L19.8513 0L16.5972 0Z" fill="#FBBC04"></path>
<path d="M24.9016 0L5.02734 20.9998H8.28142L28.1557 0L24.9016 0Z" fill="#FBBC04"></path>
<path d="M33.2024 0L13.3281 20.9998H16.5822L36.4565 0L33.2024 0Z" fill="#FBBC04"></path>
<path d="M41.5071 0L21.6328 20.9998H24.8869L44.7611 0L41.5071 0Z" fill="#FBBC04"></path>
<path d="M49.8079 0L29.9336 20.9998H33.1923L53.0619 0L49.8079 0Z" fill="#FBBC04"></path>
<path d="M58.1119 0L38.2422 20.9998H41.4963L61.3659 0L58.1119 0Z" fill="#FBBC04"></path>
<path d="M66.4165 0L46.5469 20.9998H49.801L69.6706 0L66.4165 0Z" fill="#FBBC04"></path>
<path d="M74.7212 0L54.8516 20.9998H58.1056L77.9753 0L74.7212 0Z" fill="#FBBC04"></path>
<path d="M66.4064 20.9989L82.999 3.4618V0.0234375L63.1523 20.9989H66.4064Z" fill="#FBBC04"></path>
<path d="M74.7111 20.9989L83.0005 12.2352V8.79688L71.457 20.9989H74.7111Z" fill="#FBBC04"></path>
<path d="M82.9981 20.9989V17.5703L79.7578 20.9989H82.9981Z" fill="#FBBC04"></path>
</svg>
</div>
"""
    return html_stripe_svg

def get_month_year(version: str) -> str:
    """
    Generate month, year of submission based on the version.
    
    Args:
        version (str): Version string (e.g., 'v1.0', 'v1.1', 'v2.0', ..., 'v9.1')
        
    Returns:
        str: month, str: year
    """
    # Define version-to-month mapping
    version_month_map = {
        "0": "February",
        "1": "August"
    }
    
    try:
        if not version.startswith('v'):
            raise ValueError("Version must start with 'v'")
        
        major, minor = version[1:].split('.')
        major = int(major)
        minor = minor.strip()
        
        if minor not in version_month_map:
            raise ValueError("Invalid minor version. Expected '0' or '1'.")
        
        if not (1 <= major <= 9):
            raise ValueError("Major version out of range (expected 1-9).")
        
        # Calculate year, starting from 2024 for v1.0
        year = 2021 + (major - 1)
        month = version_month_map[minor]
        
        return month, year
    
    except (ValueError, IndexError) as e:
        return f"Error: Invalid version format - {e}"


def get_header_table(system_json, version):
    submitter = system_json.get('submitter')
    system_name = system_json.get('system_name')
    division = system_json.get('division')
    category = system_json.get('system_type')
    status = system_json.get('status')

    '''
    availability_string = get_availability_string(version)
    if status.lower() == "available":
        availability_string = f"""Available {availability_string}"""
    elif status.lower() == "preview":
        availability_string = f"""Preview {availability_string}, should be avaiable within 180 days"""
    else:
        availability_string = f"""Research and Internal {availability_string}"""
    '''
    availability_string = status
    month, year = get_month_year(version)

    html =  f"""<div class="titlebarcontainer">
<div class="titlebar">
<h1 class="main-title">MLPerf Inference {version}</h1>
<p class="main-title-description">Copyright 2019 - 2025 MLCommons</p>
<span class="date-right">{month} {year}</span>
</div>
</div>
<div class="table table-full submittertitle">
<h2>{submitter} - {system_name}</h2>
</div>
<div class="test-details-container table-half">
<div class="test-details">
<div class="details-group">
<span id="license_num" class="details-cell"><a href="https://github.com/mlcommons/inference/blob/master/README.md">MLPerf Inference Category:</a></span>
<span id="license_num_val" class="details-cell">{category}</span>
</div>
<div class="details-group">
<span id="sw_avail" class="details-cell"><a href="https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#results-categories">Availability:</a></span>
<span id="sw_avail_val" class="details-cell">{availability_string}</span>
</div>
</div>
<div class="test-details">
<div class="details-group">
<span id="tester" class="details-cell">Submitted by:</span>
<span id="tester_val" class="details-cell">{submitter}</span>
</div>
<div class="details-group">
<span id="test_date" class="details-cell"><a href="https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc#divisions">MLPerf Inference Division:</a></span>
<span id="test_date_val" class="details-cell">{division}</span>
</div>
</div>
</div>
"""
    return html


def get_system_json(path):
    #import requests
    # Send a GET request to the URL
    #response = requests.get(url)

    with open(path, "r") as f:
        data = json.load(f)
    # Check if the request was successful
    #if response.status_code == 200:
    #    # Parse the JSON content
    #    data = response.json()
        
    return data

def get_accelerator_details_table(system_json):
    html_stripe_svg = get_stripe_image()
    main_keys = [ "accelerator_model_name", "accelerators_per_node", "accelerator_memory_capacity", "accelerator_host_interconnect" ]
    table = f"""{html_stripe_svg}
<h3>Accelerator Details</h3>
<div class="table-container">
<table class="table">
"""
    for key in main_keys:
        if key in system_json:
            value = system_json[key]
            table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""
    for key,value in system_json.items():
        if not key.startswith("accelerator") or key in main_keys:
            continue
        table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""

    table += "</table></div>"
    return table

def get_cpu_details_table(system_json):
    html_stripe_svg = get_stripe_image()
    main_keys = [ "host_processor_model_name", "host_processors_per_node", "host_processor_core_count", "host_processor_frequency" ]
    table = f"""{html_stripe_svg}
<h3>Processor and Memory Details</h3>
<div class="table-container">
<table class="table">
"""
    for key in main_keys:
        if key in system_json:
            value = system_json[key]
            table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""
            
    hardware_fields = [ "processor", "cpu", "memory" ]
    for key,value in system_json.items():
        if any (a in key for a in hardware_fields) and "accelerator" not in key and key not in main_keys:
            table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""

    table += "</table></div>"
    return table

def get_network_details_table(system_json):
    html_stripe_svg = get_stripe_image()
    table = f"""{html_stripe_svg}
<h3>Network and Interconnect Details</h3>
<div class="table-container">
<table class="table">
"""
    hardware_fields = [ "network", "nics" ]
    for key,value in system_json.items():
        if any (a in key for a in hardware_fields) and "accelerator" not in key:
            table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""

    table += "</table></div>"
    return table
    
def get_hardware_details_table(system_json):
    html_stripe_svg = get_stripe_image()
    table = f"""{html_stripe_svg}
<h3>Other Hardware Details</h3>
<div class="table-container">
<table class="table">
"""
    hardware_fields = [ "hardware", "disk", "cooling",  "power", "hw_" ]
    for key,value in system_json.items():
        if any (a in key for a in hardware_fields) and "accelerator" not in key:
            table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""

    table += "</table></div>"
    return table

def get_software_details_table(system_json):
    html_stripe_svg = get_stripe_image()
    table = f"""{html_stripe_svg}
<h3>Software Details</h3>
<div class="table-container">
<table class="table">
"""
    software_fields = [ "software", "framework", "firmware", "sw_", "operating_" ]
    for key,value in system_json.items():
        if any (a in key for a in software_fields):
            table += f"""<tr><td>{key}</td><td>{value}</td></tr>"""

    table += "</table></div>"
    return table

def round_to_max_5_digits(number):
    # Ensure the input is a float (if it's a string, convert it)
    if isinstance(number, str):
        number = float(number)

    # Convert the number to a string to check its decimal part
    number_str = f"{number:.10f}".rstrip('0').rstrip('.')
    
    if '.' in number_str:
        # Split into integer and decimal parts
        integer_part, decimal_part = number_str.split('.')
        # Check if decimal part exceeds 5 digits
        if len(decimal_part) > 5:
            return round(number, 5)
    
    return number

def round_dict_values(input_dict):
    """
    Takes a dictionary and rounds all numeric values (integers or floats) to max 5 decimal places.
    
    Args:
        input_dict (dict): A dictionary where the values are numbers.
        
    Returns:
        dict: A new dictionary with the values rounded to max 5 decimal places.
    """
    if isinstance(input_dict, str):
        input_dict = convert_string_to_dict(input_dict)
    return ", ".join(f"""{key}: {round_to_max_5_digits(value)}""" for key, value in input_dict.items())


# Function to convert a string to a dictionary
def convert_string_to_dict(input_string):
     # Split the input string by spaces
    items = input_string.split("  ")
    
    # Initialize an empty dictionary
    result_dict = {}
    
    # Iterate through the items, taking each pair of key and value
    for item in items:
        # Split each item into key and value at the colon
        key_value = item.split(':')
        
        # Ensure there are exactly two parts (key and value)
        if len(key_value) == 2:
            key, value = key_value
            # Strip any extra whitespace
            key = key.strip().replace("_", " ")
            value = value.strip()
            
            # Check if the value is not empty, then convert it to float
            if value:
                try:
                    result_dict[key] = float(value)
                except ValueError:
                    print(f"Warning: Could not convert '{value}' to float. Skipping this entry.")
            else:
                print(f"Warning: Empty value found for '{key}'. Skipping this entry.")
        else:
            print(f"Warning: Invalid format for item '{item}'. Skipping this entry.")
    
    return result_dict

def get_button_links(system, division):
    code_link = os.path.dirname(system.replace("/results/", "/code/"))
    results_link = system
    measurements_link = system.replace("/results/", "/measurements/")
    compliance_link = system.replace("/results/", "/compliance/")

    html = f"""<div class="button-container">
<a href="{code_link}" class="button">Code</a>
<a href="{results_link}" class="button">Result Logs</a>
<a href="{measurements_link}" class="button">Measurements</a>
"""
    if division == "closed":
        html += f"""<a href="{compliance_link}" class="button">Compliance</a>
"""
    html +="""</div>"""

    return html

def get_table_header(division, category):
    if division == "open":
        accuracy_achieved_header = '<th>Accuracy</th>'
        colspan = "3"
    else:
        accuracy_achieved_header = "" #dont show accuracy as submitters are only expected to achieve the target
        colspan = "2"

    num_scenarios = 1
    html_stripe_svg = get_stripe_image()
    html_table_head = f"""{html_stripe_svg}
<h3>Results Table</h3>
<div class="table-container">
<table class="table results-table">
<tr>
<th rowspan="2" class="th-parent">Model</th>
<th rowspan="2" class="th-parent">Accuracy Target</th>
"""
    if "datacenter" in category:
        num_scenarios += 1
        html_table_head += f"""<th colspan="{colspan}">Server</th>
"""

    html_table_head += f"""<th colspan="{colspan}">Offline</th>
"""

    if "edge" in category:
        num_scenarios += 2
        html_table_head += f"""<th colspan="{colspan}">SingleStream</th>
<th colspan="{colspan}">MultiStream</th>
"""
    html_table_head += f"""</tr>
<tr>
"""

    for i in range(num_scenarios):
        html_table_head += f"""{accuracy_achieved_header}
<th>Metric</th>
<th>Performance</th>
"""

    html_table_head += f"""</tr>"""
    return html_table_head

# Initialize a dictionary to organize the data by 'Details'
tables = {}
version = os.environ.get('INFERENCE_RESULTS_VERSION')

# Populate the dictionary with data
for entry in data:
    details = entry['Details']
    if details not in tables:
        tables[details] = {}
    categories = [ "edge", "datacenter" ]
    for category in categories:
        if category not in entry['Suite']:
            continue
        if category not in tables[details]:
            tables[details][category] = {}
        if entry['Category'] not in tables[details][category]:
            tables[details][category][entry['Category']] = {}

        if entry['Model'] not in tables[details][category][entry['Category']]:
            tables[details][category][entry['Category']] [entry['Model']] = {}
        if entry['Scenario'] not in tables[details][category][entry['Category']][entry['Model']]:
            tables[details][category][entry['Category']][entry['Model']][entry['Scenario']] = entry

# Now you can format each group in 'tables' as a markdown table
for details, entries in tables.items():
            
    details_split = details.split("/")
    details_split[9] = "systems"
    system = os.path.sep.join(details_split[7:11])
    system_json_path = f"""{system}.json"""
    system_json = get_system_json(system_json_path)
    header_table = get_header_table(system_json, version)
    accelerator_details = get_accelerator_details_table(system_json)
    cpu_details = get_cpu_details_table(system_json)
    hardware_details = get_hardware_details_table(system_json)
    software_details = get_software_details_table(system_json)
    network_details = get_network_details_table(system_json)
    
    out = f"## {details}"

    #models_edge = [ "gptj-99", "gptj-99.9", "bert-99", "bert-99.9", "stable-diffusion-xl", "retinanet", "resnet", "3d-unet-99", "3d-unet-99.9"  ]
    #if "datacenter" in entries:
    #    models = [ "llama2-70b-99", "llama2-70b-99.9", "gptj-99", "gptj-99.9", "bert-99", "bert-99.9", "stable-diffusion-xl",  "dlrm-v2-99", "dlrm-v2-99.9", "retinanet", "resnet", "3d-unet-99", "3d-unet-99.9"  ]

    models = checker.MODEL_CONFIG[version]["models"]

    for category in entries:
        for division, data in entries[category].items():
            button_links = get_button_links(details, division) 
            html_table = get_table_header(division, category)
            if division == "open":
                colspan="3"
                scenario_missing_td = "<td></td><td></td><td></td>"
            else:
                colspan="2"
                scenario_missing_td = "<td></td><td></td>"

            for model in models:
                        
                if model in data:
                    html_table += f"""<tr><td class="model">{model}</td>"""
                    
                    #version = data[model]["Offline"]["version"]
                    acc_target = checker.MODEL_CONFIG[version]["accuracy-target"][model]
                    if model in checker.MODEL_CONFIG[version]["required-scenarios-datacenter"]:
                        required_scenarios_datacenter = checker.MODEL_CONFIG[version]["required-scenarios-datacenter"][model]
                    else:
                        required_scenarios_datacenter = []
                    if model in checker.MODEL_CONFIG[version]["required-scenarios-edge"]:
                        required_scenarios_edge = checker.MODEL_CONFIG[version]["required-scenarios-edge"][model]
                    else:
                        required_scenarios_edge = []

                    i = 0
                    acc_targets = []
                    key = None
                    for item in acc_target:
                        if i%2 == 0:
                            key = item
                        else:
                            acc_targets.append( (key, item))
                        i+=1

                    acc_targets_list = []
                    for item in acc_targets:
                        acc_targets_list.append(f"""{item[0]}: {round(item[1], 4)}""")
                    acc_targets_string = ", ".join(acc_targets_list)
                    html_table += f"""<td class="acc-target">{acc_targets_string}</td>"""

                    if "datacenter" in category:
                        if "Server" in data[model]:
                            if division == "open":
                                html_table += f"""<td class="accuracy">{round_dict_values(data[model]["Server"]["Accuracy"])}</td>"""
                            html_table += f"""<td class="units">{data[model]["Server"]["Performance_Units"]}</td> <td class="perf">{data[model]["Server"]["Performance_Result"]:.2f}</td>"""
                        else:
                            if "Server" in required_scenarios_datacenter: #must be open
                                html_table += scenario_missing_td
                            else:
                                html_table += f"""<td class="na" colspan="{colspan}"> N/A </td>"""

                    if "Offline" in data[model]:
                        if division == "open":
                            html_table += f"""<td class="accuracy">{round_dict_values(data[model]["Offline"]["Accuracy"])}</td>"""
                        html_table += f"""<td class="units">{data[model]["Offline"]['Performance_Units']}</td> <td class="perf">{data[model]["Offline"]["Performance_Result"]:.2f}</td>"""
                    else:
                        html_table += scenario_missing_td
                    if "edge" in category:
                        if "SingleStream" in data[model]:
                            scenario = "SingleStream"
                            if division == "open":
                                html_table += f"""<td class="accuracy">{round_dict_values(data[model][scenario]["Accuracy"])}</td>"""
                            html_table += f"""<td class="units">{data[model][scenario]["Performance_Units"]}</td> <td class="perf">{data[model][scenario]["Performance_Result"]:.2f}</td>"""
                        else:
                            if "SingleStream" in required_scenarios_edge: #must be open
                                html_table += scenario_missing_td
                            else:
                                html_table += f"""<td class="na" colspan="{colspan}"> N/A </td>"""
                        if "MultiStream" in data[model]:
                            scenario = "MultiStream"
                            if division == "open":
                                html_table += f"""<td class="accuracy">{round_dict_values(data[model][scenario]["Accuracy"])}</td>"""
                            html_table += f"""<td class="units">{data[model][scenario]["Performance_Units"]}</td> <td class="perf">{data[model][scenario]["Performance_Result"]:.2f}</td>"""
                        else:
                            if "MultiStream" in required_scenarios_edge: #must be open
                                html_table += scenario_missing_td
                            else:
                                html_table += f"""<td class="na" colspan="{colspan}"> N/A </td>"""
                else:
                    pass
                    #html_table += "<td></td> <td></td>"
                    #html_table += "<td></td> <td></td>"
                    #html_table += "</tr>"
            html_table += "</table></div>"
            sut_name = os.path.basename(details)
            tmp_path = os.path.dirname(details)
            tmp_path = os.path.dirname(tmp_path)
            submitter = os.path.basename(tmp_path)
            out_path = os.path.join(division, submitter, "results", sut_name, "README.md")
            os.makedirs(os.path.dirname(out_path), exist_ok=True)

            html_table = f"""<header class="topbar">
<div class="topbar-container">
<div class="logo">
<a href="/" style="border: none">
<svg xmlns="http://www.w3.org/2000/svg" width="107" height="32" viewBox="0 0 107 32" fill="none">
<path class="svg-text" d="M18.0112 24.3313C18.0112 27.8295 19.5479 29.9324 22.3789 29.9324C24.8053 29.9324 25.8568 28.1733 26.1803 27.1016C26.1871 27.0701 26.2054 27.0424 26.2315 27.0237C26.2577 27.005 26.2899 26.9967 26.3219 27.0004H28.1013C28.1619 27.0004 28.2024 27.0206 28.2024 27.1016C28.2024 28.4361 26.605 31.6513 22.3789 31.6513C17.9303 31.6513 15.9891 28.6181 15.9891 24.3313C15.9891 20.0445 18.3347 17.0114 22.3789 17.0114C26.7869 17.0114 28.2024 20.4489 28.2024 21.5611C28.2024 21.642 28.1619 21.6622 28.1013 21.6622H26.3219C26.2907 21.6618 26.2605 21.6519 26.2352 21.6339C26.2099 21.6158 26.1907 21.5904 26.1803 21.5611C25.877 20.6916 25.048 18.7302 22.3789 18.7302C19.5479 18.7302 18.0112 20.8331 18.0112 24.3313ZM39.3842 26.3331C39.3842 29.4876 37.5239 31.6513 34.3694 31.6513C31.1947 31.6513 29.3547 29.4876 29.3547 26.3331C29.3547 23.1585 31.1947 21.0151 34.3694 21.0151C37.5239 21.0151 39.3842 23.1788 39.3842 26.3331ZM37.4632 26.3331C37.4632 24.2303 36.3106 22.7339 34.3694 22.7339C32.4484 22.7339 31.2756 24.2303 31.2756 26.3331C31.2756 28.4361 32.4484 29.9324 34.3694 29.9324C36.3106 29.9324 37.4632 28.4361 37.4632 26.3331ZM51.7994 21.0151C50.8288 21.0151 49.5145 21.3386 48.7461 22.2284C48.645 22.3295 48.6045 22.3093 48.5034 22.2284C47.553 21.3184 46.9869 21.0151 45.5714 21.0151C44.5806 21.0151 43.5292 21.5004 43.1652 22.2284C43.1247 22.3093 42.963 22.3497 42.9225 22.2284L42.7203 21.3184C42.7001 21.2578 42.6799 21.2173 42.6192 21.2173H41.1027C41.0892 21.2165 41.0757 21.2186 41.063 21.2234C41.0504 21.2281 41.0389 21.2356 41.0294 21.2451C41.0198 21.2547 41.0124 21.2662 41.0076 21.2788C41.0028 21.2914 41.0007 21.305 41.0015 21.3184V31.3479C41.0007 31.3614 41.0028 31.3749 41.0076 31.3875C41.0124 31.4002 41.0198 31.4116 41.0294 31.4212C41.0389 31.4308 41.0504 31.4382 41.063 31.443C41.0757 31.4478 41.0892 31.4498 41.1027 31.449H42.8214C42.8349 31.4498 42.8484 31.4478 42.8611 31.443C42.8737 31.4382 42.8852 31.4308 42.8947 31.4212C42.9043 31.4116 42.9117 31.4002 42.9165 31.3875C42.9213 31.3749 42.9234 31.3614 42.9225 31.3479V25.7873C42.9225 24.21 43.4685 22.7339 45.167 22.7339C47.088 22.7339 47.4317 24.21 47.4317 25.7873V31.3479C47.4303 31.3589 47.4315 31.37 47.435 31.3805C47.4385 31.391 47.4443 31.4006 47.452 31.4086C47.452 31.4288 47.4721 31.449 47.5126 31.449H49.2516C49.2626 31.4504 49.2737 31.4493 49.2842 31.4457C49.2947 31.4422 49.3043 31.4364 49.3123 31.4288C49.3246 31.4191 49.3346 31.4069 49.3416 31.3929C49.3486 31.3789 49.3524 31.3635 49.3527 31.3479V25.7873C49.3527 24.21 49.6965 22.7339 51.5972 22.7339C53.599 22.7339 53.8619 24.2504 53.8619 25.7873V31.3479C53.8611 31.3614 53.8631 31.3749 53.8679 31.3875C53.8727 31.4002 53.8801 31.4116 53.8897 31.4212C53.8992 31.4308 53.9107 31.4382 53.9233 31.443C53.936 31.4478 53.9495 31.4498 53.963 31.449H55.6818C55.6953 31.4498 55.7088 31.4478 55.7215 31.443C55.7341 31.4382 55.7456 31.4308 55.7551 31.4212C55.7647 31.4116 55.7721 31.4002 55.7769 31.3875C55.7817 31.3749 55.7837 31.3614 55.7829 31.3479V25.7873C55.7829 22.7541 54.4281 21.0151 51.7994 21.0151ZM68.9058 21.0151C67.9351 21.0151 66.6208 21.3386 65.8524 22.2284C65.7513 22.3295 65.7109 22.3093 65.6098 22.2284C64.6594 21.3184 64.0933 21.0151 62.6778 21.0151C61.6869 21.0151 60.6355 21.5004 60.2715 22.2284C60.231 22.3093 60.0693 22.3497 60.0289 22.2284L59.8266 21.3184C59.8064 21.2578 59.7862 21.2173 59.7256 21.2173H58.209C58.1955 21.2165 58.182 21.2186 58.1693 21.2234C58.1567 21.2281 58.1452 21.2356 58.1357 21.2451C58.1261 21.2547 58.1187 21.2662 58.1139 21.2788C58.1091 21.2914 58.107 21.305 58.1079 21.3184V31.3479C58.107 31.3614 58.1091 31.3749 58.1139 31.3875C58.1187 31.4002 58.1261 31.4116 58.1357 31.4212C58.1452 31.4308 58.1567 31.4382 58.1693 31.443C58.182 31.4478 58.1955 31.4498 58.209 31.449H59.9277C59.9412 31.4498 59.9547 31.4478 59.9674 31.443C59.98 31.4382 59.9915 31.4308 60.0011 31.4212C60.0106 31.4116 60.018 31.4002 60.0228 31.3875C60.0276 31.3749 60.0297 31.3614 60.0289 31.3479V25.7873C60.0289 24.21 60.5748 22.7339 62.2734 22.7339C64.1943 22.7339 64.538 24.21 64.538 25.7873V31.3479C64.5367 31.3589 64.5378 31.37 64.5413 31.3805C64.5448 31.391 64.5506 31.4006 64.5583 31.4086C64.5583 31.4288 64.5785 31.449 64.6189 31.449H66.3579C66.3689 31.4504 66.38 31.4493 66.3906 31.4457C66.4011 31.4422 66.4107 31.4364 66.4186 31.4288C66.431 31.4191 66.441 31.4069 66.448 31.3929C66.4549 31.3789 66.4587 31.3635 66.459 31.3479V25.7873C66.459 24.21 66.8028 22.7339 68.7035 22.7339C70.7054 22.7339 70.9682 24.2504 70.9682 25.7873V31.3479C70.9674 31.3614 70.9695 31.3749 70.9743 31.3875C70.9791 31.4002 70.9865 31.4117 70.996 31.4212C71.0056 31.4308 71.0171 31.4382 71.0297 31.443C71.0424 31.4478 71.0559 31.4498 71.0694 31.449H72.7881C72.8016 31.4498 72.8151 31.4478 72.8278 31.443C72.8404 31.4382 72.8519 31.4307 72.8614 31.4212C72.871 31.4116 72.8784 31.4002 72.8832 31.3875C72.888 31.3749 72.89 31.3614 72.8892 31.3479V25.7873C72.8893 22.7541 71.5344 21.0151 68.9058 21.0151ZM84.3741 26.3331C84.3741 29.4876 82.5139 31.6513 79.3594 31.6513C76.1848 31.6513 74.3446 29.4876 74.3446 26.3331C74.3446 23.1585 76.1848 21.0151 79.3594 21.0151C82.5139 21.0151 84.3741 23.1788 84.3741 26.3331ZM82.4531 26.3331C82.4531 24.2303 81.3006 22.7339 79.3594 22.7339C77.4384 22.7339 76.2656 24.2303 76.2656 26.3331C76.2656 28.4361 77.4384 29.9324 79.3594 29.9324C81.3006 29.9324 82.4531 28.4361 82.4531 26.3331ZM90.9861 21.0151C89.6314 21.0151 88.7416 21.642 88.3372 22.2486C88.2967 22.3093 88.135 22.3497 88.1147 22.2284L87.9125 21.3184C87.8924 21.2578 87.8721 21.2173 87.8115 21.2173H86.2949C86.2814 21.2165 86.2679 21.2186 86.2552 21.2234C86.2426 21.2282 86.2311 21.2356 86.2216 21.2451C86.212 21.2547 86.2046 21.2662 86.1998 21.2788C86.195 21.2914 86.193 21.305 86.1938 21.3184V31.3479C86.193 31.3614 86.195 31.3749 86.1998 31.3875C86.2046 31.4002 86.212 31.4116 86.2216 31.4212C86.2311 31.4307 86.2426 31.4382 86.2552 31.443C86.2679 31.4478 86.2814 31.4498 86.2949 31.449H88.0136C88.0271 31.4498 88.0406 31.4478 88.0533 31.443C88.0659 31.4382 88.0774 31.4308 88.087 31.4212C88.0965 31.4117 88.1039 31.4002 88.1087 31.3875C88.1135 31.3749 88.1156 31.3614 88.1147 31.3479V25.7873C88.1147 24.21 89.0854 22.7339 90.7839 22.7339C92.7858 22.7339 93.4733 24.2504 93.4733 25.7873V31.3479C93.4724 31.3614 93.4745 31.3749 93.4793 31.3875C93.4841 31.4002 93.4915 31.4116 93.5011 31.4212C93.5106 31.4307 93.5221 31.4382 93.5347 31.443C93.5474 31.4478 93.5609 31.4498 93.5744 31.449H95.2931C95.3066 31.4498 95.3201 31.4478 95.3328 31.443C95.3454 31.4382 95.3569 31.4307 95.3664 31.4212C95.376 31.4116 95.3834 31.4002 95.3882 31.3875C95.393 31.3749 95.3951 31.3614 95.3942 31.3479V25.7873C95.3943 23.1585 93.9181 21.0151 90.9861 21.0151ZM101.501 25.3424C100.489 25.2008 99.0335 25.1806 99.0335 24.028C99.0335 23.4011 99.7009 22.7339 101.217 22.7339C102.855 22.7339 103.745 23.4618 103.745 24.574C103.744 24.5875 103.746 24.601 103.751 24.6136C103.756 24.6263 103.763 24.6377 103.773 24.6473C103.782 24.6569 103.794 24.6643 103.806 24.6691C103.819 24.6738 103.833 24.6759 103.846 24.6751H105.585C105.646 24.6751 105.666 24.6346 105.666 24.574C105.666 22.1879 103.705 21.0151 101.217 21.0151C98.71 21.0151 97.1126 22.3699 97.1126 24.028C97.1126 26.5354 99.5592 26.8387 101.501 27.0611C102.35 27.1623 104.028 27.2431 104.028 28.3957C104.028 29.71 102.532 29.9324 101.501 29.9324C99.8829 29.9324 98.8515 29.1034 98.8515 28.0924C98.8484 28.0631 98.8341 28.0361 98.8114 28.0172C98.7888 27.9983 98.7597 27.989 98.7302 27.9913H97.0318C97.0183 27.9904 97.0048 27.9925 96.9921 27.9973C96.9795 28.0021 96.968 28.0095 96.9584 28.0191C96.9489 28.0286 96.9415 28.0401 96.9367 28.0527C96.9319 28.0654 96.9298 28.0789 96.9306 28.0924C96.9306 30.0336 98.4269 31.6513 101.501 31.6513C104.028 31.6513 105.949 30.7009 105.949 28.3957C105.949 25.8074 103.523 25.6254 101.501 25.3424ZM14.6563 0.32H11.3806C11.3199 0.32 11.2795 0.340186 11.239 0.421062L7.63978 12.5535C7.6334 12.5754 7.62009 12.5946 7.60186 12.6083C7.58363 12.6219 7.56145 12.6293 7.53866 12.6293C7.51587 12.6293 7.4937 12.6219 7.47547 12.6083C7.45723 12.5946 7.44393 12.5754 7.43754 12.5535L3.83828 0.421062C3.79785 0.340186 3.75741 0.32 3.69672 0.32H0.420997C0.407509 0.319181 0.394001 0.321233 0.381365 0.326021C0.368729 0.330809 0.357253 0.338224 0.347696 0.347777C0.338138 0.357329 0.330716 0.368801 0.325921 0.381434C0.321125 0.394067 0.319065 0.407574 0.319877 0.421062V14.4543C0.319059 14.4677 0.321114 14.4813 0.325906 14.4939C0.330699 14.5065 0.338119 14.518 0.347677 14.5276C0.357236 14.5371 0.368714 14.5446 0.381353 14.5493C0.393992 14.5541 0.407505 14.5562 0.420997 14.5554H2.13972C2.15322 14.5562 2.16673 14.5541 2.17937 14.5493C2.19201 14.5445 2.20348 14.5371 2.21304 14.5276C2.2226 14.518 2.23002 14.5065 2.23481 14.4939C2.23961 14.4813 2.24166 14.4677 2.24084 14.4543V2.34206C2.24077 2.3167 2.25014 2.29222 2.26713 2.27339C2.28412 2.25456 2.30752 2.24273 2.33275 2.2402C2.35799 2.23767 2.38326 2.24463 2.40365 2.25972C2.42403 2.2748 2.43807 2.29694 2.44303 2.32181L6.00191 14.4543C6.01669 14.4846 6.03969 14.5101 6.06829 14.528C6.09689 14.5459 6.12993 14.5554 6.16366 14.5554H8.91366C8.94739 14.5554 8.98043 14.5459 9.00903 14.528C9.03763 14.5101 9.06063 14.4846 9.07541 14.4543L12.6343 2.32181C12.6545 2.22075 12.8365 2.2005 12.8365 2.34206V14.4543C12.8357 14.4677 12.8377 14.4813 12.8425 14.4939C12.8473 14.5065 12.8547 14.518 12.8643 14.5276C12.8738 14.5371 12.8853 14.5445 12.898 14.5493C12.9106 14.5541 12.9241 14.5562 12.9376 14.5554H14.6563C14.6698 14.5562 14.6833 14.5541 14.696 14.5493C14.7086 14.5445 14.7201 14.5371 14.7297 14.5276C14.7392 14.518 14.7466 14.5065 14.7514 14.4939C14.7562 14.4813 14.7583 14.4677 14.7575 14.4543V0.421062C14.7583 0.407575 14.7562 0.394069 14.7514 0.381437C14.7466 0.368804 14.7392 0.357333 14.7296 0.347781C14.7201 0.338229 14.7086 0.330814 14.696 0.326025C14.6833 0.321236 14.6698 0.319183 14.6563 0.32ZM17.3146 14.5554H27.1463C27.1598 14.5562 27.1733 14.5541 27.186 14.5493C27.1986 14.5445 27.2101 14.5371 27.2196 14.5276C27.2292 14.518 27.2366 14.5065 27.2414 14.4939C27.2462 14.4813 27.2483 14.4677 27.2474 14.4543V12.9377C27.2482 12.9242 27.2462 12.9107 27.2414 12.8981C27.2366 12.8854 27.2292 12.874 27.2196 12.8644C27.2101 12.8549 27.1986 12.8475 27.1859 12.8427C27.1733 12.8379 27.1598 12.8358 27.1463 12.8366H19.2356C19.2221 12.8374 19.2086 12.8354 19.1959 12.8306C19.1833 12.8258 19.1718 12.8184 19.1623 12.8088C19.1527 12.7993 19.1453 12.7878 19.1405 12.7751C19.1357 12.7625 19.1336 12.749 19.1344 12.7355V0.421062C19.1353 0.407578 19.1332 0.394075 19.1284 0.381446C19.1236 0.368816 19.1162 0.357346 19.1066 0.347794C19.0971 0.338243 19.0856 0.330826 19.073 0.326035C19.0604 0.321244 19.0469 0.319187 19.0334 0.32H17.3146C17.3011 0.319188 17.2876 0.321246 17.275 0.326037C17.2623 0.330829 17.2509 0.338245 17.2413 0.347797C17.2318 0.357348 17.2243 0.368818 17.2195 0.381447C17.2148 0.394077 17.2127 0.407579 17.2135 0.421062V14.4543C17.2127 14.4677 17.2147 14.4812 17.2195 14.4939C17.2243 14.5065 17.2317 14.518 17.2413 14.5276C17.2508 14.5371 17.2623 14.5445 17.2749 14.5493C17.2876 14.5541 17.3011 14.5562 17.3146 14.5554Z" fill="black"/>
<path class="svg-dot" d="M7.53727 28.5216C9.90654 28.5216 11.8272 26.6009 11.8272 24.2316C11.8272 21.8623 9.90654 19.9417 7.53727 19.9417C5.16799 19.9417 3.24731 21.8623 3.24731 24.2316C3.24731 26.6009 5.16799 28.5216 7.53727 28.5216Z" fill="#CCEBD4"/>
</svg>
</a>
</div>
</div>
</header>
<main class="resultpage">
<div class="welcome-section">
<div class="welcome-section-wrapper">
{header_table}
</div>
<div class="welcome-section-wrapper2">
{button_links}
</div>
</div>
<div class="details-container">
<div class="table-half table-striped">
<div class="table-wrapper">{accelerator_details}</div>
<div class="table-wrapper">{cpu_details}</div>
</div>
<div class="table-half table-striped">
<div class="table-wrapper">{hardware_details}</div>
<div class="table-wrapper">{network_details}</div>
</div>
<div class="table-full table-striped">
<div class="table-wrapper">{software_details}</div>
</div>
<div class="table-full table-striped">
<div class="table-wrapper">{html_table}</div>
</div>
</div>
</main>
"""

            repo_name = os.environ.get('INFERENCE_RESULTS_REPO_NAME', "mlperf_inference_test_submissions_v5.0")
            repo_branch = os.environ.get('INFERENCE_RESULTS_REPO_BRANCH', "main")
            repo_owner = os.environ.get('INFERENCE_RESULTS_REPO_OWNER', 'mlcommons')

            readme_content = f"""See the HTML preview [here](https://htmlpreview.github.io/?https://github.com/{repo_owner}/{repo_name}/blob/{repo_branch}/{division}/{submitter}/results/{sut_name}/summary.html)
{html_table}
"""

            with open(out_path, "w") as f:
                f.write(readme_content)
            html_out_path = os.path.join(division, submitter, "results", sut_name, "summary.html")
            html_header = get_header()
            html_footer = get_footer()

            html = f"""<html>
{html_header}
<body>
{html_table}
{html_footer}
</body>
</html>
"""

            with open(html_out_path, "w") as f:
                f.write(html)
            print(html_table)
            #sys.exit()
    
    

import csv
import os
from cerberus import Validator
from flask import Flask, request, render_template, jsonify

from validation_mappings.interdependencies import INTERDEPENDENCIES
# from validation_mappings.keys import STATUS, PROVIDED, VALUE, COMPOUND_ID
from validation_mappings.minimum_recommended import MINIMUM_METRICS, RECOMMENDED_METRICS
from validation_mappings.schema import SCHEMA_PORTCO
from validation_mappings.schema_fund import SCHEMA_FUND
from validation_mappings.schema_gp import SCHEMA_GP

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

def is_float(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False

def read_csv(csv_file_path: str) -> (list[dict], list[str]):
    # Open a csv reader called DictReader
    with open(csv_file_path, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)
        rows = list(csv_reader)
    return rows

def validate_provided_rows(data: list[dict]) -> list[dict]:
    not_blank_provided_rows = []
    for row in data:
        if row['STATUS'] != 'provided':
            continue
        if row['VALUE'] == "":
            print(
                f"Validation error for '{row['COMPOUND_ID']}': Value is blank, but status is marked as 'provided'."
            )
            continue
        not_blank_provided_rows.append(row)
    return not_blank_provided_rows

def get_typed_value_portco(value: str, compound_id: str):
    if value and ";" in value:
        value = value.split(";")
    elif value and "|" in value:
        value = value.split("|")
    elif SCHEMA_PORTCO.get(compound_id, {}).get("type") == "integer" and value.isnumeric():
        value = int(value)
    else:
        if is_float(value):
            value = float(value)
    return value

def get_typed_metrics_portco(data: list[dict]) -> dict:
    # Get a metrics dictionary with metrics name as keys and values with correct types.
    metrics = {}
    for row in data:
        compound_id = row['COMPOUND_ID']
        metrics[compound_id] = get_typed_value_portco(row['VALUE'], compound_id)
    return metrics

def get_typed_value_fund(value: str, compound_id: str):
    if value and ";" in value:
        value = value.split(";")
    elif value and "|" in value:
        value = value.split("|")
    elif SCHEMA_FUND.get(compound_id, {}).get("type") == "integer" and value.isnumeric():
        value = int(value)
    else:
        if is_float(value):
            value = float(value)
    return value

def get_typed_metrics_fund(data: list[dict]) -> dict:
    # Get a metrics dictionary with metrics name as keys and values with correct types.
    metrics = {}
    for row in data:
        compound_id = row['COMPOUND_ID']
        metrics[compound_id] = get_typed_value_fund(row['VALUE'], compound_id)
    return metrics

def get_typed_value_gp(value: str, compound_id: str):
    if value and ";" in value:
        value = value.split(";")
    elif value and "|" in value:
        value = value.split("|")
    elif SCHEMA_GP.get(compound_id, {}).get("type") == "integer" and value.isnumeric():
        value = int(value)
    else:
        if is_float(value):
            value = float(value)
    return value

def get_typed_metrics_gp(data: list[dict]) -> dict:
    # Get a metrics dictionary with metrics name as keys and values with correct types.
    metrics = {}
    for row in data:
        compound_id = row['COMPOUND_ID']
        metrics[compound_id] = get_typed_value_gp(row['VALUE'], compound_id)
    return metrics


def validate_interdependencies(metrics: dict):
    errors = []
    for interdependent_keys in INTERDEPENDENCIES:
        # Identify which keys are present in the current metrics
        present_keys = [key for key in interdependent_keys if key in metrics]
        missing_keys = [key for key in interdependent_keys if key not in metrics]

        # If any keys are missing, report errors for each of the present keys
        if missing_keys:
            for present_key in present_keys:
                errors.append({
                    "csv_line": None,  # You can modify this if you want to add line number info
                    "compound_id": present_key,
                    "validation_result": f"Requires the following key to be present: {', '.join(missing_keys)}"
                })
    return errors

def validate_schema_portco(metrics: dict) -> (dict, list[dict]):
    validator = Validator(SCHEMA_PORTCO)
    validated_data = {}
    errors = []

    # Validate each entry in the data
    for key, value in metrics.items():
        if validator.validate({key: value}):
            validated_data[key] = value
            print(f"{key} is valid.")
        else:
            errors.append({
                "csv_line": None,
                "compound_id": key,
                "validation_result": str(validator.errors)
            })
    return validated_data, errors

def validate_schema_fund(metrics: dict) -> (dict, list[dict]):
    validator = Validator(SCHEMA_FUND)
    validated_data = {}
    errors = []

    # Validate each entry in the data
    for key, value in metrics.items():
        if validator.validate({key: value}):
            validated_data[key] = value
            print(f"{key} is valid.")
        else:
            errors.append({
                "csv_line": None,
                "compound_id": key,
                "validation_result": str(validator.errors)
            })
    return validated_data, errors

def validate_schema_gp(metrics: dict) -> (dict, list[dict]):
    validator = Validator(SCHEMA_GP)
    validated_data = {}
    errors = []

    # Validate each entry in the data
    for key, value in metrics.items():
        if validator.validate({key: value}):
            validated_data[key] = value
            print(f"{key} is valid.")
        else:
            errors.append({
                "csv_line": None,
                "compound_id": key,
                "validation_result": str(validator.errors)
            })
    return validated_data, errors


def validate_minimum_criteria(metrics: dict):
    errors = []
    missing_keys = set(MINIMUM_METRICS) - metrics.keys()
    if missing_keys:
        errors.append({
            "csv_line": None,
            "compound_id": None,
            "validation_result": f"Missing required minimum criteria: {', '.join(missing_keys)}"
        })
    return errors

def validate_recommended_criteria(metrics: dict):
    errors = []
    missing_keys = set(RECOMMENDED_METRICS) - metrics.keys()
    if missing_keys:
        errors.append({
            "csv_line": None,
            "compound_id": None,
            "validation_result": f"Missing recommended criteria: {', '.join(missing_keys)}"
        })
    return errors


def validate_portfolio_company_csv(csv_path: str) -> list[dict]:

    rows = read_csv(csv_path)

    # Validate provided rows and apply errors as before
    provided_rows = validate_provided_rows(rows)
    metrics = get_typed_metrics_portco(provided_rows)
    

    expected_headers = ["COMPOUND_ID", "REPORTING_PERIOD", "UNIT", "VALUE", "STATUS"]
    validation_results = []

    # Check for uniformity in the number of columns
    for idx, row in enumerate(provided_rows):
        if len(row) != len(expected_headers):
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": None,  # Not applicable
                "validation_result": "Row has an incorrect number of columns.",
                "value": None  # No value for this error
            })
            continue  # Skip further validation for this row

        compound_id = row["COMPOUND_ID"]
        value = row["VALUE"]  # Extract the value for later use
        
        # Check if the compound_id is recognized in the schema
        if compound_id not in SCHEMA_PORTCO:
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": "compound_id not recognized",
                "value": None  # No value for unrecognized compound_id
            })
            continue
        
        try:
            typed_value = get_typed_value_portco(value, compound_id)
            # Mark as 'valid' if no exceptions were raised
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": "valid",
                "value": typed_value  # Include the value for valid entries
            })
        except ValueError as e:
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": str(e),  # Capture the error message
                "value": value  # Retain the original value for reference
            })

    

    # Validate interdependencies, schema, and minimum/recommended criteria
    errors = validate_interdependencies(metrics)
    validated_metrics, schema_errors = validate_schema_portco(metrics)
    errors.extend(schema_errors)

    # Collect additional errors for minimum and recommended criteria
    additional_errors = validate_minimum_criteria(validated_metrics)
    additional_errors.extend(validate_recommended_criteria(validated_metrics))

    # Combine all errors from different checks
    for error in errors:
        # Map validation errors to their respective rows
        for result in validation_results:
            if result["compound_id"] == error["compound_id"]:
                result["validation_result"] = error["validation_result"]
                if error["validation_result"] == "valid":
                    result["value"] = error["value"]  # Retain the value for valid entries
                break
    
    # Add additional errors if they are not already captured in the validation results
    for additional_error in additional_errors:
        # You may want to adjust how to associate these errors with rows
        validation_results.append({
            "csv_line": None,  # Not applicable here
            "compound_id": None,
            "validation_result": additional_error["validation_result"],
            "value": None
        })

    return validation_results

def validate_fund_csv(csv_path: str) -> list[dict]:

    rows = read_csv(csv_path)

    # Validate provided rows and apply errors as before
    provided_rows = validate_provided_rows(rows)
    metrics = get_typed_metrics_fund(provided_rows)
    

    expected_headers = ["COMPOUND_ID", "REPORTING_PERIOD", "UNIT", "VALUE", "STATUS"]
    validation_results = []

    # Check for uniformity in the number of columns
    for idx, row in enumerate(provided_rows):
        if len(row) != len(expected_headers):
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": None,  # Not applicable
                "validation_result": "Row has an incorrect number of columns.",
                "value": None  # No value for this error
            })
            continue  # Skip further validation for this row

        compound_id = row["COMPOUND_ID"]
        value = row["VALUE"]  # Extract the value for later use
        
        # Check if the compound_id is recognized in the schema
        if compound_id not in SCHEMA_FUND:
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": "compound_id not recognized",
                "value": None  # No value for unrecognized compound_id
            })
            continue
        
        try:
            typed_value = get_typed_value_fund(value, compound_id)
            # Mark as 'valid' if no exceptions were raised
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": "valid",
                "value": typed_value  # Include the value for valid entries
            })
        except ValueError as e:
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": str(e),  # Capture the error message
                "value": value  # Retain the original value for reference
            })

    

    # Validate interdependencies, schema, and minimum/recommended criteria
    #errors = validate_interdependencies(metrics)
    validated_metrics, schema_errors = validate_schema_fund(metrics)
    errors = schema_errors


    # Combine all errors from different checks
    for error in errors:
        # Map validation errors to their respective rows
        for result in validation_results:
            if result["compound_id"] == error["compound_id"]:
                result["validation_result"] = error["validation_result"]
                if error["validation_result"] == "valid":
                    result["value"] = error["value"]  # Retain the value for valid entries
                break

    return validation_results

def validate_gp_csv(csv_path: str) -> list[dict]:

    rows = read_csv(csv_path)

    # Validate provided rows and apply errors as before
    provided_rows = validate_provided_rows(rows)
    metrics = get_typed_metrics_gp(provided_rows)
    

    expected_headers = ["COMPOUND_ID", "REPORTING_PERIOD", "UNIT", "VALUE", "STATUS"]
    validation_results = []

    # Check for uniformity in the number of columns
    for idx, row in enumerate(provided_rows):
        if len(row) != len(expected_headers):
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": None,  # Not applicable
                "validation_result": "Row has an incorrect number of columns.",
                "value": None  # No value for this error
            })
            continue  # Skip further validation for this row

        compound_id = row["COMPOUND_ID"]
        value = row["VALUE"]  # Extract the value for later use
        
        # Check if the compound_id is recognized in the schema
        if compound_id not in SCHEMA_GP:
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": "compound_id not recognized",
                "value": None  # No value for unrecognized compound_id
            })
            continue
        
        try:
            typed_value = get_typed_value_gp(value, compound_id)
            # Mark as 'valid' if no exceptions were raised
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": "valid",
                "value": typed_value  # Include the value for valid entries
            })
        except ValueError as e:
            validation_results.append({
                "csv_line": idx + 1,
                "compound_id": compound_id,
                "validation_result": str(e),  # Capture the error message
                "value": value  # Retain the original value for reference
            })

    

    # Validate interdependencies, schema, and minimum/recommended criteria
    #errors = validate_interdependencies(metrics)
    validated_metrics, schema_errors = validate_schema_gp(metrics)
    errors = schema_errors


    # Combine all errors from different checks
    for error in errors:
        # Map validation errors to their respective rows
        for result in validation_results:
            if result["compound_id"] == error["compound_id"]:
                result["validation_result"] = error["validation_result"]
                if error["validation_result"] == "valid":
                    result["value"] = error["value"]  # Retain the value for valid entries
                break

    return validation_results

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check if file has a .csv extension
    if not file.filename.lower().endswith('.csv'):
        return jsonify({"error": "Invalid file type. Please upload a .csv file"}), 400

    # Save the uploaded file temporarily for delimiter and header validation
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Open the file to check delimiter and header row
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        first_line = csvfile.readline()
        
        # Check if file is comma-separated
        if ';' in first_line and ',' not in first_line:
            os.remove(file_path)  # Delete file immediately if delimiter check fails
            return jsonify({"error": "Invalid delimiter. Please upload a comma-separated CSV file."}), 400
        
        # Reset file pointer to check the headers
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        first_line = next(reader)

        # Check if the header row matches the required format
        expected_headers = ["COMPOUND_ID", "REPORTING_PERIOD", "UNIT", "VALUE", "STATUS"]
        if first_line != expected_headers:
            os.remove(file_path)  # Delete file immediately if header check fails
            return jsonify({
                "error": "Invalid header row. The CSV file must have the following columns: "
                         "COMPOUND_ID, REPORTING_PERIOD, UNIT, VALUE, STATUS."
            }), 400

    # Proceed with validation if file passes all checks
    validation_results = validate_portfolio_company_csv(file_path)

    # Delete the file after processing
    os.remove(file_path)

    # Render results as HTML table
    return render_template('validation_results.html', errors=validation_results)


@app.route('/uploadfund', methods=['POST'])
def upload_file_fund():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check if file has a .csv extension
    if not file.filename.lower().endswith('.csv'):
        return jsonify({"error": "Invalid file type. Please upload a .csv file"}), 400

    # Save the uploaded file temporarily for delimiter and header validation
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Open the file to check delimiter and header row
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        first_line = csvfile.readline()
        
        # Check if file is comma-separated
        if ';' in first_line and ',' not in first_line:
            os.remove(file_path)  # Delete file immediately if delimiter check fails
            return jsonify({"error": "Invalid delimiter. Please upload a comma-separated CSV file."}), 400
        
        # Reset file pointer to check the headers
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        first_line = next(reader)

        # Check if the header row matches the required format
        expected_headers = ["COMPOUND_ID", "REPORTING_PERIOD", "UNIT", "VALUE", "STATUS"]
        if first_line != expected_headers:
            os.remove(file_path)  # Delete file immediately if header check fails
            return jsonify({
                "error": "Invalid header row. The CSV file must have the following columns: "
                         "COMPOUND_ID, REPORTING_PERIOD, UNIT, VALUE, STATUS."
            }), 400

    # Proceed with validation if file passes all checks
    validation_results = validate_fund_csv(file_path)

    # Delete the file after processing
    os.remove(file_path)

    # Render results as HTML table
    return render_template('validation_results.html', errors=validation_results)

@app.route('/uploadgp', methods=['POST'])
def upload_file_gp():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check if file has a .csv extension
    if not file.filename.lower().endswith('.csv'):
        return jsonify({"error": "Invalid file type. Please upload a .csv file"}), 400

    # Save the uploaded file temporarily for delimiter and header validation
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Open the file to check delimiter and header row
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        first_line = csvfile.readline()
        
        # Check if file is comma-separated
        if ';' in first_line and ',' not in first_line:
            os.remove(file_path)  # Delete file immediately if delimiter check fails
            return jsonify({"error": "Invalid delimiter. Please upload a comma-separated CSV file."}), 400
        
        # Reset file pointer to check the headers
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        first_line = next(reader)

        # Check if the header row matches the required format
        expected_headers = ["COMPOUND_ID", "REPORTING_PERIOD", "UNIT", "VALUE", "STATUS"]
        if first_line != expected_headers:
            os.remove(file_path)  # Delete file immediately if header check fails
            return jsonify({
                "error": "Invalid header row. The CSV file must have the following columns: "
                         "COMPOUND_ID, REPORTING_PERIOD, UNIT, VALUE, STATUS."
            }), 400

    # Proceed with validation if file passes all checks
    validation_results = validate_gp_csv(file_path)

    # Delete the file after processing
    os.remove(file_path)

    # Render results as HTML table
    return render_template('validation_results.html', errors=validation_results)

if __name__ == '__main__':
    app.run(debug=True)

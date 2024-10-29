import csv
from cerberus import Validator

from validation_mappings.interdependencies import INTERDEPENDENCIES
from validation_mappings.keys import STATUS, PROVIDED, VALUE, COMPOUND_ID
from validation_mappings.minimum_recommended import MINIMUM_METRICS
from validation_mappings.schema import SCHEMA


def is_float(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False


def read_csv(csv_file_path: str) -> list[dict]:
    # Open a csv reader called DictReader
    with open(csv_file_path, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)
        return list(csv_reader)


def validate_provided_rows(data: list[dict]) -> list[dict]:
    not_blank_provided_rows = []
    for row in data:
        if row[STATUS] != PROVIDED:
            continue
        if row[VALUE] == "":
            print(
                f"Validation error for '{row[COMPOUND_ID]}': Value is blank, but status is marked as 'provided'."
            )
            continue
        not_blank_provided_rows.append(row)
    return not_blank_provided_rows


def get_typed_value(value: str, compound_id: str):
    if value and ";" in value:
        value = value.split(";")
    elif value and "|" in value:
        value = value.split("|")
    elif SCHEMA.get(compound_id, {}).get("type") == "integer" and value.isnumeric():
        value = int(value)
    else:
        if is_float(value):
            value = float(value)
    return value


def get_typed_metrics(data: list[dict]) -> dict:
    # Get a metrics dictionary with metrics name as keys and values with correct types.

    metrics = {}
    for row in data:
        compound_id = row[COMPOUND_ID]
        metrics[compound_id] = get_typed_value(row[VALUE], compound_id)
    return metrics


def validate_interdependencies(metrics: dict):
    for interdependent_keys in INTERDEPENDENCIES:
        present_keys = [key for key in interdependent_keys if key in metrics]
        missing_keys = [key for key in interdependent_keys if key not in metrics]
        if len(missing_keys) > 0 and len(present_keys) > 0:
            displayed_missing_keys = ",".join(missing_keys)
            displayed_present_keys = ",".join(present_keys)
            print(
                f"Validation error: value for '{displayed_present_keys}' requires that '{displayed_missing_keys}' is also provided."
            )


def validate_schema(metrics: dict) -> dict:
    validator = Validator(SCHEMA)
    validated_data = {}

    # Validate each entry in the data
    for key, value in metrics.items():
        if validator.validate({key: value}):
            validated_data[key] = value
            print(f"{key} is valid.")
        else:
            print(f"Validation error for {key}: {validator.errors}")
    return validated_data


def validate_minimum_criteria(metrics: dict):
    missing_keys = set(MINIMUM_METRICS) - metrics.keys()
    if missing_keys:
        print(
            f"Important Note: the following variables are required to be valid to meet the minimum criteria: {', '.join(missing_keys)}"
        )
    else:
        print("Note: The minimum criteria is met.")

def validate_recommended_criteria(metrics: dict):
    missing_keys = set(RECOMMENDED_METRICS) - metrics.keys()
    if missing_keys:
        print(
            f"Important Note: the following variables are required to be valid to meet the recommended criteria: {', '.join(missing_keys)}"
        )
    else:
        print("Note: The recommended criteria is met.")


def validate_portfolio_company_csv(csv_path: str):
    rows = read_csv(csv_path)

    provided_rows = validate_provided_rows(rows)
    metrics = get_typed_metrics(provided_rows)

    validate_interdependencies(metrics)
    validated_metrics = validate_schema(metrics)
    validate_minimum_criteria(validated_metrics)
    validate_recommended_criteria(validated_metrics)

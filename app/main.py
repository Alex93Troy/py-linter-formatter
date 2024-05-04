" make my format linter"

def format_linter_error(error: dict) -> dict:
    "make funk for format error"
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"), "sourse": "flake8"}

def format_single_linter_file(file_path: str, errors: list) -> dict:
    "make func for check status error and create list errors"
    return {"errors": [format_linter_error(error)
    for error in errors], "path": file_path, "status": "failed"} \
    if errors else {"path": file_path, "status": "passed"}

def format_linter_report(linter_report: dict) -> list:
    "func for format all file with errors"
    return [{"errors": [format_linter_error(file) for file in value],
             "path": key,
             "status": format_single_linter_file(key, value).get("status")}
            for (key, value) in linter_report.items()]

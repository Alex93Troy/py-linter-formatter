""" make my format linter"""

def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"), "column": error.get("column_number"),
            "message": error.get("text"), "name": error.get("code"), "sourse": "flake8"}

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"path": file_path, "status": "passed"} if not errors else\
        {"errors": [format_linter_error(error) for error in errors],
        "path": file_path, "status": "failed"}

def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [format_linter_error(file) for file in value],
             "path": key, "status": format_single_linter_file(key, value).get("status")}
            for (key, value) in linter_report.items()]

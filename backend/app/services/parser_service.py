import os
import ast
import re

SUPPORTED_EXTENSIONS = [".py", ".js", ".ts", ".java"]

IGNORE_FOLDERS = [
    "node_modules",
    "venv",
    ".git",
    "__pycache__",
    "dist",
    "build",
    "docs",
    "docs_src",
    "tests",
    ".github"
]


# =========================
# SCAN REPOSITORY
# =========================

def scan_repository(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files:

            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):

                full_path = os.path.join(root, file)

                print(full_path)

                code_files.append(full_path)

    return code_files


# =========================
# PYTHON PARSER
# =========================

def extract_python_functions(file_path):

    try:

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            source_code = file.read()

        tree = ast.parse(source_code)

        imports = extract_python_imports(tree)

        routes = extract_fastapi_routes(tree)

        calls = extract_function_calls(tree)

        functions = []

        for node in ast.walk(tree):

            # FUNCTION EXTRACTION
            if isinstance(node, ast.FunctionDef):

                end_line = getattr(node, "end_lineno", node.lineno)

                functions.append({
                    "type": "function",
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": end_line
                })

            # CLASS EXTRACTION
            elif isinstance(node, ast.ClassDef):

                end_line = getattr(node, "end_lineno", node.lineno)

                functions.append({
                    "type": "class",
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": end_line
                })

        # SAFE METADATA ITEMS

        functions.append({
            "type": "imports",
            "name": ",".join(imports),
            "start_line": 1,
            "end_line": 1
        })

        functions.append({
            "type": "routes",
            "name": str(routes),
            "start_line": 1,
            "end_line": 1
        })

        functions.append({
            "type": "function_calls",
            "name": ",".join(calls),
            "start_line": 1,
            "end_line": 1
        })

        return functions

    except Exception as e:

        print(f"Error parsing Python file {file_path}: {e}")

        return []


# =========================
# JAVASCRIPT / TYPESCRIPT PARSER
# =========================

def extract_js_ts_functions(file_path):

    try:

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            source_code = file.readlines()

        extracted_items = []

        patterns = [
            r'function\s+(\w+)\s*\(',
            r'const\s+(\w+)\s*=\s*\(?.*\)?\s*=>',
            r'let\s+(\w+)\s*=\s*\(?.*\)?\s*=>',
            r'class\s+(\w+)'
        ]

        for line_number, line in enumerate(source_code, start=1):

            for pattern in patterns:

                matches = re.search(pattern, line)

                if matches:

                    name = matches.group(1)

                    item_type = (
                        "class"
                        if "class" in pattern
                        else "function"
                    )

                    extracted_items.append({
                        "type": item_type,
                        "name": name,
                        "start_line": line_number,
                        "end_line": min(line_number + 40, len(source_code))
                    })

        return extracted_items

    except Exception as e:

        print(f"Error parsing JS/TS file {file_path}: {e}")

        return []


# =========================
# JAVA PARSER
# =========================

def extract_java_methods(file_path):

    try:

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            source_code = file.readlines()

        extracted_items = []

        patterns = [
            r'(public|private|protected)\s+\w+\s+(\w+)\s*\(',
            r'class\s+(\w+)'
        ]

        for line_number, line in enumerate(source_code, start=1):

            for pattern in patterns:

                matches = re.search(pattern, line)

                if matches:

                    if "class" in pattern:

                        name = matches.group(1)
                        item_type = "class"

                    else:

                        name = matches.group(2)
                        item_type = "method"

                    extracted_items.append({
                        "type": item_type,
                        "name": name,
                        "start_line": line_number,
                        "end_line": min(line_number + 40, len(source_code))
                    })

        return extracted_items

    except Exception as e:

        print(f"Error parsing Java file {file_path}: {e}")

        return []


# =========================
# UNIVERSAL EXTRACTOR
# =========================

def extract_code_elements(file_path):

    if file_path.endswith(".py"):

        return extract_python_functions(file_path)

    elif file_path.endswith(".js") or file_path.endswith(".ts"):

        return extract_js_ts_functions(file_path)

    elif file_path.endswith(".java"):

        return extract_java_methods(file_path)

    return []


# =========================
# PYTHON IMPORT EXTRACTOR
# =========================

def extract_python_imports(tree):

    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:

                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):

            if node.module:

                imports.append(node.module)

    return list(set(imports))


# =========================
# FASTAPI ROUTE EXTRACTOR
# =========================

def extract_fastapi_routes(tree):

    routes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            for decorator in node.decorator_list:

                if isinstance(decorator, ast.Call):

                    if hasattr(decorator.func, "attr"):

                        route_type = decorator.func.attr

                        if route_type in [
                            "get",
                            "post",
                            "put",
                            "delete"
                        ]:

                            route_path = ""

                            if decorator.args:

                                if isinstance(
                                    decorator.args[0],
                                    ast.Constant
                                ):

                                    route_path = decorator.args[0].value

                            routes.append({
                                "function": node.name,
                                "method": route_type.upper(),
                                "path": route_path
                            })

    return routes


# =========================
# FUNCTION CALL EXTRACTOR
# =========================

def extract_function_calls(tree):

    calls = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):

                calls.append(node.func.id)

            elif isinstance(node.func, ast.Attribute):

                calls.append(node.func.attr)

    return list(set(calls))

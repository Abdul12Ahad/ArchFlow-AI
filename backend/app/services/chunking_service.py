import os


def get_language(file_path):

    extension = os.path.splitext(file_path)[1]

    mapping = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java"
    }

    return mapping.get(extension, "unknown")


def create_chunks(file_path, extracted_elements):
    chunks = []

    try:

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()

        # =====================================
        # EXTRACT GLOBAL METADATA
        # =====================================
        # FULL FILE CHUNK

        imports = []
        calls = []
        routes = []

        for item in extracted_elements:

            if item["type"] == "imports":

                imports = [
                    imp.strip()
                    for imp in item["name"].split(",")
                    if imp.strip()
                ]

            elif item["type"] == "function_calls":

                calls = [
                    call.strip()
                    for call in item["name"].split(",")
                    if call.strip()
                ]

            elif item["type"] == "routes":

                routes = str(item["name"])

        # =====================================
        # BUILD CHUNKS
        # =====================================

        full_file_chunk = {
            "type": "file",
            "name": os.path.basename(file_path),
            "file_path": file_path,
            "language": get_language(file_path),
            "imports": imports if 'imports' in locals() else [],
            "calls": [],
            "routes": [],
            "code": "".join(lines[:500])
        }

        chunks.append(full_file_chunk)
        
        for element in extracted_elements:

            if element["type"] not in [
                "function",
                "class",
                "method"
            ]:
                continue

            if (
                "start_line" not in element
                or "end_line" not in element
            ):
                continue

            start = element["start_line"] - 1
            end = element["end_line"]

            code_chunk = "".join(lines[start:end])

            chunk = {
                "type": element["type"],
                "name": element["name"],
                "file_path": file_path,
                "language": get_language(file_path),
                "imports": imports,
                "calls": calls,
                "routes": routes,
                "code": code_chunk
            }

            chunks.append(chunk)

        return chunks

    except Exception as e:

        print(f"Chunking Error in {file_path}: {e}")

        return []

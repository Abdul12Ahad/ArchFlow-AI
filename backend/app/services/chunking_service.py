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
                "code": code_chunk
            }

            chunks.append(chunk)

        return chunks

    except Exception as e:

        print(f"Chunking Error in {file_path}: {e}")

        return []
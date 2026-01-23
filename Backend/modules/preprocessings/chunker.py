import re

QUESTION_PATTERN = r"(?i)(Q\s*\d+[\.\)])|(^\d+[\.\)])"

def split_into_questions(text: str) -> list:
    """
    Split cleaned text into question-wise chunks.
    """
    
    # Normalize Q formats → Q1. (consistent)
    text = re.sub(r"Q\s*[\.\-]?\s*(\d+)", r"Q\1.", text)

    # Split into: ["", "Q1.", "text", "Q2.", "text"...]
    parts = re.split(r"(Q\d+\.)", text)

    chunks = []
    current = ""

    for part in parts:
        if re.match(r"Q\d+\.", part):
            if current:
                chunks.append(current.strip())
            current = part
        else:
            current += " " + part

    if current:
        chunks.append(current.strip())

    return chunks


def smart_overlap(chunks: list, overlap_lines: int = 1) -> list:
    """
    Adds overlap only for long questions.
    - If chunk has <= 2 lines → no overlap
    - If chunk has > 2 lines → add last N lines as overlap
    """

    final_chunks = []

    for i in range(len(chunks)):
        chunk = chunks[i]

        # Convert chunk into lines for analysis
        lines = chunk.split("\n")

        # If this is NOT the first question
        if i > 0:

            prev_chunk = chunks[i - 1]
            prev_lines = prev_chunk.split("\n")

            # SMART CONDITION:
            # Only long questions get overlap
            if len(prev_lines) > 2:
                overlap = "\n".join(prev_lines[-overlap_lines:])
                chunk = overlap + "\n" + chunk

        final_chunks.append(chunk.strip())

    return final_chunks

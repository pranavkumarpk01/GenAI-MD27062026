def extract_output_text(output) -> str:
    """
    Gemini (2.5+) sometimes returns AIMessage.content as a list of content
    blocks (text parts + internal 'thought signature' metadata used for
    multi-turn tool calling) instead of a plain string. This pulls out just
    the human-readable text, in order, and joins it.
    """
    if isinstance(output, str):
        return output

    if isinstance(output, list):
        parts = []
        for block in output:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                if block.get("type") == "text" and block.get("text"):
                    parts.append(block["text"])
        return "\n".join(parts).strip() or "(no response text)"

    return str(output)

def detect_changes(source_text, main_text):
    source_lines = source_text.split("\n")
    main_lines = main_text.split("\n")

    changes = []

    for line in source_lines:
        if line.strip() and line not in main_lines:
            changes.append({
                "change": line.strip()
            })

    return changes
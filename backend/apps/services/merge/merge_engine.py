def apply_changes(main_text, changes):
    updated_text = main_text

    for change in changes:
        new_line = change.get("change")

        if new_line and new_line not in updated_text:
            updated_text += "\n" + new_line

    return updated_text
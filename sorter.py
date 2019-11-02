def sort(entries):
    sorted_entries = []

    for entry in iter(entries):
        sorted_entries = __update_sorted_entries(sorted_entries, entry)

    return sorted_entries


def __update_sorted_entries(sorted_entries, entry):
    for i in range(len(sorted_entries)):
        for e in iter(sorted_entries[i]):
            if e.key in entry.key:
                if len(entry.key) > len(e.key):
                    sorted_entries.insert(i, [entry])
                    return sorted_entries
                sorted_entries[i].append(entry)
                return sorted_entries
            if entry.key in e.key:
                break
        else:
            sorted_entries[i].append(entry)
            return sorted_entries
    sorted_entries.append([entry])
    return sorted_entries



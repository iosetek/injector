import json
from entry import Entry

invalid_format_exception = Exception("Invalid format")

class EntryLoader:
    @staticmethod
    def load_entries(filename):
        f = open(filename, 'r', encoding="utf-8")
        data = json.load(f)
        entries = []
        for e in iter(data):
            if not e["encoding"] in ["utf8", "utf16"]:
                print("Unsupported encoding type. Please choose 'utf8' or 'utf16'")
                raise InvalidEncoding
            entries += EntryLoader.__json_data_to_entries(e["entries"], e["encoding"])
        f.close()
        return entries
        

    @staticmethod
    def __json_data_to_entries(data, encoding):
        if not isinstance(data, list):
            raise invalid_format_exception
        entries = []
        for entry in iter(data):
            if not isinstance(entry, dict):
                raise invalid_format_exception
            if encoding == "utf16":
                entries.append(Entry(bytearray(entry["key"], encoding)[2:], bytearray(entry["value"], encoding)[2:], encoding, entry["adding_spaces"]))
            else:
                entries.append(Entry(bytearray(entry["key"], encoding), bytearray(entry["value"], encoding), encoding, entry["adding_spaces"]))
        return entries


class InvalidEncoding(Exception):
    pass

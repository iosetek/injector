from entry import Entry
from entry_loader import EntryLoader
import sorter

class Translator:
    def __init__(self, source, destination, fileWithEntries, keepSumControl=True):
        self.__oldFile = self.__load_old_file(source)
        not_sorted_entries = EntryLoader.load_entries(fileWithEntries)
        self.__bytes_stack = bytearray()

        if keepSumControl:
            not_sorted_entries = self.__parse_entries(not_sorted_entries)

        self.__translationEntries = sorter.sort(not_sorted_entries)


    def __parse_entries(self, entries):
        length_of_keys = 0
        length_of_values = 0

        for e in iter(entries):
            length_of_keys += len(e.key)
            length_of_values += len(e.value)

        if length_of_values > length_of_keys:
            print("Total length of entries values (%i) cannot be higher than entries keys (%i)." % (length_of_values, length_of_keys))
            raise InvalidSumControlException

        spacesLeft = length_of_keys - length_of_values

        while True:
            for i in range(len(entries)):
                if spacesLeft == 0:
                    return entries
                if entries[i].encoding == "utf8":
                    entries[i].value.append(bytearray(" ", entries[i].encoding)[0])
                    spacesLeft -= 1
                if entries[i].encoding == "utf16":
                    if spacesLeft == 1:
                        entries[i].value.append(0)
                        return entries
                    entries[i].value.append(32)
                    entries[i].value.append(0)
                    spacesLeft -= 2


    def __load_old_file(self, source):
        oldFile = open(source, "rb")
        return oldFile


    def translate(self, dest):
        byte = self.__oldFile.read(1)
        while byte != b"":
            self.__bytes_stack.append(byte[0])
            byte = self.__oldFile.read(1)

        print("Levels of entries: %i" % len(self.__translationEntries))

        for entries in iter(self.__translationEntries):
            print("Entries: %i" % len(entries))
            self.__handle_stack(entries)
        self.__print_not_found()
        self.save_new_file(dest)


    def __handle_stack(self, entries):
        current_index = 0
        while current_index < len(self.__bytes_stack):
            byte = self.__bytes_stack[current_index]
            for entry in iter(entries):
                if entry.first_key_byte() == byte:
                    if self.__does_key_match(current_index, entry.key):
                        self.__apply_entry_at_index(current_index, entry)
                        current_index += len(entry.value)
                        entries.remove(entry)
            current_index += 1


    def __does_key_match(self, index_from_stack, key):
        return self.__bytes_stack[index_from_stack:index_from_stack+len(key)] == key


    def __apply_entry_at_index(self, index, entry):
        del self.__bytes_stack[index : index+len(entry.key)]
        for i in range(len(entry.value)):
            self.__bytes_stack.insert(index + i, entry.value[i])


    def __print_not_found(self):
        print("Keys that were not located:")
        for e in iter(self.__translationEntries):
            for ee in iter(e):
                print(ee.key)


    def save_new_file(self, dest):
        # TODO: Handle error with opening file
        newFile = open(dest, "wb")
        newFile.write(self.__bytes_stack)
        newFile.close()
        self.__oldFile.close()


class InvalidSumControlException(Exception):
    pass

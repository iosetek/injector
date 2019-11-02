from translator import Translator
import sys

if len(sys.argv) != 4:
    print("The correct usage is python main.py SOURCE_PATH DEST_PATH ENTRIES_PATH.")
    exit(0)

translator = Translator(sys.argv[1], sys.argv[2], sys.argv[3])
translator.translate(sys.argv[2])


from Diary import Diary

class DiaryPersistence:

    @staticmethod
    def save_to_file(diary, filename):
        f = open(filename, "w", encoding="utf-8")
        for entry in diary.entries:
            f.write(entry + "\n")


    @staticmethod
    def load_from_file(filename):
        new_diary = Diary()
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            new_diary.entries = lines
            new_diary.counter = len(lines)
        return new_diary
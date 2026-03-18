class Diary:

    def __init__(self):
        self.entries = []
        self.counter = 0
    
    def add_entry(self, entry):
        self.entries.append(entry)
        self.counter += 1

    def remove_entry(self, entry):
        if entry in self.entries:
            self.entries.remove(entry)
            self.counter -= 1

    def save(self, filename):
        f = open(filename, "w", encoding="utf-8")
        for entry in self.entries:
            f.write(entry + "\n")
        f.close()

    def load(self, filename):
        f = open(filename, "r", encoding="utf-8")
        self.entries = f.read().splitlines()
        f.close()

    def print_statistics(self):

        average_characters = sum(len(entry) for entry in self.entries)
        count = len(self.entries)
        if count == 0:
            print("Sissekandeid pole.")
            return
        
        average_characters = average_characters / count
        print(f"Sissekannete arv: {len(self.entries)}")
        print(f"Keskmine tähemärkide arv sissekandes: {average_characters}")

    def __str__(self):
        return "\n".join(self.entries)



d = Diary()
d.add_entry("Täna oli ilus ilm.")
d.add_entry("Õppisin programmeerimist.")
d.save("diary.txt")

d.print_statistics()
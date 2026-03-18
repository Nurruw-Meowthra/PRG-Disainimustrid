class DiaryStatistics:


    def print_statistics(self):

        average_characters = sum(len(entry) for entry in self.entries)
        count = len(self.entries)
        if count == 0:
            print("Sissekandeid pole.")
            return
        
        average_characters = average_characters / count
        print(f"Sissekannete arv: {len(self.entries)}")
        print(f"Keskmine tähemärkide arv sissekandes: {round(average_characters, 2)}")
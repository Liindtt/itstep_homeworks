class Numbers:
    def __init__(self, filename: str):
        self.filename = filename
        self.lst_numbers = []

    def save_numbers(self):
        with open(f"{self.filename}.txt", "r") as filename:
            for i in filename.readlines():
                i = int(i.replace('\n', ''))
                self.lst_numbers.append(i)

    def update_numbers(self):
        pass

    










class Acer:
    def __init__(self, model, processor, ram, videocard, hard_protector, motherboard, display):
        self.model = model
        self.processor = processor
        self.ram = ram
        self.videocard = videocard
        self.hard_protector = hard_protector
        self.motherboard = motherboard
        self.display = display

    def get_info(self):
        return self.__dict__

note = Acer('Acer XS-A5', 'A9-Series 9425', 'DDR-4', 'Intel UHD Graphics', 'HDD protector', 'PRIME Z690-A', '15.6-inch')
print(note.get_info())
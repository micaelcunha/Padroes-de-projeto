class DuplicatedCode:
    def __init__(self) -> None:
        self.time: float
        self.hours: int = 0
        self.minute: int = 0

    def admit_guest(self, name: str, admission_time: str):
        self.set_time(admission_time)
        if (self.hours_less_than(10)):
            pass

    def update_admission(self, admission_id: int, name: str, admission_time: str):
        self.set_time(admission_time)
        if (self.hours_less_than(30)):
            pass

    def validate_time(self, admission_time) -> int:
        try:
            return int(admission_time.replace(":", ""))
        except:
            raise Exception("No date.")

    def set_time(self, admission_time: str) -> None:
        self.time = self.validate_time(admission_time)
        self.hours = self.time / 100
        self.minutes = self.time % 100

    def hours_less_than(self, hours: int) -> bool:
        if (self.hours < hours):
            return True
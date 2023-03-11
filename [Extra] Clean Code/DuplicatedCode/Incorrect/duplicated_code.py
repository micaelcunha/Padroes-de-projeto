class DuplicatedCode:
    def __init__(self) -> None:
        pass

    def admit_guest(self, name: str, admission_time: str):
        time: float
        hours: int = 0
        minute: int = 0

        if (not admission_time):
            try:
                time = int(admission_time.replace(":", ""))
                hours = time / 100
                minutes = time % 100
            except:
                raise Exception("No date.")
        else:
            raise Exception("No date.")

        if (hours < 10):
            pass

    def update_admission(self, admission_id: int, name: str, admission_time: str):
        time: float
        hours: int = 0
        minute: int = 0

        if (not admission_time):
            try:
                time = int(admission_time.replace(":", ""))
                hours = time / 100
                minutes = time % 100
            except:
                raise Exception("No date.")
        else:
            raise Exception("No date.")

        if (hours < 30):
            pass

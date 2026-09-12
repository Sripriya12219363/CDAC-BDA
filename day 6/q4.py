import re

class Patient:
    _patient_counter = 0
    @staticmethod
    def validate_dob_format(dob_str):
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        match = re.search(pattern, dob_str)
        if match:
            return True
        else:
            return False
    def __init__(self, name, dob):
        if not Patient.validate_dob_format(dob):
            raise ValueError(
                f"Invalid date of birth format: '{dob}'. Expected YYYY-MM-DD."
            )
        Patient._patient_counter += 1
        self.patient_id = "PAT-" + str(1000 + Patient._patient_counter)
        self.name = name
        self.dob = dob
    @classmethod
    def get_total_patients(cls):
        return cls._patient_counter
def main():
    p1 = Patient("Arham Khan", "1999-05-15")
    print(p1.patient_id)
    try:
        p2 = Patient("Lisa", "12/08/1998")
    except ValueError as e:
        print(e)
    print(Patient.get_total_patients())
main()
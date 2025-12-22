from abc import ABC, abstractmethod
from datetime import datetime


class MedicalProfessional(ABC):
    def __init__(self, name, specialization, years_experience):
        self.name = name
        self.specialization = specialization
        self.years_experience = years_experience
    
    @abstractmethod
    def perform_duty(self):
        pass
    
    def introduce(self):
        return f"I am {self.name}, {self.specialization} with {self.years_experience} years experience"


class MedicalRecordKeeper(ABC):
    def __init__(self, record_system, access_level):
        self.record_system = record_system
        self.access_level = access_level
        self.records_managed = 0
    
    @abstractmethod
    def update_record(self, patient_id, update_info):
        pass
    
    def get_access_info(self):
        return f"Access level: {self.access_level}, System: {self.record_system}"


class Doctor(MedicalProfessional):
    def __init__(self, name, specialization, years_experience, license_number, hospital):
        super().__init__(name, specialization, years_experience)
        self.license_number = license_number
        self.hospital = hospital
        self.patients_treated = 0
    
    def perform_duty(self):
        return f"Dr. {self.name} is diagnosing and treating patients"
    
    def prescribe_medication(self, patient, medication):
        self.patients_treated += 1
        return f"Dr. {self.name} prescribed {medication} to {patient}"

class Nurse(MedicalProfessional):
    def __init__(self, name, specialization, years_experience, shift, department):
        super().__init__(name, specialization, years_experience)
        self.shift = shift
        self.department = department
        self.patients_cared = 0
    
    def perform_duty(self):
        return f"Nurse {self.name} is providing patient care in {self.department}"
    
    def administer_medication(self, patient, medication):
        self.patients_cared += 1
        return f"Nurse {self.name} administered {medication} to {patient}"

class Surgeon(Doctor):
    def __init__(self, name, specialization, years_experience, license_number, hospital, surgery_type):
        super().__init__(name, specialization, years_experience, license_number, hospital)
        self.surgery_type = surgery_type
        self.surgeries_performed = 0
    
    def perform_surgery(self, patient):
        self.surgeries_performed += 1
        return f"Dr. {self.name} performed {self.surgery_type} surgery on {patient}"

class MedicalSecretary(MedicalRecordKeeper):
    def __init__(self, name, record_system, access_level, department, typing_speed):
        super().__init__(record_system, access_level)
        self.name = name
        self.department = department
        self.typing_speed = typing_speed
    
    def update_record(self, patient_id, update_info):
        self.records_managed += 1
        return f"Updated record {patient_id} with: {update_info}"
    
    def schedule_appointment(self, patient, doctor, date):
        return f"Scheduled appointment for {patient} with Dr. {doctor} on {date}"

class Pharmacist(MedicalProfessional, MedicalRecordKeeper):
    def __init__(self, name, specialization, years_experience, pharmacy_name, record_system, access_level):
        MedicalProfessional.__init__(self, name, specialization, years_experience)
        MedicalRecordKeeper.__init__(self, record_system, access_level)
        self.pharmacy_name = pharmacy_name
        self.prescriptions_filled = 0
    
    def perform_duty(self):
        return f"Pharmacist {self.name} is dispensing medications at {self.pharmacy_name}"
    
    def update_record(self, patient_id, update_info):
        self.records_managed += 1
        return f"Updated medication record for {patient_id}: {update_info}"
    
    def fill_prescription(self, patient, medication):
        self.prescriptions_filled += 1
        return f"Filled prescription for {medication} for {patient}"

class LabTechnician(MedicalRecordKeeper):
    def __init__(self, name, record_system, access_level, lab_type, certifications):
        super().__init__(record_system, access_level)
        self.name = name
        self.lab_type = lab_type
        self.certifications = certifications
        self.tests_conducted = 0
    
    def update_record(self, patient_id, update_info):
        self.records_managed += 1
        return f"Updated lab results for {patient_id}: {update_info}"
    
    def conduct_test(self, patient, test_type):
        self.tests_conducted += 1
        return f"Conducted {test_type} test for {patient}"
    
    def get_certifications(self):
        return f"Certifications: {', '.join(self.certifications)}"





#----------------------------------------------------------------------------------------------------------------------------




if __name__ == "__main__":

    
    
    doctor = Doctor("ahmad", "Cardiology", 15, "MED123", "polyclinic")
    nurse = Nurse("Ali", "ICU", 8, "Night", "Emergency")
    surgeon = Surgeon("David", "Neurosurgery", 20, "SUR456", "General Hospital", "Brain")
    secretary = MedicalSecretary("Lee", "Epic Systems", "Basic", "Cardiology", 75)
    pharmacist = Pharmacist("narin", "Clinical Pharmacy", 10, "Health Pharmacy", "PharmaSoft", "Medication")
    lab_tech = LabTechnician("samet", "LabSystem", "Results", "Blood Lab", ["MLT", "Phlebotomy"])


    
    
    professionals = [doctor, nurse, surgeon, pharmacist]
    
    print("\n\n=== POLYMORPHISM DEMONSTRATION ===")
    for professional in professionals:
        print(professional.perform_duty())
    
    print("\n=== MULTIPLE INHERITANCE DEMONSTRATION ===")
    print(pharmacist.perform_duty())
    print(pharmacist.get_access_info())
    
    print("\n=== SUPER USAGE DEMONSTRATION ===")
    print(doctor.introduce())
    print(secretary.get_access_info())
    
    print("\n\n=== METHOD IMPLEMENTATION ===")
    print(doctor.prescribe_medication("hasan Patient", "Aspirin"))
    print(nurse.administer_medication("maryam Patient", "Insulin"))
    print(surgeon.perform_surgery("Emergency Patient"))
    print(secretary.schedule_appointment("Regular Patient", "camile", "2024-01-15"))
    print(pharmacist.fill_prescription("Chronic Patient", "Metformin"))
    print(lab_tech.conduct_test("Test Patient", "Blood Count"))

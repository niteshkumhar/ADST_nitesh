hospital_departments = [
    "Cardiology",
    "Orthopedics",
    "Neurology",
    "Dermatology",
    "Pediatrics",
    "ENT",
    "General Medicine",
]

available_departments = {"Cardiology", "Neurology", "Orthopedics", "Pediatrics"}
emergency_departments = {"Cardiology", "Neurology"}

doctor_list = [
    "Dr. Tanishq Sharma (Cardiology)",
    "Dr. Jay Patel (Orthopedics)",
    "Dr. Himanshu Verma (Neurology)",
    "Dr. Hardik Gupta (Pediatrics)",
    "Dr. Teeth Mehta (General Medicine)",
    "Dr. Krishnan Iyer (ENT)",
]

available_doctors = {"Dr.Tanishq Sharma", "Dr.Jay Patel", "Dr.Himanshu Verma", "Dr.Hardik Gupta"}

patient_name = input("Enter Patient Name: ")

print("\n--- Hospital Departments Menu ---")
for i in range(len(hospital_departments)):
    print(i + 1, "-", hospital_departments[i])

req_input = input("\nEnter department numbers to request (e.g. 1, 2, 1, 4): ")
requested_departments = []
for num in req_input.split(","):
    num = num.strip()
    if num != "":
        idx = int(num) - 1
        requested_departments.append(hospital_departments[idx])

prev_input = input(
    "Enter previously visited department numbers (press enter if none): "
)
previous_departments = []
if prev_input != "":
    for num in prev_input.split(","):
        num = num.strip()
        if num != "":
            idx = int(num) - 1
            previous_departments.append(hospital_departments[idx])

print("\n--- Available Doctors List ---")
for i in range(len(doctor_list)):
    print(i + 1, "-", doctor_list[i])

doc_input = input(
    "\nEnter preferred doctor numbers in priority (e.g. 1, 2, 3): "
)
preferred_doctors = []
for num in doc_input.split(","):
    num = num.strip()
    if num != "":
        idx = int(num) - 1
        doc_name_only = doctor_list[idx].split(" (")[0]
        preferred_doctors.append(doc_name_only)

# List operations: indexing, slicing, copy, append, remove
first_doctor = preferred_doctors[0] if preferred_doctors else "None"
top_2_doctors = preferred_doctors[:2]

extra_list = preferred_doctors.copy()
extra_list.append("Dr.Dipak Joshi")
extra_list.remove("Dr.Dipak Joshi")

duplicates = []
seen = []
for d in requested_departments:
    if d in seen:
        if d not in duplicates:
            duplicates.append(d)
    else:
        seen.append(d)

req_set = set(requested_departments)
prev_set = set(previous_departments)

# Set operations
available_req_depts = req_set.intersection(available_departments)
unavailable_depts = req_set.difference(available_departments)
common_depts = req_set.intersection(prev_set)
urgent_depts = req_set.intersection(emergency_departments)

assigned_doctor = "None"
for doc in preferred_doctors:
    if doc in available_doctors:
        assigned_doctor = doc
        break

if urgent_depts:
    recommended_department = list(urgent_depts)[0]
    final_appointment_status = "Confirmed - Emergency"
elif common_depts:
    recommended_department = list(common_depts)[0]
    final_appointment_status = "Confirmed - Follow-up"
elif available_req_depts:
    recommended_department = list(available_req_depts)[0]
    final_appointment_status = "Confirmed - Regular"
else:
    recommended_department = "None"
    final_appointment_status = "Rejected - Department Not Available"

if (
    "Confirmed" in final_appointment_status
    and assigned_doctor != "None"
):
    final_appointment_status = (
        final_appointment_status + " with " + assigned_doctor
    )

print("\n--- FINAL APPOINTMENT REPORT ---")
print("Requested Departments:", requested_departments)
print("Available Departments:", list(available_departments))
print("Unavailable Departments:", list(unavailable_depts))
print("Common Departments:", list(common_depts))
print("Previous Departments:", previous_departments)
print("Emergency Departments:", list(emergency_departments))
print("Recommended Department:", recommended_department)
print("Final Appointment Status:", final_appointment_status)
print("--------------------------------")
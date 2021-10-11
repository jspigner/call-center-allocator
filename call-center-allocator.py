# Pull a list of calls 
# Pull a list of names of staff  
# Add variables (early_staff, early_calls) 
# Create a dictionary called early_allocation 
# Add variables (late_calls, late_staff)
# Create a dictionary called late_allocation 

calls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

staff = ["anna", "ben", "cherry"]
staff_count = len(staff)
early_staff = 2
early_calls = calls[:5]

early_allocation = {}
for employee in staff[:early_staff]:
  position = staff.index(employee)
  early_allocation[employee] = early_calls[position::early_staff]

print(early_allocation)

late_calls = calls[5:]
late_staff = staff[::-1]
late_allocation = {}

for employee in late_staff:
  position = late_staff.index(employee)
  late_allocation[employee] = late_calls[position::staff_count]

print(late_allocation)

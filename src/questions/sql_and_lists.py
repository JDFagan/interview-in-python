"""
# SQL Questions

# Healthcare Tables:

# dispenses
# id
# dispense_date
# patient_id

# patients
# id
# first_name

# Q1) Return following output by patient_id:
# Patient ID, Earliest Dispense Date

select
    d.patient_id
    , min(d.dispense_date)
  from dispenses d
  group by
    d.patient_id

# Q2) Return following output by patient_id:
# Patient's First Name, Earliest Dispense Date

select
    p.first_name
    , min(d.dispense_date)
  from dispenses d
    join patients p on d.patient_id = p.id
  group by
    p.id

# Q3) Return following output by patient_id even if there were no dispenses:

select
    p.first_name
    , min(d.dispense_date)
  from patients p
    left join dispenses d on p.id = d.patient_id
  group by
    p.id

# Q4) Add column first_dispense_date to Patients table

alter table patients add column first_dispense_date date

# Q5) Populate newly added column

update table patients p join (
  select
    p.id
    , min(d.dispense_date) min_dispense_date
  from patients p
    left join dispenses d on p.id = d.patient_id
  group by
    p.id) dd on p.id = dd.id
  set p.first_dispense_date = dd.min_dispense_date
"""

"""
Python Questions

# Q1) Write function that outputs string and len of string given an array of strings:

Example:
color = ['red', 'green', 'blue', 'yellow']

red 3
green 5
blue 4
yellow 6

# Q2) Can you make use of list comprehensions to yield similar result?
"""


def print_lens(list_):
    for item in list_:
        print('{} {}'.format(item, len(item)))


color = ['red', 'green', 'blue', 'yellow']
print_lens(list_=color)


# List comprehension version
def print_lens2(list_):
    [print('{} {}'.format(item, len(item))) for item in list_]


print()
print_lens2(list_=color)

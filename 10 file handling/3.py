#3.Accept contact details from the user and create a vcard that we can directly store in our mobile.

def create_vcard(name, phone, email, address, company, job_title):
    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
ORG:{company}
TITLE:{job_title}
END:VCARD
"""
    return vcard

name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
address = input("Enter address: ")
company = input("Enter company name: ")
job_title = input("Enter job title: ")

vcard = create_vcard(name, phone, email, address, company, job_title)

file_name = f"{name.replace(' ', '_')}_contact.vcf"
with open(file_name, "w") as file:
    file.write(vcard)

print(f"vCard file '{file_name}' created successfully!")

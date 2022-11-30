from decorator.decorator import input_error
from models import Contact, Phone
from sqlalchemy.sql import select
import re


@input_error
def add_contact(data, session):

    name = data[1]

    if session.query(Contact).filter_by(name=name).all():
        return f"{name} is already in the Address Book, contact's name should be unique"
    else:
        new_contact = Contact(name=name)
        session.add(new_contact)
        session.commit()

        return f"New contact {name} was added to the Address Book"


@input_error
def add_phone(data, session):

    name = data[1]
    phone = data[2]
    check_match = re.search(
        r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", phone)

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    elif not check_match:
        return "Phone should be of these formats: (00)-000-0-000 or (00)-000-00-00"

    elif check_match and session.query(Phone).filter_by(phone=phone).first():
        return f"{phone} already exists in the Address Book"

    find_id = select(Contact).where(Contact.name == name)
    result = session.execute(find_id)

    for row in result.scalars():
        new_phone = Phone(phone=phone, contact_id=int(row.id))

    session.add(new_phone)
    session.commit()

    return f"New phone {phone} was added to contact {name}"


@input_error
def add_email(data, session):

    name = data[1]
    email = data[2]

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    elif not re.search(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
        return "Email is of the wrong format"

    elif session.query(Contact).filter_by(email=email).all():
        return f"{email} already exists for contact {name}"

    session.query(Contact).filter_by(name=name).update({"email": email})
    session.commit()

    return f"Email {email} was added to contact {name}"

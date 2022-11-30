from decorator.decorator import input_error
from models import Contact, Phone
from sqlalchemy.sql import select


@input_error
def show_contact(data, session):
    name = data[1]
    result = []

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    stmt = select(Contact.id, Contact.name, Contact.email).where(
        Contact.name == name)

    for row in session.execute(stmt):
        result.append(row)

    return f"Contact id: {result[0][0]}, Contact name: {result[0][1]}, Contact email: {'No email' if not result[0][2] else result[0][2]}"


@input_error
def show_phones(data, session):
    name = data[1]
    phones = []

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    stmt = select(Phone.phone).join(
        Contact).order_by(Contact.id == Phone.contact_id).where(Contact.name == name)

    for phone in session.execute(stmt):
        phones.append(phone[0])

    return phones

from decorator.decorator import input_error
from models import Contact, Phone
import re


@input_error
def change_phone(data, session):
    name = data[1]
    old_phone = data[2]
    new_phone = data[3]

    check_match = re.search(
        r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", new_phone)

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    if not session.query(Phone).filter_by(phone=old_phone).all():
        return f"{old_phone} doesn't exist in the Address Book"

    if not check_match:
        return "Phone should be of these formats: (00)-000-0-000 or (00)-000-00-00"

    session.query(Contact).filter_by(
        name=name).update({"email": new_phone})
    session.commit()

    return f"{old_phone} for contact {name} was changed to {new_phone}"


@input_error
def change_email(data, session):
    name = data[1]
    new_email = data[2]

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    if not re.search(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", new_email):
        return "Email is of the wrong format"

    session.query(Contact).filter_by(name=name).update({"email": new_email})
    return f"{name} contact's email was changed to {new_email}"

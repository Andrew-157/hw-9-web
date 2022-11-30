from decorator.decorator import input_error
from models import Contact, Phone
from sqlalchemy.sql import select


@input_error
def delete_contact(data, session):

    name = data[1]

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    find_id = select(Contact).where(Contact.name == name)
    result = session.execute(find_id)

    for row in result.scalars():
        objects = session.query(Phone).filter_by(contact_id=row.id).all()

    if objects:
        for obj in objects:
            session.delete(obj)

        obj = session.query(Contact).filter_by(name=name).first()
        session.delete(obj)

        session.commit()

        return f"Contact {name} and his info were deleted from the Address Book"

    obj = session.query(Contact).filter_by(name=name).first()
    session.delete(obj)

    session.commit()

    return f"Contact {name} was deleted from the Address Book"


@input_error
def delete_phone(data, session):

    name = data[1]
    phone = data[2]

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    if not session.query(Phone).filter_by(phone=phone).all():
        return f"{phone} doesn't exist in the Address Book"

    obj = session.query(Phone).filter_by(phone=phone).first()
    session.delete(obj)
    session.commit()

    return f"{phone} for contact {name} was deleted from the Address Book"


@input_error
def delete_email(data, session):
    name = data[1]

    if not session.query(Contact).filter_by(name=name).all():
        return f"No such contact {name} in the Address Book"

    session.query(Contact).filter_by(name=name).update({"email": None})
    session.commit()
    return f"Email for contact {name} was deleted"

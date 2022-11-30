from functions.add_to_db import add_contact, add_email, add_phone
from functions.change_data_db import change_phone, change_email
from functions.delete_from_db import delete_contact, delete_phone, delete_email
from functions.show_data import show_contact, show_phones
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def create_session():

    engine = create_engine("sqlite:///addressbook.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


COMMANDS = {"add_contact": add_contact,
            "add_phone": add_phone,
            "add_email": add_email,
            "delete_contact": delete_contact,
            "delete_phone": delete_phone,
            "delete_email": delete_email,
            "change_phone": change_phone,
            "change_email": change_email,
            "show_contact": show_contact,
            "show_phones": show_phones}


def handler(comm):
    return COMMANDS[comm]


def main():

    session = create_session()

    while True:

        user_command = input("Enter a command: ")
        parsed = user_command.split(' ')

        command = parsed[0].lower()

        if command == 'hello':
            print('How can I help you?')

        elif command in COMMANDS.keys():
            print(handler(command)(parsed, session))

        elif command in ["goodbye", "close", "bye"]:
            print("Goodbye!")
            break

        else:
            print("NO SUCH A COMMAND")


if __name__ == '__main__':

    main()

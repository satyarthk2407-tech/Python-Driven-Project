from .logic import add_book_record

def handle_add():
    print("\n➕ ADD BOOK")
    b_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    success, msg = add_book_record(b_id, title, author)
    print(f"\n {'[✓]' if success else '[!]'} {msg}")
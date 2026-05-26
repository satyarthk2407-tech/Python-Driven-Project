from .logic import show_books

def handle_show():
    books = show_books()

    if not books:
        print("\n📭 No books available.")
        return

    print("\n📚 BOOK LIST\n" + "-"*40)

    for b_id, b in books.items():
        print(f"ID: {b_id}")
        print(f"Title: {b['title']}")
        print(f"Author: {b['author']}")
        print(f"Status: {b['status']}")
        print(f"Student: {b['student'] if b['student'] else '---'}")
        print("-"*40)
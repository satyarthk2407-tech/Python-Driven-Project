from .logic import return_book_record

def handle_return():
    print("\n📥 RETURN BOOK")
    b_id = input("Enter Book ID: ")
    date = input("Enter Return Date (YYYY-MM-DD): ")

    success, msg, fine = return_book_record(b_id, date)

    print(f"\n {'[✓]' if success else '[!]'} {msg}")
    if fine > 0:
        print(f"💰 Fine: ₹{fine}")
    else:
        print("🎉 No fine!")

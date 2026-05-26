from .logic import issue_book_record

def handle_issue():
    print("\n📤 ISSUE BOOK")
    b_id = input("Enter Book ID: ")
    student = input("Enter Student Name: ")
    date = input("Enter Issue Date (YYYY-MM-DD): ")
    days = input("Enter Days: ")

    success, msg = issue_book_record(b_id, student, date, days)
    print(f"\n {'[✓]' if success else '[!]'} {msg}")


def show_fine_notice():
    print("\n📢 FINE POLICY")
    print("-"*30)
    print("Week 1 → ₹10/day")
    print("Week 2 → ₹20/day")
    print("Week 3 → ₹60/day")
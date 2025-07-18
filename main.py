import mysql.connector
#establish connection to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        database='contact_book',
        user='root',
        password='Adarsh123@'       #workbench password
    )
#ADD contact
def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone number : ")
    email=input("Enter email:")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO contacts (name,phone,email) VALUES (%s,%s,%s)",(name,phone,email))
    conn.commit()
    print("Contact added successfully !")
    conn.close()
#display all contacts
def display_contacts():
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT name,phone,email FROM contacts")
        for row in cursor.fetchall():
            print(f"Name: {row[0]},Phone: {[1]},Email: {row[2]}")
        conn.close()
#search contact
def search_contact():
    name=input("Enter name to search:")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM contacts WHERE name=%s",(name,))
    contact=cursor.fetchone()
    if contact:
        print(f"Name: {contact[0]},Phone: {contact[1]},Email: {contact[2]}")
    else:
        print("Contact not found.")
    conn.close()
#Delete contact
def delete_contact():
    name=input("Enter name to delete: ")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE name = %s",(name,))
    conn.commit()
    print("Contact deleted successfully! ")
    conn.close()
#Main menu
def main():
    while True:
        print("\n1.Add Contact\n2.Display Contact\n3.Search Contact\n4.Delete Contact\n5.Exit")
        choice=input("Enter choice:")
        if choice =='1':
            add_contact()
        elif choice =='2':
            display_contacts()
        elif choice== '3':
          search_contact()
        elif choice=='4':
         delete_contact()
        elif choice=='5':
            print("Good Bye!")
            break
        else:
            print("Invalid choice,try again.")
main()



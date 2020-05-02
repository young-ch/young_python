
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("phone_number: ", self.phone_number)
        print("e_mail: ", self.e_mail)
        print("addr: ", self.addr)


def set_contact():
    name = input('name : ')
    phone_number = input('phone_number : ')
    e_mail = input('e_mail : ')
    addr = input('addr : ')

    contact = Contact(name, phone_number, e_mail, addr)

    return contact


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")

    menu = input('메뉴선택: ')
    return int(menu)

def delete_contact(contact_list ,name):
    for i, contract in enumerate(contact_list):
        if contract.name == name:
            del contact_list[i]

def print_contact(contact_list):
    for contract in contact_list:
        contract.print_info()

def load_contact(contact_list):
    f = open('contact.txt','wt')
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4 * i+1].rstrip('\n')
        email = lines[4 * i+2].rstrip('\n')
        addr = lines[4 * i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

def store_contact(contact_list):
    f = open('contact.txt','wt')

    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def run():
    contact_list = []

    while 1:

        menu = print_menu()
        if menu == 1:
            contract = set_contact()
            contact_list.append(contract)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input('name : ')
            delete_contact(contact_list,name)
        elif menu == 4:
            store_contact(contact_list)
            break


if __name__ == "__main__":
    run()

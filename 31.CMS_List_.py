################################################Customer management system###############################################
customer_id=[]
customer_name=[]
customer_age=[]
customer_mob=[]
#Bll start here
def addcustomer(id,name,age,mob):
    customer_id.append(id)
    customer_name.append(name)
    customer_age.append(age)
    customer_mob.append(mob)

def searchcustomer(id):
    id_index=customer_id.index(id)
    name=customer_name[id_index]
    age=customer_age[id_index]
    mob=customer_mob[id_index]
    return name,age,mob

def updatecustomer(id,name,age,mob):
    id_index=customer_id.index(id)
    customer_name[id_index]=name
    customer_age[id_index]=age
    customer_mob[id_index]=mob
    return id,name,age,mob

def deletecustomer(id):
    id_index=customer_id.index(id)
    customer_id.pop(id_index)
    customer_name.pop(id_index)
    customer_age.pop(id_index)
    customer_mob.pop(id_index)

def viewAllcustomer():
    for i in range(len(customer_id)):
        print(customer_id[i],"\t",customer_name[i],"\t",customer_age[i],"\t",customer_mob[i],"\n")





#Pl start here
while True:
    choice=input("""
    press 1 to add new customer
    press 2 to edit customer details
    press 3 to search customer
     press 4 to delete customer
    press 5 to view all customer
    
    press 6 to exit
    Enter your choice:  
    """)

    if choice=='1':
        new_id=int(input("Enter new customer id"))
        new_name=input("Enter customer name")
        new_age=int(input("Enter customer age"))
        new_mob=int(input("Enter customer number"))
        addcustomer(new_id,new_name,new_age,new_mob)

    elif choice=='2':
        search_id= int(input("Enter customer id to search"))
        search_name,search_age,search_mob= searchcustomer(search_id)
        print("The required customer details are:")
        print("id:",search_id,"name:",search_name,"age:",search_age,"mob",search_mob)


    elif choice=='3':
        edit_id=int(input("Enter customer id to edit details of customer:"))
        edit_name=input("Enter new customer name")
        edit_age=int(input("Enter updated customer age"))
        edit_mob=int(input("Enter updated customer mobile number"))
        updatecustomer(edit_id,edit_name,edit_age,edit_mob)
        print("customer details updated successfully")

    elif choice=='4':
        delete_id=int(input("Enter customer id to delete details"))
        deletecustomer(delete_id)
        print("Customer deleted successfully")

    elif choice=='5':
        print("id\t name\t age\t mob\n")
        viewAllcustomer()

    elif choice==6:
        print("Thank you for using our CMS")
        break


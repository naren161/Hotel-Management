class hotel:
  def __init__(self,menu):
    self.food_menu = menu
  def show(self):
    print(*self.food_menu)

class customer:
  def take_order(self):
    Total_items = []
    idly = []
    vada = []
    pongal = []
    while True:
      print("Enter the choice below")
      print("1-idly,2-vada,3-pongal,4-TotalBill")
      choice = int(input("enter your choice : "))
      if choice==1:
        idly_no = int(input("Enter your quantity you want : "))
        idly.append(idly_no)
        if len(idly)==0:
          Total_items.append(0)
        else:
          Total_items.append(idly_no*10)
      elif choice==2:
        vada_no = int(input("Enter the quantity you want : "))
        vada.append(vada_no)
        if len(vada)==0:
          Total_items.append(0)
        else:
          Total_items.append(vada_no*5)
      elif choice==3:
        pongal_no = int(input("Enter your quantity : "))
        pongal.append(pongal_no)
        if len(pongal)==0:
          Total_items.append(0)
        else:
          Total_items.append(pongal_no*15)
      elif choice==4:
        if len(idly)!=0:
          print("Total idly price : ",idly[0]*10)
        if len(vada)!=0:
          print("Total vada price : ",vada[0]*5)
        if len(pongal)!=0:
          print("Total pongal price : ",pongal[0]*15)
        print("Total : ",sum(Total_items))
        break
    return Total_items

  class Bill_counter:
    def Customer_billing(self,Order_details):
      self.order_details=Order_details
      print("\nYour order total:",sum(self.order_details),"\n")

bas = hotel(["idly - RS10\nvada - RS5\npongal - RS15"])
naren = customer()


        
while True:
  print("Welcome to NANBA STAR Hotel")
  print("Select the option below")
  print("1-Display the menu\n2-Take the order and Bill payment\n3-exit")
  print("------------------------------------------------------------")
  option = int(input("Enter the option : "))
  if option==1:
    bas.show()
    print("----------------------------------------------------------")
  elif option==2:
    request_order = naren.take_order()
  elif option==3:
    print("Thank you visit again")
    break

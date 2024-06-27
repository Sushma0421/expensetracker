class Expense:
    def __init__(self,date,description,amount):
      self .date=date
      self .description=description
      self .amount=amount
class ExpenseTracker:
    def __init__(self):
        self.expenses=[]
    def add_expense(self,expense):
      self.expenses.append(expense)
      def remove_expense(self,index):
          if 0<=index < len(self.expenses):
              del self.expenses[index]
              print("Expense removed successfully.")
          else:
                  print("Invalid expense index.")
                  def view_expenses(self):
                      if len(self.expense)==0:
                          print("no expense found.")
                      else:
                        print("Expense list")
                  for i,expense in enumerate(self.expenses,start=1):
                        print(f"{i}.date:{expense.date},description:{expense.description}.Amount:${expense.amount:.2f}")
    def  total_expense(self):
             total = sum(expense.amount for expense in self.expenses)
             print(f"total expenses:${total:.2f}")
    def main():
         tracker = ExpenseTracker()
         while True:
                 print("/nExpense Tracker Menu:")
                 print("1. Add Expense")
                 print("2.Remove Expense")
                 print("3.View Expenses")
                 print("4.Total Expenses")
                 print("5.Exit")

                 choice = input("Enter your choice(1-5):")

                 if choice =="1":
                    date=input("Enter the date(YYYY-MM-DD):")
                    description=input("enter the description:")
                    amount=float(input("enter the amount:"))
                    expense=Expense(date,description,amount)
                    tracker.add_expense(expense)
                    print("Expense added succesfully.")
                 elif choice == "2":
                       index = int(input("enter the expense index to remove:"))-1
                       tracker.remove_expense(index)
                 elif choice =="3":
                     tracker.view_expenses()
                 elif choice =="4":
                     tracker.total_expenses()
                 elif choice =="5":
                      print("Goodbye!!")
                      break
                 else:
                       print("Invalid choice.please try again.")

                 
    

import csv

def save_expenses():
    with open("expense.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Amount"])
        writer.writerow(["chips", 200])
        writer.writerow(["mobile", 45000])
        writer.writerow(["daal", 300])
        writer.writerow(["rice", 400])
        writer.writerow(["tea", 50])

    print("expense data saved successfully")



    
      
    
    
    
    
    
    
    
    
    
# def load_expenses():
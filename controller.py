import view
import model

def button():
    data_user = view.write_into_file()
    if "Запись" in data_user:
        model.add(data_user)
    else:
        model.search(data_user)

    
   




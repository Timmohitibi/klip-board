# store multiple stuff on my keyboard
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

#save data to json file
def save_data(filepath, data):
  with open(filepath, 'w') as f:
    json.dump(data, f)

  

  #load data from json file
  def load_data(filepath):
    try:
      with open(filepath, 'r') as f:
        data = json.load(f)
        return data
    except:
      return

   

if len(sys.argv) == 2:
  command = sys.argv[1]
  data = load_data(SAVED_DATA)

  if command == "save":
    key = input("Enter key: ")
    data[key] = clipboard.paste()
    save_data(SAVED_DATA, data)
    print("data saved")
    
  
  elif command =="load":
    key = input("Enter key: ")
    if key in data:
      clipboard.copy(data[key])
      print("data loaded")
    else:
      print("key not found")

  elif command =="list":
    print (data)

  else:
    print("Unknown command")
else:
  print("please pass exactly one command")
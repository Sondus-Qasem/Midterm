open_tabs=[] #global variables
nested_tabs={} #global variables
# Function to open a new tab
def open_tab(): #method1
  title = input("Enter the title of the website: ") # the user to input
    url = input("Enter the URL: ")
    new_tab = {"Title": title, "URL": url, "Nested Tabs": []}
    open_tabs.append(new_tab)
# Function to close a tab
def close_tab():

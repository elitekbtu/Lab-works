import os 

#task 1

path = r"C:\Users\Турарбек\Documents"
all = list(os.listdir(path))
print(all)

#task 2

def check_access(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return 
    else:
        print('path does exist')
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("don't readable")
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("don't executable")

if __name__ == "__main__":
    path_to_check = r"C:\Users\Турарбек\Documents"
    
check_access(path_to_check)

#task 3




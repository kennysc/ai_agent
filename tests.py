#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test():
    print(get_file_content("calculator", "lorem.txt"))
#    print(get_file_content("calculator", "main.py"))
#    print(get_file_content("calculator", "pkg/calculator.py"))
#    print(get_file_content("calculator", "/bin/cat"))
#    print(get_file_content("calculator", "pkg/does_not_exist.py"))
#    print("Results for current directory:")
#    print(get_files_info("calculator", "."))
#    print("")
#    
#    print("Results for 'pkg' directory:")
#    print(get_files_info("calculator", "pkg"))
#    print("")
#    
#    print("Results for '/bin' directory:")
#    print(get_files_info("calculator", "/bin"))
#    print("")
#    
#    print("Results for '../' directory:")
#    print(get_files_info("calculator", "../"))
#    print("")

if __name__== "__main__":
    test()

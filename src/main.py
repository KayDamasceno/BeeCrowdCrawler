import sys
import os
import re
sys.path.append("../page")
parent_dir = "C:\\Users\\kboin\\Documents\\CodesFromBeeCrowd\\"



from playwright.sync_api import sync_playwright
from beeCrowdPage import beeCrowdPage



def main():
    with sync_playwright() as pw:

        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        

        bc = beeCrowdPage(context)

        bc.navigate()
        
        bc.go_to_perfil()
        valid = True

        while valid:

            table =  bc.collect_table()

            for submission in table:
                current_folder = os.path.join(parent_dir,submission[0])
                #Create folder for the problem
                if not os.path.exists(current_folder):
                    os.mkdir(current_folder)

                #removing marks 
                submission[1] = re.sub(r'[^\w\s]', '', submission[1])
                #create title + extesion
                file_title = ""
                if "Python" in submission[4]:
                    file_title = submission[1]+".py"
                elif "C++" in submission[4]:
                    file_title = submission[1]+".cpp"
                elif "PostgreSQL" in submission[4]:
                    file_title = submission[1]+".txt"
                elif "Java" in submission[4]:
                    file_title = submission[1]+".java"
                elif "Kotlin" in submission[4]:
                    file_title = submission[1]+".kt"
                elif "Lua" in submission[4]:
                    file_title = submission[1]+".lua"
                elif "Haskell" in submission[4]:
                    file_title = submission[1]+".hs"
                elif submission[4] == "C" or submission[4] == "C99":
                    file_title = submission[1]+".c"

               
                code = bc.get_code(submission)
                

                with open (os.path.join(current_folder, file_title), "w") as f:
                    f.write(code)
                

            valid = bc.next_is_visible()
            if valid:
                bc.next()

        

if __name__ == '__main__':
    main()
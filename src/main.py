import sys
sys.path.append("../page")

from playwright.sync_api import sync_playwright
from beeCrowdPage import beeCrowdPage



def main():
    with sync_playwright() as pw:

        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        

        bc = beeCrowdPage(context)

        bc.navigate()
        #bc.login('kboing11@hotmail.com', '32216538')
        bc.go_to_perfil()

        table =  bc.collect_table()

        bc.get_code(table)

        

if __name__ == '__main__':
    main()
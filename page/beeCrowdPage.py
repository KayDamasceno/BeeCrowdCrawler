class beeCrowdPage:

    def __init__(self, context):
        self.context = context
        self.page = self.context.new_page()
        

    def navigate(self):
        self.page.goto("https://www.beecrowd.com.br/")

    def login(self, email, password):
        
        self.page.locator("input[name=\"email\"]").type(email)
        self.page.locator("input[name=\"password\"]").type(password)

        self.page.locator("input:has-text(\"Sign In\")").click()

        self.context.storage_state(path="state.json")

    def go_to_perfil(self):

        self.page.locator("#menu >> text=Perfil").click()
    
    def collect_table(self):

        table_values = []
        self.rows = self.page.locator("table tr")

        for i in range(1,self.rows.count()):

            self.row = self.rows.nth(i)
            table_values.append(self.row.locator("td").all_inner_texts())

        return table_values

    def get_code(self, table_values):

        self.code_page = self.context.new_page()
        self.code_page.goto("https://www.beecrowd.com.br/judge/pt/runs/code/"+table_values[3])

        lines = self.code_page.locator("[class = 'ace_line']")
        
        code = ""
        
        for j in range(0, lines.count()):
            
            code = code + lines.nth(j).all_inner_texts()[0].replace("\xa0", " ") + '\n'
            
                
        self.code_page.close()

        return code
    
    def next_is_visible(self):

        return self.page.locator("[class = 'next']").is_visible()

    def next(self):

        self.page.locator("[class = 'next']").click()


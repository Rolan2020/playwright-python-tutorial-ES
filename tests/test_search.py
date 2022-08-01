from playwright.sync_api import Page
    # Dado que se muestra la página de inicio de DuckDuckGo
    # Cuando el usuario busca una frase
    # Entonces la consulta del resultado de la búsqueda es la frase
    # Y los enlaces de los resultados de la búsqueda pertenecen a la frase
    # Y el título del resultado de la búsqueda contiene la frase
def test_basic_duckduckgo_search(page: Page) -> None:
    page.goto('https://www.duckduckgo.com')
    # clase locator, toma el selector ID y con el metodo fill introduce un texto
    page.locator('#search_form_input_homepage').fill('panda')
    # seleccionar el boton de busqueda y hacer click con con el metodo 'click()' 
    page.locator('#search_button_homepage').click()
    
    pass
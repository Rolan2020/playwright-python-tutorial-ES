> En Playwright, también puede esperar otros eventos de página como éste:

```python
def test_basic_duckduckgo_search(page):
    # Dado que se muestra la página de inicio de DuckDuckGo
    page.goto('https://www.duckduckgo.com', wait_until='networkidle')
```

> ejecuta pruebas de la carpeta tets, en modo headed y en slow motion de 1 seg
`$ python3 -m pytest tests --headed --slowmo 1000`
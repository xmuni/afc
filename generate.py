from jinja2 import Template, Environment, FileSystemLoader

def save_html(path, text):
    file = open(path, 'w', encoding='UTF-8')
    file.write(text)
    file.close()

# Takes 'home.html' or 'gallery.html' or any other html file containing the main block
# And the dictionary of replacements
def render_page(main_html, dictionary):
    env = Environment(loader=FileSystemLoader('./sources/'))
    template = env.get_template(main_html)
    html_text = template.render(dictionary)
    return html_text
    # save_html(dictionary['name']+'.html', html_text)


replacements_it_home = {
    'language': 'it',
    'name': 'index',
    'select_home': True,
    'title': 'Antica Fornace Carraro',
    'bodytext': 'Body text goes here',
    'navbutton_home': "Fornace",
    'navbutton_gallery': "Gallery",
    'navbutton_catalog': "Catalogo",
    'navbutton_about': "Contatti",
    'intro_heading': 'AFC descrizione',
    'intro_paragraph': 'L’Antica Fornace Carraro rappresenta un autentico baluardo dell’artigianato piovese, continuando a produrre ininterrottamente dall’Ottocento cotto di altissima qualità. La realizzazione avviene tuttora secondo le antiche tecniche produttive, utilizzando solamente argilla locale e rispettando i lenti ritmi produttivi. Le argille utilizzate vengono raccolte nei territori circostanti e i mattoni prodotti sono sottoposti ad essiccazione per tutta l’estate nelle aie all’aperto. In autunno invece, i mattoni vengono cotti nell’antico forno Hoffmann ottocentesco, autentico fulcro del complesso. Il prodotto finale si distingue nel mondo per la sua indiscussa qualità, mantenendo così vivi i saperi secolari della produzione di laterizi.',
}
html = render_page('home.html', replacements_it_home)
save_html('it/index.html', html)
save_html('./index.html', html)


replacements_en_home = {
    'language': 'en',
    'name': 'index',
    'select_home': True,
    'title': 'Antica Fornace Carraro',
    'bodytext': 'Body text goes here',
    'navbutton_home': "Home",
    'navbutton_gallery': "Gallery",
    'navbutton_catalog': "Catalogue",
    'navbutton_about': "About",
    'intro_heading': 'AFC description',
    'intro_paragraph': 'Antica Fornace Carraro is an authentic bulwark of the craftsmanship of Rainforest, continuing to produce uninterruptedly since the nineteenth century terracotta of the highest quality. The realization still takes place according to ancient production techniques, using only local clay and respecting the slow pace of production. The clays used are collected in the surrounding areas and the bricks produced are dried throughout the summer in the open-air farmyards. In autumn, however, the bricks are baked in the old nineteenth-century Hoffmann oven, the real heart of the complex. The final product stands out in the world for its undisputed quality, thus keeping alive the centuries-old knowledge of brick production.',
}
html = render_page('home.html', replacements_en_home)
save_html('en/index.html', html)


print("Done")
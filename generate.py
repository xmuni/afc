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
    'navbutton_catalog': "Catalog",
    'navbutton_about': "About",
}
html = render_page('home.html', replacements_en_home)
save_html('en/index.html', html)


print("Done")
from jinja2 import Template, Environment, FileSystemLoader

def save_html(path, text):
    file = open(path, 'w', encoding='UTF-8')
    file.write(text)
    file.close()

replacements_home = {
    'select_home': True,
    'title': 'Antica Fornace Carraro',
    'bodytext': 'Body text goes here',
    'navbutton_home': "Fornace",
    'navbutton_gallery': "Gallery",
    'navbutton_catalog': "Catalogo",
    'navbutton_about': "Contatti",
}

print(replacements_home,'\n')

env = Environment(loader=FileSystemLoader('./sources/'))
template = env.get_template('home.html')
result = template.render(replacements_home, language="it")
# print(result)
save_html('index.html', result)
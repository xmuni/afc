from jinja2 import Template, Environment, FileSystemLoader


replacements_home = {
    'title': 'Antica Fornace Carraro',
    'bodytext': 'Body text goes here'
}

print(replacements_home,'\n')

env = Environment(loader=FileSystemLoader('./sources/'))
template = env.get_template('home.html')
result = template.render(replacements_home, language="it")
print(result)

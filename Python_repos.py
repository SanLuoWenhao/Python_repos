
import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

Json_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
res = requests.get(Json_url)
print('Status code: {}'.format(res.status_code))

response_dict = res.json()
# print(response_dict)
print(response_dict.keys())
print('Total repositories: {}'.format(response_dict['total_count']))

repo_dicts = response_dict['items']
print('Repositories returned: {}'.format(len(repo_dicts)))

# for item in response_dict['items']:
#     print(item)

# repo_dict = repo_dicts[0]
# for key in repo_dict:
#     print(key)

names = []
owner = []
stars = []
repositoies_link = []
descriptation = []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    print(plot_dict)
    plot_dicts.append(plot_dict)

print(plot_dicts)
# print(len(names), names)
# print(len(owner), owner)
# print(len(stars), stars)
# print(len(repositoies_link), repositoies_link)
# print(len(descriptation), descriptation)

# 第一种方法
# my_style = LS('#333366', base_style=LCS)
# bar_chart = pygal.Bar(style=my_style, show_legend=False, x_label_rotation=45)
# bar_chart.title = 'Most-Star Python Projects on Github'
# bar_chart.x_labels = names
# bar_chart.add('Stars', stars)
# bar_chart.render_to_file('python_repo.svg')

# 第二张方法
# my_style = LS('#333366', base_style=LCS)
#
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 24
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
# bar_chart = pygal.Bar(my_config, style=my_style)
# bar_chart.title = 'Most-Star Python Projects on Github'
# bar_chart.x_labels = names
# bar_chart.add('', stars)
# bar_chart.render_to_file('python_repo.svg')

# 第三种方法
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

bar_chart = pygal.Bar(my_config, style=my_style)
bar_chart.title = 'Most-Star Python Projects on Github'
bar_chart.x_labels = names
bar_chart.add('Star', plot_dicts)
bar_chart.render_to_file('python_repo.svg')
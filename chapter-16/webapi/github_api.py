import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/users/annilq"
r = requests.get(url,auth=('annilq', '123456liu'))
response = r.json()
my_followers_url = response["followers_url"]
# 关注我的人
followers_response = requests.get(my_followers_url,auth=('annilq', '123456liu'))
followers_data = followers_response.json()
# 关注我的人同时又被关注的人的列表
followers_arr, my_users = [], []
for my_follower in followers_data:
    # 关注我的人的姓名
    other_follower_name = my_follower["login"]
    my_users.append(other_follower_name)
    # 关注我的人又被谁关注
    other_follower_url = my_follower["followers_url"]
    other_follower_response = requests.get(other_follower_url,auth=('annilq', '123456liu'))
    other_follower_data = other_follower_response.json()
    # 关注我的人同时被关注的列表
    users = []
    print("fetch....")
    for user in other_follower_data:
        users.append(user["login"])
    followers_arr.append(len(users))
print("over")
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = my_users
chart.add('', followers_arr)
chart.render_to_file('python_repos.svg')

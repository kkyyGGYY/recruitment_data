import json, requests, time
import pandas as pd

def get_urls():
	urls = []
	for i in range(0,37):
		i = i * 20
		time.sleep(5)
		url = 'http://zhaopin.baidu.com/api/quanzhiasync?query=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&sort_type=1&city_sug=%E4%B8%8A%E6%B5%B7&detailmode=close&rn=20&pn=' + str(i)
		urls.append(url)
	return urls

def get_contents():
	officialname = []  # 公司名称
	name = [] # 职位
	ori_education = [] # 学历
	experience = [] # 经验年限
	salary = [] # 薪资
	description = [] # 岗位要求
	contents = {}

	for url in get_urls():
		res = requests.get(url)
		jd = json.loads(res.text)
		information = jd['data']['main']['data']['disp_data']
		time.sleep(5)
		for i in range(0,20):
			officialname.append(information[i]['officialname'])
			name.append(information[i]['name'])
			ori_education.append(information[i]['ori_education'])
			experience.append(information[i]['experience'])
			salary.append(information[i]['salary'])
			description.append(information[i]['description'])

	contents['公司名称'] = officialname
	contents['职位'] = name
	contents['学历'] = ori_education
	contents['经验年限'] = experience
	contents['薪资'] = salary
	contents['岗位要求'] = description

	df = pd.DataFrame(contents, columns=['公司名称', '职位', '学历', '经验年限', '薪资', '岗位要求'])
	df.to_excel('data.xlsx')

get_contents()
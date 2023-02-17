import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return requests.get(url)

def extract(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup.find_all('article', class_ = 'Box-row')

def transform(html_repos):
    html_text = []
    for row in html_repos:
        repos_name = ''.join(row.find('h1', class_ = 'h3 lh-condensed').text.split())
        developer_name = row.find('img', class_ = 'avatar mb-1 avatar-user')['alt']
        star = ' '.join(row.find('span', class_ = 'd-inline-block float-sm-right').text.split())
        dic = {'developer': developer_name, 'repository_name': repos_name, 'nbr_stars': star}
        html_text.append(dic)
    return html_text

def format(repositories_data):
    ans = ''
    fline = 'Developer, Repository Name, Number of Stars\n'
    lngth = len(repositories_data)
    i = 0
    oneline = ''
    while i < lngth:
        oneline += repositories_data[i]['developer'] + ", "
        oneline += repositories_data[i]['repository_name'] + ", "
        oneline += repositories_data[i]['nbr_stars'] + '\n'
        i += 1
    ans = fline + oneline
    return ans

def main():
    url = "https://github.com/trending"
    page = request_github_trending(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos)
    print(format(repositories_data))

if __name__ == "__main__":
    main()
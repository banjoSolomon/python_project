import requests
url = "https://cdn.britannica.com/31/183231-050-8D8EB720/Carli-Lloyd-penalty-goal-semifinal-match-Germany-2015.jpg"
r = requests.get(url)
#date = r.json()
#print(date)

with open('britannica.png', mode= 'wb') as mf:
    mf.write(r.content)
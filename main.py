## you should install github API first:
# pip install PyGithub

# with this code you grab python code from specific day until today.
from github import Github
from datetime import datetime
import time
import os




g = Github('***') #here you pu your github token
# see rescurce to learn more about github token

end_time = time.time()
end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
start_time = time.time() - 86400
start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
id=0
for i in range(3): #The number 3 means that all python 
  				   #code will be grabed from 3 day ago
    try:
        query =  f"language:python created:{start_time_str}..{end_time_str}"
        end_time = start_time
        start_time -= 86400
        start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
        end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')

        result  = g.search_repositories(query)
        id=0
        for repo in result:
            id+=1
            os.system(f'git clone {repo.clone_url} repo/{repo.owner.login}/{repo.name}_{id}')


        


from django.shortcuts import render,redirect
from .InstaTools.InstaFunctions import *
from selenium import webdriver
import yaml
from InstaWinner.settings import STATICFILES_DIRS

# Create your views here.

likers = []
global_followers = []
driver_url = str(STATICFILES_DIRS[0])+"/chromedriver"
base_url = str(STATICFILES_DIRS[0])+"/base.yaml"
driver = None 
profile = None 

def main(request):
    ctx = {}
    return render(request,'base.html',context = ctx )

def log_in(request):
    global driver 
    global base_url 
    global driver_url
    global profile 
    with open(base_url,'r') as file : 
        data = yaml.load(file)
        username = data.get('username')
        password = data.get('password')
    driver = webdriver.Chrome(executable_path=driver_url)
    account = login(driver,username,password)
    profile = get_profile(driver)
    return redirect('Main')




def followers(request):
    global global_followers 
    ctx = {'followers':global_followers}
    return render(request,'followers.html',context = ctx)

def populate_followers(request):
    global profile
    global driver
    global global_followers
    list_followers = []
    my_driver,follower_list  = get_followers(profile)
    for follower in follower_list :
        list_followers.append(follower.text)
    driver = my_driver
    global_followers = list_followers
    return redirect('Followers')

def likers(request):
    global likers
    ctx = {'likers':likers}
    return render(request,'likers.html',context=ctx)

def populate_likers(request):
    global likers
    global driver
    global global_followers
    my_driver = driver 
    tmp_list = []
    if request.method == "POST" and 'winner' in request.POST:
        post = request.POST['post_url']
        select_winner(my_driver,post,global_followers)
        driver = my_driver
    elif request.method == 'POST' and 'likers' in request.POST : 
        post = request.POST['post_url']
        my_driver,list_liker = get_likers(my_driver,post)
        for liker in list_liker : 
            tmp_list.append(liker.text)
        likers = tmp_list
        driver  = my_driver
    return redirect('Likers')

def settings(request):

    return render(request,'settings.html')
def login_settings(request):
    user,passwd = None,None
    if request.method == 'POST' :
        user = request.POST['username']
        passwd = request.POST['password']
        base_url = str(STATICFILES_DIRS[0])+"/base.yaml"
        data = dict(username=user,password = passwd)
        def quoted_presenter(dumper, data):
                return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
        with open(base_url,'w') as file :
            	yaml.dump(data,file,default_flow_style=False)
    return redirect('Settings')
def code(request):
    user,passwd = None,None
    if request.method == 'POST' :
        security_code = request.POST['security_code']
        base_url = str(STATICFILES_DIRS[0])+"/security.yaml"
        data = dict(code=str(security_code))
        def quoted_presenter(dumper, data):
                return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
        with open(base_url,'w') as file :
            	yaml.dump(data,file,default_flow_style=False)
    return redirect('Settings')

def home(request):
    global driver
    my_driver = driver 
    my_driver.get('https://www.instagram.com/')
    driver = my_driver

    return redirect('Main')
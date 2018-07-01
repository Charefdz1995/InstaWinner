from django.shortcuts import render,redirect
from .InstaTools.InstaFunctions import *
from selenium import webdriver
import yaml
from InstaWinner.settings import STATICFILES_DIRS

# Create your views here.

likers = []


def main(request):
    ctx = {}
    return render(request,'base.html',context = ctx )

def followers(request):
    driver_url = str(STATICFILES_DIRS[0])+"/chromedriver"
    base_url = str(STATICFILES_DIRS[0])+"/base.yaml"
    username , password = None , None
    with open(base_url,'r') as file :
        data = yaml.load(file)
        username = data.get('username')
        password = data.get('password')

    driver = webdriver.Chrome(executable_path=driver_url)
    followers = []
    log_in = login(driver,username,password)
    profile = get_profile(driver)
    follower_list  = get_followers(driver)
    for follower in follower_list :
        followers.append(follower.text)
    driver.close()
    ctx = {'followers':followers}
    return render(request,'followers.html',context = ctx)


def likers(request):
    global likers
    ctx = {'likers':likers}
    return render(request,'likers.html',context=ctx)

def populate_likers(request):
    global likers
    list = []
    if request.method == "POST":
        post = request.POST['post_url']
        driver_url = str(STATICFILES_DIRS[0])+"/chromedriver"
        base_url = str(STATICFILES_DIRS[0])+"/base.yaml"
        username , password = None , None
        with open(base_url,'r') as file :
            data = yaml.load(file)
            username = data.get('username')
            password = data.get('password')

        driver = webdriver.Chrome(executable_path=driver_url)
        log_in = login(driver,username,password)
        liker_list = get_likers(log_in,post)
        for liker in liker_list:
            list.append(liker.text)
        driver.close()
        likers = list
        print(len(likers))
        print(len(list))
    return redirect('Likers')

from selenium import webdriver
import time
import random
import json
import instaloader
from selenium.common.exceptions import NoSuchElementException
import instaloader




jokes = ["How does a rabbi make coffee? Hebrews it!","Rest in peace boiling water. You will be mist!","How do you throw a space party? You planet!","Want to hear a construction joke? Oh never mind, I'm still working on that one.","Why don't scientists trust atoms? Because they make up everything!",
"I hate Russian dolls… they're so full of themselves!",
"Talk is cheap? Have you ever talked to a lawyer?",
"Why did the gym close down? It just didn't work out!",
"Two artists had an art contest. It ended in a draw!",
"A plateau is the highest form of flattery.",
"I have a fear of speed bumps. But I am slowly getting over it.",
"You can only get spoiled milk from a pampered cow.",
"What do you call a boomerang that doesn't come back? A stick!",
"You know what I saw today? Everything I looked at.",
"What are shark's two most favorite words? Man overboard!",
"If we shouldn't eat at night, why do they put a light in the fridge?",
"Have you ever tried eating a clock? It's really time-consuming, especially if you go for seconds.",
"Why are ghosts such bad liars? Because they are easy to see through.",
"It's cleaning day so naturally, I've already polished off a whole chocolate bar.",
"What did the buffalo say when his son left for college? Bison!",
"Here, I bought you a calendar. Your days are numbered now.",
"Where do fish sleep? In the riverbed.",
"What did one plate say to his friend? Tonight, dinner's on me!",
"Where are average things manufactured? The satisfactory.",
"I tried to sure the airport for misplacing my luggage. I lost my case.",
"What kind of exercise do lazy people do? Diddly-squats.",
"What do you call a pony with a cough? A little horse!",
"What is Forest Gump's password? 1Forest1.",
"Why did the M&amp;M go to school? He wanted to be a Smartie.",
"What did one traffic light say to the other? Stop looking! I am changing!",
"What do you call bears with no ears? B.",
"What's a foot long and slippery? A slipper!",
"Why do French people eat snails? They don't like fast food!",
"What's red and moves up and down? A tomato in an elevator!",
"I invented a new word today. Plagiarism.",
"What is sticky and brown? A stick!",
"Why doesn't the sun go to college? Because it has a million degrees!",
"I was wondering why the frisbee was getting bigger, then it hit me.",
"I have many jokes about unemployed people, sadly none of them work.",
"What do you call a singing laptop? A Dell!",
"Why was six afraid of seven? Because seven ate nine.",
"Why are skeletons so calm? Because nothing gets under their skin.",
"How do trees get online? They just log on!",
"Some people think prison is one word…but to robbers it's the whole sentence.",
"Where does the sheep get his hair cut? The baa baa shop!",
"Why did the orange stop? It ran out of juice!",
"I never make mistakes. …I thought I did once; but I was wrong.",
"What dd the man in the moon do when his hair got too long? Eclipse it!",
"What did 0 say to 8? Nice belt!",
]
emojies =["😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊","😋","😎","😍","😘","😗","😙","😚","☺️","🙂","🤗","🤩","🤔","🤨","😐","😑","😶","🙄","😏","😣","😥","😮","🤐","😯","😪","😫","😴","😌","😛","😜","😝","🤤","😒","😓","😔","😕","🙃","🤑","😲","☹️","🙁","😖","😞","😟","😤","😢","😭","😦","😧","😨","😩","🤯","😬","😰","😱","😳","🤪","😵"]

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver2 = webdriver.Firefox(executable_path=r'geckodriver.exe')
starttime=time.time()
L = instaloader.Instaloader()



def get_followers():
    try:
        driver2.get("https://instastatistics.com/#!/imprudhvim")
        time.sleep(30)
        pre = driver2.find_element_by_class_name("odometer-inside")
        count = pre.text
        finalCount = int((count.replace("\n", "")[0:3]))
        print("1:",finalCount)
        return finalCount
    except:
        looped =1

def get_followers2():
    try:
        driver2.get("view-source:https://www.instagram.com/imprudhvim/?__a=1")
        time.sleep(30)
        pre = driver2.find_element_by_tag_name("pre").text
        data = json.loads(pre)
        graphql = data['graphql']
        user  = graphql['user']
        followedby = user["edge_followed_by"]
        followers = followedby['count']
        print("2:",followers)
        return followers
    except:
        looped =2

def get_followers3():
    try:
        time.sleep(30)
        profile = instaloader.Profile.from_username(L.context, "imprudhvim")
        print("3:",profile.followers)
        return (profile.followers)
    except ConnectionException:
        looped =0

followers = get_followers2()
print(followers)
time.sleep(1)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(2)


username = driver.find_element_by_name("username")
username.send_keys("")

password = driver.find_element_by_name("password")
password.send_keys("")
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
looped = 0

while True:
    if((driver.current_url)=="https://www.instagram.com/" or "https://www.instagram.com/accounts/edit/" or "https://www.instagram.com/?hl=en"):
        print("minutes since started :",(starttime-time.time())/60)
        if(looped ==0):
            update_followers = get_followers()
            looped =1
        elif(looped==1):
            update_followers = get_followers2()
            looped = 2
        elif(looped==2):
            update_followers = get_followers3()
            looped =0
        if (followers and update_followers != None):
            if(int(followers)!=int(update_followers)):
                driver.get('https://www.instagram.com/accounts/edit/')
                if((driver.current_url)=="https://www.instagram.com/accounts/edit/"):
                    time.sleep(1)
                    bio = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea")
                    bio.clear()
                    jokeselected = jokes[random.randint(0,49)]
                    emoji = emojies[random.randint(0,len(emojies)-2)]
                    emoji2 = emojies[random.randint(0, len(emojies) - 2)]
                    print(emoji)
                    print(emoji2)
                    bio.send_keys(emoji," Realtime Followers : ",update_followers,"\n",emoji2," AJoke4U : ",jokeselected)
                    print(emoji," Realtime Followers : ",update_followers,"\n",emoji2," AJoke4U : ",jokeselected)
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button[1]").click()
                    followers = update_followers

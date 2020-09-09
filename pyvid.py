import time
from selenium import webdriver

#Muting all audio
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
#Create the ChromDriver and click the login button
driver = webdriver.Chrome('/Users/awesometim1/Music/chromedriver',chrome_options = chrome_options)
driver.get('http://testout.com');

def logIn():
    
    login = driver.find_element_by_id('logIn')
    login.click()
    time.sleep(2) 
    #User ID Input
    print "input user ID"
    userid = raw_input()
    #User PW Input
    print "input password"
    pw = raw_input()
    #Find username field and send the username
    idfield = driver.find_element_by_id('tbLogin')
    idfield.click()
    idfield.send_keys(userid)
    #Find password field and send the password
    pwfield = driver.find_element_by_id('tbPassword')
    pwfield.click()
    pwfield.send_keys(pw)
    #LOGIN
    driver.find_element_by_id('tb').click()
    time.sleep(3)
    #Which class?
    print "Which Course?\nOptions are:\nNetwork, PC Pro, Security"
    course =  raw_input()
    print "How many videos to watch? or type test if you want it to take tests automatically."
    choice = raw_input()
    #Default Setting
    course_default = driver.find_element_by_id("im")
    course_choice = driver.find_element_by_id("im")
    allimgs = driver.find_elements_by_tag_name("img")
    #Finding the Image tags and clicking on it to access the course
    for img in allimgs:
    	if course in img.get_attribute("alt"):
    		course_choice = img
    if course_default != course_choice:
    	course_choice.click()
    else:
    	course_default.click()

    #Choice between videos or test
    if choice.isdigit():
    	watchVideos(int(choice))
    elif choice == "test":
    	takeTest()
    else:
    	print "Invalid option"

def watchVideos(v_times):
	while(v_times > 0):
			time.sleep(3)
			#ALL THIS FOR A PLAY BUTTON!!!
			#Find all the DIVS and separate out the main panels(theres 3. very annoying..)
			panels = []
			mainPanel = 0
			playBtn = 0
			allPanels = driver.find_elements_by_tag_name("div")
			for div in allPanels:
				if "cInner.Panel.Panel" in div.get_attribute("id") and len(div.get_attribute("id"))<20:
					panels.append(div)
			#Panel comparison with css value of "left" the one in the middle has the middle value
			pn1,pn2,pn3=panels
			pn1v,pn2v,pn3v,= pn1.value_of_css_property("left"),pn2.value_of_css_property("left"),pn3.value_of_css_property("left")
			if pn1v > pn2v and pn1v > pn3v:
				mainPanel = pn1
			elif pn2v > pn3v:
				mainPanel = pn2
			else:
				mainPanel = pn3
			#Find play Button
			print mainPanel
			for div in mainPanel.find_elements_by_xpath(".//*"):
				if "spPlay" in div.get_attribute("id"):
					playBtn = div
					break
			if not (str(playBtn).isdigit()):
				playBtn.click()
				time.sleep(1)
				#Time text changes around and some divs have empty content. Set max time to the one with innerhtml (time text).
				max_time = driver.find_elements_by_tag_name("div")
				for times in mainPanel.find_elements_by_xpath(".//*"):
					if "tbTime" in times.get_attribute("id") and len(times.get_attribute('innerHTML')) > 1:
						max_time = times
						break
				max_time = max_time.get_attribute("innerHTML")
				print max_time
				max_time = max_time.split("/")[1].strip().split(":")
				max_time = int((int(max_time[0].encode())*60)+int(max_time[1].encode()))
				print max_time
				time.sleep(max_time)
				v_times = v_times-1
				nextVid = driver.find_element_by_id("bRightNav.Image")
				nextVid.click()
			else:
				nextVid = driver.find_element_by_id("bRightNav.Image")
				nextVid.click()
# def takeTest():
# 	taken = False
# 	while(taken == False):
# 			answers = []
# 			time.sleep(3)
# 			#Find all the DIVS and separate out the main panels(theres 3. very annoying..)
# 			panels = []
# 			mainPanel = 0
# 			startBtn = 0
# 			allPanels = driver.find_elements_by_tag_name("div")
# 			for div in allPanels:
# 				if "cInner.Panel.Panel" in div.get_attribute("id") and len(div.get_attribute("id"))<20:
# 					panels.append(div)
# 			#Panel comparison with css value of "left" the one in the middle has the middle value
# 			pn1,pn2,pn3=panels
# 			pn1v,pn2v,pn3v,=pn1.value_of_css_property("left"),pn2.value_of_css_property("left"),pn3.value_of_css_property("left")
# 			if pn1v > pn2v and pn1v > pn3v:
# 				mainPanel = pn1
# 			elif pn2v > pn3v:
# 				mainPanel = pn2
# 			else:
# 				mainPanel = pn3
# 			for div in mainPanel.find_elements_by_xpath(".//*"):
# 				if "btnStartExam" in div.get_attribute("id") and "Start Exam" in div.get_attribute(innerHTML):
# 					startBtn = div
# 					break
# 			if (playBtn!=0):
# 				startBtn.click()
# 				time.sleep(2)
# 				#Time text changes around and some divs have empty content. Set max time to the one with innerhtml (time text).
# 				choices = driver.find_elements_by_tag_name("div")
# 				for radiobtn in choices.find_elements_by_xpath(".//*"):
# 					if "":
# 						max_time = times
# 						break
# 				max_time = max_time.get_attribute("innerHTML")
# 				print max_time
# 				max_time = max_time.split("/")[1].strip().split(":")
# 				max_time = int((int(max_time[0].encode())*60)+int(max_time[1].encode()))
# 				print max_time
# 				time.sleep(max_time)
# 				v_times = v_times-1
# 				nextVid = driver.find_element_by_id("bRightNav.Image")
# 				nextVid.click()
# 			else:
# 				nextVid = driver.find_element_by_id("bRightNav.Image")
# 				nextVid.click()

logIn()
driver.quit()
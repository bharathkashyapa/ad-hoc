import subprocess,os,sys,re
import datetime,time
from random import randint

def create_network(interface_name,ssid,key,ip): # Call all commands
	print"Creating Network... please wait"
	com="sudo service network-manager stop"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	time.sleep(5)
	com="sudo ip link set "+interface_name+" down"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" mode ad-hoc"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	channel_no=str(randint(1,12))
	com="sudo iwconfig "+interface_name+" channel "+channel_no#"5" raw_input("Enter a channel no")
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" essid "+ssid
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" key "+key#"1234567890"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo ip link set "+interface_name+" up"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo ip addr add "+ip+"/8 dev "+interface_name
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	#com="ifconfig "+interface_name+" netmask 255.255.255.0"
	#subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	print "Created network with :",ssid,key,interface_name,ip,channel_no
def connect_network(interface_name,ip):       #CAll all commands
        #ip="169.254.34.2/16"
	com1=" sudo iwlist "+interface_name+" scan | grep ESSID > .wifinames.txt" # . is hidden file in Unix
	subprocess.call(com1, stdin=None, stdout=None, stderr=None, shell=True)
	f=open('.wifinames.txt','r')
	f=f.readlines()
	names=[]
	for i in range(0,len(f)):
		string=f[i]
		names.append(re.findall(r'"([^"]*)"', string)[0])
	flag=True
	while flag is True:
	        nw_name=raw_input("Enter the name of network you want to connect\n")
	        if nw_name  in names:
	                flag=False
                else :
                        print  "No network with this name is present , try again , press ^C to exit\n"        
        print "Connecting to "+nw_name+"\nPlease Wait............................................................"
        time.sleep(2)
        com="sudo service network-manager stop"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo ip link set "+interface_name+" down"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" mode ad-hoc"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" channel "+(raw_input("Enter a channel no\n"))
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" essid "+nw_name
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo iwconfig "+interface_name+" key "+raw_input("Enter network key\n")
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo ip link set "+interface_name+" up"
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	com="sudo ip addr add "+ip+"/8 dev "+interface_name
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
        print("connected successfully")
	        
def display_nw(iname):
	com="sudo iw dev "+iname+" scan "
	print("-----Networks Available-----")
	print subprocess.check_output(com,shell=True)
def assign_ip(interface_name):  #assign ip 10.last 3 octets
	com="ifconfig "+interface_name+" | grep HWaddr |cut -dH -f2|cut -d\  -f2"
	mac_address=subprocess.check_output(com,shell=True).strip('\n')
	sp=mac_address.split(":")
	x1=int(sp[3],16)
	x2=int(sp[4],16)
	x3=int(sp[5],16)
	ip="10."+str(x1)+"."+str(x2)+"."+str(x3)
	return ip
#print assign_ip("wlan0")
def ispresent(a,ll):
        for i in ll:
                if a in i:
                        return True
        return False
        
def get_interface_name(): #get name of wireless card
	com="ls /sys/class/net|grep wl*"									#worst hack , search for a better one
	interface_name=subprocess.check_output(com,shell=True).strip('\n')
	return interface_name
#interface_name=get_interface_name()
#ip=assign_ip(interface_name)

def name_network(interface_name):
	name=raw_input("Enter a name you want to give the network \n")
	if len(name)>31 or name=='':
		print("You have disobeyed rules, take the name we give you")
		return "nsociety"+str(time.time()).split(".")[0]
	ret_name=name
	com1=" sudo iwlist "+interface_name+" scan | grep ESSID > .wifinames.txt" # . is hidden file in Unix
	subprocess.call(com1, stdin=None, stdout=None, stderr=None, shell=True)
	f=open('.wifinames.txt','r')
	f=f.readlines()
	names=[]
	for i in range(0,len(f)):
		string=f[i]
		names.append(re.findall(r'"([^"]*)"', string)[0])
		#names.append(string)
	#print names
	if name in names:
		print("Duplicate Name found , a slight modification is being offered \n")
		ll=31-len(name)
		name=name+str(time.time()).split(".")[0][0:ll]
		return name
	else:
		return name
def give_key():         #There is a problem with this works only length 10 keys
	key=raw_input("Enter a key only containing only 0-9 whose length is greater than 9\n")
	if (len(key)<=9 or len(key)>62) and (re.search('\D',key)==None):
		print("You have disobeyed rules , your key is : 1234567890")
		return "1234567890"
	else:
		return key 
def give_key2():         #There is a problem with this works only length 10 keys
	key=raw_input("Enter a key only containing only 0-9 whose length is 10\n")
	if (len(key) is not 10) and (re.search('\D',key)==None):
		print("You have disobeyed rules , your key is : 1234567890")
		return "1234567890"
	else:
		return key 
interface_name=get_interface_name()
ip=assign_ip(interface_name)
com="sudo ip addr flush dev "+interface_name
subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
com="sudo service network-manager start"
time.sleep(2)
subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
time.sleep(2)
display_nw(interface_name)
print("-------------Run in root mode--------------------------------------------------")
print "Choose action"
print "1.Create an ad-hoc Network"
print "2.Connect to an ad-hoc network"
action=raw_input("Enter\n")
if action=='1':
        print "Setting up an ad-hoc Network.."
	ssid=name_network(interface_name)
	key=give_key2()
        create_network(interface_name,ssid,key,ip)
elif action=='2':
	connect_network(interface_name,ip)
else:
	print("invalid input,run this program again")
	exit(0)
what=raw_input( "Do you want to transfer a file? (y for yes)")
if what=="y":
        pass
else:
        exit(0)
'''ssid= name_network()
key=give_key()
interface_name=get_interface_name()
ip=assign_ip(interface_name)
print ssid,key,interface_name,ip'''

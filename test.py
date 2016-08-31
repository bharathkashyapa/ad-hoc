import subprocess,os,sys,re
import datetime,time
def create_network(interfaceNname,ssid,key,ip): # Call all commands
	pass
def connect_network(interfaceNname,ssid,key,ip):       #CAll all commands
	pass

def assign_ip(interfaceNname):  #assign ip 10.last 3 octets
	com="ifconfig "+interface_name+" | grep HWaddr |cut -dH -f2|cut -d\  -f2"
	mac_address=subprocess.check_output(com,shell=True).strip('\n')
	sp=mac_address.split(":")
	x1=int(sp[3],16)
	x2=int(sp[4],16)
	x3=int(sp[5],16)
	ip="10."+str(x1)+"."+str(x2)+"."+str(x3)
	return ip
#print assign_ip("wlan0")

def get_interface_name(): #get name of wireless card
	com="ls /sys/class/net|grep wl*"									#worst hack , search for a better one
	interface_name=subprocess.check_output(com,shell=True).strip('\n')
	return interface_name
#interface_name=get_interface_name()
#ip=assign_ip(interface_name)

def name_network():
	name=raw_input("Enter a name you want to give the network \n")
	if len(name)>31 or name=='':
		print("You have disobeyed rules, take the name we give you")
		return "nsociety"+str(time.time()).split(".")[0]
	ret_name=name
	com="nmcli d wifi list > .wifinames.txt" #hidden file in Unix
	subprocess.call(com, stdin=None, stdout=None, stderr=None, shell=True)
	f=open('.wifinames.txt','r')
	f=f.readlines()
	names=[]
	for i in range(1,len(f)):
		string=f[i]
		names.append(re.findall(r"'(.*?)'", string)[0].strip("'"))
	if name in names:
		print("Duplicate Name found , a slight modification is being offered \n")
		ll=31-len(name)
		name=name+str(time.time()).split(".")[0][0:ll]
		return name
	else:
		return name
def give_key():
	key=raw_input("Enter a key whose length is greater than 9\n")
	if len(key)<9 or len(key)>62:
		print("You have disobeyed rules , your key is : 'weakestpassword'")
		return 'weakestpassword'
	else:
		return key 

ssid= name_network()
key=give_key()
interface_name=get_interface_name()
ip=assign_ip(interface_name)

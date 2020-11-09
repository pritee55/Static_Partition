import os
import getpass


print("\n\t\t**....................##.........................**")
os.system("tput setaf 3")
print("\n\t*****************WELCOME In MY AUTOMATION TOOL*****************")
os.system("tput setaf 7")
print("\n\t\t**....................##.........................**")


passwd = getpass.getpass("\nEnter your password: ")

if passwd != "root":
    print("\n password is incorrect.Please enter right password. ")
    exit()
os.system("tput setaf 3")
print("\n\tThank You...")
print("\n\t############ You locally logged in successfully  ###########")
os.system("tput setaf 7")

def option():
      op = int(input('''
      \n
      ..............#WELCOME IN MAIN MENU#................

      \n
      Press 1 : To Create a Static Partition..
      press 2 : Format and mount partition..
      Press 3 : To increase size of Partition..
      Press 4 : To decrease size of partition..
      Press 5 : To delete the static partiton..
      press 6 : exit..
      \n
      what can I help you..: '''))
             
      if op == 1:
          os.system("\n yum install parted")
          name1= input("\n\tEnter your harddisk that you want..>> ")
          part1= input("\n\tEnter start point of partition..>> ")
          part2= input("\n\tEnter end point of partition..>> ")
          os.system("parted {} mkpart primary ext4 {}G {}G;".format(name1,part1,part2))
          os.system("lsblk")
          option()
      elif op == 2:
          name3= input("\n\t Enter the name of partition..>> ")
          os.system("mkfs.ext4 {}".format(name3))
          name4= input("\n\t Enter the folder name that you want..>>" )
          os.system("mkdir \{}".format(name4))
          os.system("mount {} {}".format(name3name4))
          os.system("lsblk")
      elif op == 3:
          name1= input("\n\t Enter the name of harddisk..>> ")
          num1= input("\n\t Enter the number of partition..>> ")
          size1= input("\n\t Enter the incresing end point size..>> ")
          os.system("parted {} resizepart {} {}G".format(name1,num1,size1))
          os.system("lsblk")
          option()
      elif op == 4:
          name1= input("\n\t Enter the name of harddisk..>> ")
          num1= input("\n\t Enter the number of partition..>> ")
          size2= input("\n\t Enter the decreasing end point size..>> ")
          os.system("parted {} resizepart {} {}G".format(name1,num1,size2))
          os.system("lsblk")
          option()
      elif op == 5:
          name1= input("\n\t Enter the name of harddisk..>> ")
          num1= input("\n\t Enter the number of partition..>> ")
          os.system("parted {} rm {}".format(name1,num1))
          os.system("lsblk")
          option()
      elif op == 6:
          os.system("exit")
          os.system("tput setaf 3")
          print("\n\n\t#########..THANK YOU..See you soon..#########")
          os.system("tput setaf 7")
          print("\n")

      else:
          print("Incorrect Choice,select correct option..")
          anykey =input("\n\t Press Enter to go main menu")
          option()


option()


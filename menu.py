import csv
import sys
import os

def main():
   menu()


def menu():
    print("\n\n************ ---------Welcome to Python Automation Menu---------- **************")
    print()

    choice = input("""
                      1: Basic linux commands
                      2: Hadoop setup
                      3: AWS Setup
                      4: HDD config
                      5: Exit menu

                      Please enter your choice: """)

    if(choice == 1):
        Basiccommands()
    elif (choice ==2):
        Hadoopsetup()
    elif(choice == 3):
        AWSsetup()
    elif(choice==4):
        HDD()
    elif(choice ==5):
        sys.exit
    else:
        print("Selected option is not vailid")
        print("Please try again")
        menu()

def Basiccommands():
    
    print ("""
    ----------------------------------------------------------------------------------------------
    1.for checking todays date
    2.for checking todays panchang
    3.for configuring your ip
    4.for checking your pwd
    5.to login as a root user
    6.to add user
    7.to configure your yum 
    8.to check your yum repolist
    9.to install any package through yum 
    10.to check your ram memory
    11.to check your harddisk/ssd memory
    12.to ping any website
    13.to check items in present directory
    14.to delete any directory
    15.to open file in vim editor
    16.to create a python program
    17.to rum python program
    18.press 0-(zero) to go to main menu
    ----------------------------------------------------------------------------------------------
     """)
    bc=int(input("enter your chocie for running basic linux commands : "))
    if(bc==1):
        os.system("date")
        Basiccommands()
    elif(bc==2):
        os.system("cal")
        Basiccommands()
    elif(bc==3):
        os.system("ifconfig")
        Basiccommands()
    elif(bc==4):
        os.system("pwd")
        Basiccommands()
    elif(bc==5):
        os.system("sudo su - root")
        Basiccommands()
    elif(bc==6):
        addeduser=input("Enter The username you want to add : ")
        os.system("useradd {}".format(addeduser))
        os.system("passwd addeduser")
        Basiccommands()
    elif(bc==7):
        os.system("sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        Basiccommands()
    elif(bc==8):
        os.system("yum repolist")
        Basiccommands()
    elif(bc==9):
        pkg=input("Enter the software you want to install : ")
        os.system("yum install {}".format(pkg))    
        Basiccommands()
    elif(bc==10):
        os.system("free -m")
        Basiccommands()
    elif(bc==11):
        os.system("fdisk -l")
        Basiccommands()
    elif(bc==12):
        pi=input("Enter your website or ip to check connection : ")
        os.system("ping {}".format(pi))
        Basiccommands()
    elif(bc==13):
        os.system("ls")
        Basiccommands()
    elif(bc==14):
        nm=input("Enter your filename to delete : ")
        os.system("rm {}".format(nm))
        Basiccommands()
    elif(bc==15):
        nm=input("Enter your filename to create in vim editor: ")
        os.system("vi {}".format(nm))
        Basiccommands()
    elif(bc==16):
       nm=input("Enter your filename to create python file : ")
       os.system("{}.py".format(nm))
       Basiccommands()
    elif(bc==17):
        pg=input("Enter filename with py extension to run the python program  : ")
        os.system("{}".format(pg))
        Basiccommands()
    else:
        main()
        


def AWSsetup():
    
    print("""
    ----------------------------------------------------------------------------------------------
    1.for installing python on your device(if alredy installed no need to select this option )
    !!!! python is mandatory to install 
    2.for install aws on cli
    3.for checking version of your installed aws 
    4.To start your aws cli (This step is mandatory for launching instance)
    5.To launch your free t2.micro instance in south-ap-1 region
    6.To launch your customised instance
    ----------------------------------------------------------------------------------------------  
    """)
    awsoption=int(input("enter your chocie for running AWS commands : "))
    if(awsoption==1):
        os.system("dnf install python3-pip")
    if(awsoption==2):
        os.system("pip3 install awscli --upgrade --user")
    if(awsoption==3):
        os.system("aws --version")
    if(awsoption==4):
        os.system("aws configure")
    if(awsoption==5):
        os.system("aws ec2 run-instances --image-id  ami-0a9d27a9f4f5c0efc --instance-type  t2.micro --count 1 --subnet-id subnet-2edccd46 --security-group-ids sg-02fb764381c3dd016 --key-name ec2user ")
    if(awsoption==6):
        iid=input("Enter your image id : ")
        iid.isalnum()
        itype=input("Enter your instance type  : ")
        subid=input("Enter your subnet id : ")
        sgid=input("Enter your security group id : ")
        kn=input("enter your keyname : ")
        os.system(" aws ec2 run-instances --image-id  iid --instance-type  itype --count 1 --subnet-id subid --security-group-ids sgid --key-name kn  ")

def HDD():
    print("""
      ----------------------------------------------------------------------------------------------  
      1.To check your disks connected
      2.To partition your drive
      3.To format your drive
      4.To mount your drive
      ----------------------------------------------------------------------------------------------  
        """)
    
    hddoption=int(input("Enter your choice : "))
    if(hddoption==1):
        os.system("fdisk-l")
    if(hddoption==2):
        dname=input("enter your disk name")
        os.system("fdisk {}".format(dname))
    if(hddoption==3):
        dname=input("enter your disk name")
        os.system("mkfs.ext4 {}".format(dname))
    if(hddoption==4):
        fname=input("enter your folder name to mount : ")
        dname=input("enter your disk name to mount : ")
        os.system("mkdir /{}".format(fname))
        os.system("mount {} /fname".format(dname))

    
def Hadoopsetup():
   pass

main()






#if(awsoption==1):
 #       os.system("")

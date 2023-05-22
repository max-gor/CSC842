#CSC-842 Cycle 1 Tool by Max Gorbachevsky
# This program scans local network, creates a list of connected devices and conducts vulnerability scan of all the connected devices.

import os
import sys
import nmap                         
import time
import subprocess


try:
    nm = nmap.PortScanner()         # Starting nMap
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

hostList = []

#*graceperiod = 7


def seek():                         # Scanning Network
    curHosts = []

    network = input('Please enter the Network you would like to scan (i.e 192.168.1.1/24): ')
    nm.scan(hosts = network, arguments = '-n -sP -PE -T5') # Ping Scan

    localtime = time.asctime(time.localtime(time.time()))
    print('============ {0} ============'.format(localtime)) # System Time
    
    for host in nm.all_hosts():
        try:
            mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'][mac]
            
        except:
            vendor = 'unknown'

        curHosts.append((host,mac,vendor)) #*,gracePeriod))
        
    updateHostList(curHosts)

    for host in hostList:
        print('Scan report for %s\nMAC Address: %s (%s)' % (host[0], host[1], host[2]))

    print('Number of connected devices: ' + str(len(hostList)))

    #Create a file with a list of IPs
    file = open('IPlist.txt','w')
    for host in hostList:
        file.write(host[0]+"\n")
    file.close()

    #Scan the list of IPs for vulnerabilities
    vuln = subprocess.Popen(["nmap","-sV","--script","vulners", "-iL", "IPlist.txt", "-oN", "Vulnerabilities.txt"], stdout=subprocess.PIPE)
    output = vuln.communicate()[0]
    print('Please check IPlist.txt for the list of connected devices IP addresses and Vulnerabilities.txt for the results of vulnerability scan of the connected devices')


    #*return len(hostList)                # returns count

def updateHostList(curHosts):
    global hostList
    
    if hostList == []:
        hostList = curHosts
    
    else:
        hostList = [(x[0],x[1],x[2],x[3]-1) for x in hostList]
    
        
   #* New Hosts
        
#*        newList = [(x[0],x[1],x[2],x[3]) for x in curHosts if not (any(x[0]==y[0] for y in hostList))]   

#*        for host in newList:
            
#*            hostList.append(host)
       
        
#*        for host in hostList:
            
#*            if any(host[0] == y[0] for y in curHosts):
                
#*                hostList[hostList.index(host)] = (host[0],host[1],host[2],gracePeriod)           
        
#*        for host in hostList:            
#*            if host[3] <= 0:
                
#*                hostList.remove(host)
#*                
#*            
#*            return newList, curHosts
#*def newHost():
#*    curHosts = []
#*    newList = []
#*    newList, curHosts = updateHostList(curHosts)
#*    new_host = (list(set(newList) - set(curHost)))
    
#*    return new_host#return new_host
#*    if len([new_host]) >=1:

#*        print('New connection detected:')       

if __name__ == '__main__':
    seek() #single run (comment out if using ongoing scanning)

    #*old_count = new_count = seek()

    #*startCounter = gracePeriod
    
    #* Looking for new hosts
    #*while (new_count <= old_count) or startCounter >= 0:
    #*    startCounter -= 1
            
    #*    time.sleep(1)
    #*    old_count = new_count          
    #*    new_count = seek()


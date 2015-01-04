#!/usr/bin/env python
import os

log=file('RSA_check.log','a')

def check_rsa_result(rsa_server):
    ''' use os.putenv to set shell env is very important used in cron'''
    os.putenv('HOME','/root/')
    os.putenv('USER','root')
    os.putenv('USERNAME','root')
    tocken_f=os.popen('/usr/local/stocken/bin/stoken')
    tocken=tocken_f.readlines()
    tocken_f.close()
    log.write("\n\ntocken"+tocken[0])

    radtest_command='/usr/bin/radtest username <pin>'+tocken[0].strip()+' '+rsa_server+' 0 <radius_pwd> <group> <source_ip>'
    log.write(radtest_command+"\n")
    radtest_f=os.popen(radtest_command)
    radtest=radtest_f.readlines()
    result1=''.join(radtest)
    radtest_f.close()
    return result1



if __name__ == "__main__":
    result=check_rsa_result('192.168.1.1')
    log.write(result)
    if result.find('Access-Accept packet') == -1:
        print "check 192.168.1.1 failed"
        log.write("check 192.168.1.1 failed")
        send_SMS.send_SMS(mobile_list, "RSA-master 192.168.1.1 failed")
    else:
        log.write("check 192.168.1.1 seccussful")
        print "check 192.168.1.1 seccussful"

log.close()

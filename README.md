RSA_status_check
================

scripts to check RSA server status;

1.Install the stoken
  https://github.com/cernekee/stoken

2.Config stoken with valid RSA token seed
  I use the stdid file RSA server generated for ios version.
  stoken import --file mytoken.sdtid

3.initiate the RSA tocken pin password
  I initiate the pin manually

4.test it use radtest

  ‘/usr/bin/radtest <username> <pin>`/usr/local/stocken/bin/stoken`<rsa_server_ip> 0 <radius_password> <group> <source_ip>‘

5.use the python script to check RSA status 
  /usr/bin/python rsa_monitor.py 

"""
This script does the following:
 1. Stops a tomcat webapp
 2. Creates a data file with the current date and time
 3. Saves it into a jar file
 4. Copies the jar file into the lib folder of the stopped tomcat app
 5. For random times (1-5):p
    1. Starts the tomcat webapp
    2. Runs a jmeter scenario
    3. Stops the tomcat webapp
 6. Starts the tomcat webapp again

 Before running this script - make sure that the provided tomcat user has "manager-script" permission (configurable
 at "tomcat-users.xml").
 Python >=3.6 is required.
"""

import os
import random
import shutil
import subprocess
import sys
import time
import zipfile

import pip

try:
    import tomcatmanager
except ImportError:
    if int(pip.__version__.split('.')[0]) > 9:
        from pip._internal import main
    else:
        from pip import main
    main(['install', 'tomcatmanager'])
    import tomcatmanager

working_dir = 'C:/Users/Administrator/Desktop/apache-jmeter-5.1.1/bin'
webgoat_dir = 'C:/Program Files/CxIAST/Demo/webapps/WebGoat-6.0.1/WEB-INF/lib'
data_file = 'data.html'
jar_file = 'newCheckSum.jar'
tomcat_app = '/WebGoat-6.0.1'
jmeter_command = 'jmeter -n -t WebGoat-6.0.1.jmx'

os.chdir(working_dir)

tomcat = tomcatmanager.TomcatManager()
tomcat.connect(url='http://localhost:8360/manager', user='tomcat', password='tomcat')
tomcat.stop(tomcat_app)
time.sleep(5)

with open(data_file, 'w') as f:
    f.write(time.strftime("%Y%m%d-%H%M%S"))
    f.close()
    with zipfile.ZipFile(jar_file, 'a') as z:
        z.write(data_file)
shutil.move(os.path.join(working_dir, jar_file), os.path.join(webgoat_dir, jar_file))

for i in range(random.randint(1, 6)):
    tomcat.start(tomcat_app)
    time.sleep(10)
    process = subprocess.Popen(jmeter_command, shell=True, cwd=working_dir, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    time.sleep(45)
    tomcat.stop(tomcat_app)
    time.sleep(5)

tomcat.start(tomcat_app)
time.sleep(5)
sys.exit()

Checkmarx Jmeter Runner
#######################

This script does the following:

1. Stops a tomcat webapp
2. Creates a data file with the current date and time
3. Saves it into a jar file
4. Copies the jar file into the lib folder of the stopped tomcat app
5. For random times (1-5):
      a. Starts the tomcat webapp
      b. Runs a jmeter scenario
      c. Stops the tomcat webapp
6. Starts the tomcat webapp again

-----


.. contents::

.. section-numbering::

Usage
=====
This project requires:

* Python 3.6

Clone the source code
---------------------
In your working folder (your home folder, for example)

.. code-block:: bash

    git clone https://github.com/yevgenykuz/checkmarx-jmeter-runner.git

Configure and run
-----------------
- Before running this script - make sure that the provided tomcat user has "manager-script" permission (configurable at "tomcat-users.xml").

Meta
====
Authors
-------
`yevgenykuz <https://github.com/yevgenykuz>`_

License
-------
`MIT License <https://github.com/yevgenykuz/checkmarx-jmeter-runner/blob/master/LICENSE>`_

-----

# Process_Monitoring_WMI
Creating a process monitor in python with Windows Management Instrumentation.
<h1>Process Monitoring with WMI</h1>

<h2>Description</h2>
The Windows Management Instrumentation (WMI) API gives programmers the ability to monitor a system for certain events and then receive callbacks when those events occur. We’ll leverage this interface to receive a callback every time a process is created and then log some valuable information: the time the process was created, the user who spawned the process, the executable that was launched and its command line arguments, the process ID, and the parent process ID. This will show us any processes created by higher-privilege accounts, and in particular, any processes that call external files, such as VBScript or batch scripts. When we have all of this information, we’ll also determine the privileges enabled on the process tokens. In certain rare cases, you’ll find processes that were created as a regular user but have been granted additional Windows privileges that you can leverage.

<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>WQLt</b>
- <b>WingPro/b>

<h2>Environments Used </h2>

- <b>Windows 11</b> (22H2)

<h2>Program walk-through:</h2>
Let’s begin by writing a very simple monitoring script that provides the basic process information and then build on that to determine the enabled privileges. This code was adapted from the Python WMI page (http://timgolden.me.uk/python/wmi/tutorial.html). Note that in order to capture information about high-privilege processes created by SYSTEM, for example, you’ll need to run your monitoring script as Administrator.

<h2>Usage Example:</h2>

  C:\Users\tim\work> python WMI.py
    "Calculator.exe",
     20200624083538.964492-240 ,

C:\Program Files\WindowsApps\Microsoft.WindowsCalculator\Calculator.exe,
1204 ,
10312 ,
('DESKTOP-CC91N7I', 0, 'tim') ,
N/A

notepad ,
20200624083340.325593-240 ,
C:\Windows\system32\notepad.exe,
13184 ,
12788 ,
('DESKTOP-CC91N7I', 0, 'tim') ,
N/A

<p align="center">
TODO: <br/>
Windows Token Privileges
<br />

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

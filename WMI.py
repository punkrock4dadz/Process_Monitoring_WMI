import os 
import sys
import win32api
import win32con
import win32security
import wmi

def get_process_privileges(pid):
    try:
      hproc = win32api.OpenProcess( 
                      win32con.PROCESS_QUERY_INFORMATION, False, pid
                      ) # We use the process ID to obtain a handle to the target process
                htok = win32security.OpenProcessToken(hproc, win32con.TOKEN_QUERY) # Request the token information for that process
                privs = win32security.GetTokenInformation( # By sending the win32security.TokenPrivileges structure.
                    htok,win32security.TokenPrivileges
                    ) # The function call returns a list of tuples, where the first member of the tuple is the privilege and the second member describes whether the privilege is enabled or not
                privileges = ''
                for priv_id, flags in privs:
                    if flags == (win32security.SE_PRIVILEGE_ENABLED | # Because we're concerned only with the enabled ones, we first check for the enabled bits.
                            win32security.SE_PRIVILEGE_ENABLED_BY_DEFAULT):
                        privileges += f'{win32security.LookupPrivilegeName(None, priv_id)}|' # And then lookup the human readable name for that priv.
            except Exception:
                privileges = get_process_privileges(pid)
        
            return privileges
               
def log_to_file(message):
    with open('process_monitor_log.csv', 'a') as fd:
        fd.write(f'{message}\r\n')

def monitor():
    head = 'CommandLine, Time, Executable, Parent PID, PID, User, Privileges'
    log_to_file(head)
    c = wmi.WMI() # We start by instantiating the WMI class
    process_watcher = c.Win32_Process.watch_for('creation') # tell it to watch for the process creation event
    while True:
        try:
            new_process = process_watcher() #2. We then enter a loop, which blocks until process_watcher returns a new process event

            cmdline = new_process.CommandLine
            create_date = new_process.CreationDate
            executable = new_process.ExecutablePath
            parent_pid = new_process.ParentProcessId
            pid = new_process.ProcessId
            proc_owner = new_process.GetOwner() # One of the class functions is GetOwner, which we call 4 to determine who spawned the process.
           
            privileges = get_process_privileges(pid)
            process_log_message = (
                f'{cmdline} , {create_date} , {executable},'
                f'{parent_pid} , {pid} , {proc_owner} , {privileges}'
                )
            print(process_log_message)
            print()
            log_to_file(process_log_message)
        except Exception:
            pass

if __name__ == '__main__':
    monitor()

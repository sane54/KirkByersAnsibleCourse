from snmp_helper import snmp_get_oid_v3
import pickle


def detect_config_change(ipaddr, port):

#Get HistoryRunningLastChanged
#In the lab environment, I am using the following credentials:

    user_name = 'pysnmp'
    auth_key = 'galileo1'         
    encrypt_key = 'galileo1'

    snmp_user = (user_name, auth_key, encrypt_key)
    snmp_device = (ipaddr, port)
    
    
    history_running_last_changed_set = snmp_get_oid_v3(snmp_device, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.1.0', auth_proto='sha',
                    encrypt_proto='aes128', display_errors=True)

    history_running_last_changed = str(history_running_last_changed_set[0])
    history_running_last_changed = history_running_last_changed.split('=', 1)[1]
    history_running_last_changed = int(history_running_last_changed.strip())
    print history_running_last_changed
    router_name = snmp_device[0]
                    
    #check the stored file
    while True:
        try:
            f = open("router_config_changes.pkl", "rb")
            router_changetime = pickle.load(f)
            break
        except:
            print " read failed "
            f = open("router_config_changes.pkl", "wb")
            pickle.dump([router_name, 0], f)
            
    #If HistoryRunningLastChanged is greater then send email with router name plus HistoryRunningLastChanged
    time = router_changetime[1]
    if history_running_last_changed > time: 
        difference = history_running_last_changed - time
        my_message = "Network node " + router_changetime[0] + " configuration has changed"
        send_mail("sane54@gmail.com", "alert", my_message, "witzgall.munoz@gmail.com")      
    
    #Save HistoryRunningLastChanged to stored_time_of_last_change   
        router_changetime = [router_name, history_running_last_changed]
        f = open("router_config_changes.pkl", "wb")
        pickle.dump(router_changetime, f)
    
    #cleanup
    f.close()

def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection

    smtp_conn.quit()

    return True

def __main__():
    #pynet-rtr1  = "184.105.247.70"
    #pynet-rtr2  = "184.105.247.71"
    #port = 161
    #detect_config_change(pynet-rtr1, port)
    detect_config_change("184.105.247.70", 161)
    
if __name__ == "__main__":
    __main__()  


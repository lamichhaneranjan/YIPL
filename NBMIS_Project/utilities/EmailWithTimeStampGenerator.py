from datetime import  datetime

def get_new_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%H_%S")
    return "super" + time_stamp + "@admin.com"
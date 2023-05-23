log = """2023-05-04 10:30:12 INFO Starting application
2023-05-04 10:30:14 INFO Connected to database
2023-05-04 10:30:15 DEBUG Received request to process data for user_id=1234
2023-05-04 10:30:16 DEBUG Fetching data from database for user_id=1234
2023-05-04 10:30:17 DEBUG Processing data for user_id=1234
2023-05-04 10:30:19 INFO Completed processing data for user_id=1234
2023-05-04 10:30:21 DEBUG Received request to process data for user_id=5678
2023-05-04 10:30:22 DEBUG Fetching data from database for user_id=5678
2023-05-04 10:30:23 DEBUG Processing data for user_id=5678
2023-05-04 10:30:25 INFO Completed processing data for user_id=5678
2023-05-04 10:30:27 INFO Shutting down application"""

def value_in_dict(line):
    lvl_dict = dict()
    msg_dict = dict()
    userid_dict = dict()
    main_value = line[20:]

    splitted_value = main_value.find(" ")
    lvl_key = main_value[:splitted_value].strip()
    msg_key = main_value[splitted_value:].strip()
    userid_value = main_value[-4:]

    lvl_dict.update({"level": lvl_key})
    msg_dict.update({"message": msg_key})
    if("user_id") in msg_key:
        userid_dict.update({"user_id": userid_value})
        return lvl_dict, msg_dict, userid_dict
    else:
        return lvl_dict, msg_dict

    
def keys_values_in_dict(log):
    master_dict = dict()
    lines = log.split("\n")
    for line in lines:
        main_key = line[:19]
        master_dict.update({main_key: value_in_dict(line)})
    return master_dict

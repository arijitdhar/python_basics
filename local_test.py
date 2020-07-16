__author__ = '220152'

import datetime, json
has_any_error = False

def invoke_update_exporter_status(status):
    """
    Function to invoke update_exporter_status
    :return:
    """
    global has_any_error
    try:
        print(status)
        if status == 'failed':
            has_any_error = True
        return status
    except Exception as e:
        print(e)


method_invocation_status = invoke_update_exporter_status("failed")
print(method_invocation_status)
print(has_any_error)

ddl_str="abcd"
if ddl_str.find("1") != -1:
    print("Found")
else:
    print("Not found")



# date_time_formatter = "%Y-%m-%d %H:%M:%S"
# curr_time_stamp = datetime.datetime.now()
# curr_time_stamp_str = curr_time_stamp.strftime(date_time_formatter)
# print("curr_time_stamp_str: {}".format(curr_time_stamp_str))

"""
try:
    with open("files/conn_cfg.json",'r') as cfg:
        obj=json.load(cfg)
        database_name = obj["database"]["dbname"]
        hostname = obj["database"]["host"]
        port_number = obj["database"]["port"]
        username = obj["database"]["user"]
        password = obj["database"]["password"]
        exporter_log_table = obj["exporter_log_table"]

        print("schemas: ", str(obj["schemas"]))
        print("tables: ", str(obj["tables"]))
        print("views", str(obj["views"]))

        config_str = "schemas:"+str(obj["schemas"]).replace("'","\"")+","+"tables:"+str(obj["tables"]).replace("'","\"")+","+"views:"+str(obj["views"]).replace("'","\"")
        print("config_str: \n",config_str)
except Exception as e:
    print(e)
"""







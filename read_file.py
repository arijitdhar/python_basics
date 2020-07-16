__author__ = '220152'
import multiprocessing, os, time

def execute_unload_sql(item):
    thread_id = "Thread[{}:{}]".format(multiprocessing.current_process().pid, multiprocessing.current_process().name)
    print(thread_id)
    return {item[0]:"Success"}


if __name__ == "__main__":

    with open("files/unload.sql", "r") as unload_sqls:
        sql = unload_sqls.read()

    unload_sql_list = sql.split("\n--END--\n")

    print("Number of Unload sqls: {}".format(len(unload_sql_list)))
    unload_sql_aggr_list = []
    for unload_sql in unload_sql_list:
        table_schema = unload_sql[unload_sql.find('from "')+5:unload_sql.find('\') \n')]
        table_schema = table_schema.replace('"','')

        unload_sql_list = []
        unload_sql_list.append(table_schema)
        unload_sql_list.append(unload_sql)
        unload_sql_aggr_list.append(unload_sql_list)
        # print("{}:{}\n".format(table_schema, unload_sql))

    # print(len(unload_sql_dict))
    # for item in unload_sql_dict.items():
    #     print(item[0])
    #     print(item[1])

    print("Main pid: {}".format(os.getpid()))
    p = multiprocessing.Pool(processes=2, maxtasksperchild=2)

    results = p.map(execute_unload_sql, unload_sql_aggr_list)

    print("Results: ", results)

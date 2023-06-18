
db_names={
    "product":"product_info.db",
    "user":"user_info.db",
    "storage":"storage_info.db",
    "date":"date.db",
    "staff":"staff.db"
}




table_names={
    "table1":"products",
    "table2":"employers",
    "table3":"storage",
    "table5":"product_enter_date",
    "table6":"user_date",
    "table7":"product_exit_date",
    "table8":"salary"
    
}


def qustion_mark_generator(count):
  
    number_of_qustion_mark = ""

    for i in range(count):
        number_of_qustion_mark += "?,"

    return number_of_qustion_mark[:-1]
    



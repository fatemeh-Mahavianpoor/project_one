
db_names={
    "product":"product_info.db",
    "user":"user_info.db",
    "storage":"storage_info.db",
    "store":"storage.db"
}




table_names={
    "table1":"products",
    "table2":"employers",
    "table3":"storage",
    "table4":"test"
}


def qustion_mark_generator(count):
  
    number_of_qustion_mark = ""

    for i in range(count):
        number_of_qustion_mark += "?,"

    return number_of_qustion_mark[:-1]
    

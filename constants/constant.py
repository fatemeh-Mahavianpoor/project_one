
db_names={
    "product":"product_info.db",
    "user":"user_info.db",
    "storage":"storage_info.db",
    "date":"date.db",
    "staff":"staff.db"
}




table_names={
    "product_table":"products",
    "user_table":"employers",
    "storage_table":"storage",
    "product_enter_date_table":"product_enter_date",
    "user_date_table":"user_date",
    "product_exit_date":"product_exit_date",
    "salary_table":"salary"
    
}


def qustion_mark_generator(count):
  
    number_of_qustion_mark = ""

    for number in range(count):
        number_of_qustion_mark += "?,"

    return number_of_qustion_mark[:-1]
    



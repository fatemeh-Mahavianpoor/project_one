
db_names={
    "product":"product_info.db",
    "employer":"employer_info.db"
}



table_names={
    "table1":"products",
    "table2":"employers"
}

item_table={
    
    "item_one":"category",
    "item_two":"product_id",
    "item_three":"product_name"
}

def qustion_mark_generator(count):
  
    number_of_qustion_mark = ""

    for i in range(count):
        number_of_qustion_mark += "?,"

    return number_of_qustion_mark[:-1]
    
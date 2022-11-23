import cafe_app as a
import file_handlers as fh
import pyinputplus as ip

def print_whole_list(list_type):
    whole_list = ""
    for item in list_type:
        whole_list += f"{item}\n"
    return print(whole_list)

def print_orders_list():
    orders_list = ""
    for order in fh.sorted_orders_list:
        orders_list += f"{order}\n"
    return print(orders_list)

def view_list(list_type, menu_type):
    if len(list_type) == 0:
        print(f"{menu_type.title()} list is empty.\n")
        a.sub_menu(list_type, menu_type)
    elif menu_type == 'order':
        print_orders_list()
    else:
        print_whole_list(list_type)
        a.sub_menu(list_type, menu_type)
        
def id_generator_create(temp_dict):
    temp_dict["id"] = "".join(
                [
                    value[0]
                    for key, value in temp_dict.items()
                    if key == "name" 
                ]) + "".join(
                [
                    value[-1]
                    for key, value in temp_dict.items()
                    if key == "name"
                ])
    return temp_dict

def create_temp_dict(menu_type, temp_dict):
    if menu_type == "product":
        temp_dict = {"id": "", "name": "", "price": ""}
    elif menu_type == "courier":
        temp_dict = {"id": "", "name": "", "phone_number": ""}
    return temp_dict

def create_name(temp_dict, name_input):
    temp_dict["name"] = name_input
    return temp_dict

def create_price(temp_dict, name_input):
    temp_dict["price"] = name_input
    return temp_dict

def create_phone_num(temp_dict, input_info_int):
    temp_dict["phone_number"] = input_info_int
    return temp_dict

def append_to_dict_to_list(list_type, temp_dict):
    list_type.append(temp_dict)
    return list_type

def create(list_type, menu_type):
    temp_dict = {}
    create_temp_dict(menu_type, temp_dict)
    input_info_str = ""
    input_info_str = ip.inputStr("Input name\n")
    create_name(temp_dict, input_info_str)
    if menu_type == "product":
        input_info_float = ip.inputFloat("Input price\n")
        create_price(temp_dict, input_info_float)
    else:
        input_info_str = ip.inputStr("Input courier phone number\n")
        create_phone_num(temp_dict, input_info_str)
    id_generator_create(temp_dict)
    sorted_temp_dict = {key: value for key, value in sorted(temp_dict.items())}   
    append_to_dict_to_list(list_type, sorted_temp_dict)
    return view_list(list_type, menu_type)

def update_price(list_type, index, key, input_info):
    list_type[index][key] = input_info
    return list_type[index][key]

def update_record(list_type, index, key, input_info):
    list_type[index][key] = input_info
    return list_type[index][key]

def id_generator_update(list_type, index):
    print(index)
    list_type[index].update(
        {
            "id": "".join(
                [
                    value[0]
                    for key, value in list_type[index].items()
                    if key == "name" 
                ]
            )
            + "".join(
                [
                    value[-1]
                    for key, value in list_type[index].items()
                    if key == "name"
                ]
            )
        }
    )
    print(index)
    return list_type

def update(list_type, menu_type):
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    else:
        for item in list_type:
            print(item)
        info = ip.inputStr(f"Input id of {menu_type}\n", blank=True)
        if info in [value["id"] for value in list_type]:
            index = next(
                (index for (index, key) in enumerate(list_type) if key["id"] == info),
                None,
            )
            for key, _ in list_type[int(index)].items():
                if key == "price":
                    input_info_float = str(
                        ip.inputFloat(f"Input new {key.replace('_', ' ')}\n", blank=True)
                    )
                    if not input_info_float:
                        continue
                    else:
                        update_price(list_type, index, key, input_info_float)
                else:
                    if not key == "id":
                        input_info_str = ip.inputStr(f"Input new {key.replace('_', ' ')}\n")
                        if not input_info_str:
                            continue
                        else:
                            update_record(list_type, index, key, input_info_str)
                    else:
                        continue
            id_generator_update(list_type, index)
        else:
            a.incorrect_input()
    view_list(list_type, menu_type)
    
def delete_record(list_type, index):
    return list_type.remove(list_type[index])

def delete_order_record(order_number):
            return fh.orders_list.remove(fh.orders_list[order_number])
        
def delete(list_type, menu_type):
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    elif list_type == fh.orders_list:
        for index, order in enumerate(fh.orders_list):
            print(index, order)
        order_number = ip.inputInt("Input number of order you would like to delete\n")
        delete_order_record(order_number) 
        view_list(list_type, menu_type)
    else:
        for item in list_type:
            print(item)
        info = ip.inputStr(f"Input id of {menu_type} to delete\n")
        if [value["id"] for value in list_type if info in value["id"]]:
            index = next(
                (index for (index, key) in enumerate(list_type) if key["id"] == info),
                None,
            )
            delete_record(list_type, index)
            view_list(list_type, menu_type)
        else:
            a.incorrect_input()

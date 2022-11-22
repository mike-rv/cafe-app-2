# temp_dict = {"id": '1', "name": "coke", "phone_number": "2.0"}

# def id_generator(temp_dict):
#     temp_dict.update(
#         {
#             "id": "".join(
#                 [
#                     value[:2]
#                     for key, value in temp_dict.items()
#                     if key == "name" 
#                 ]
#             )
#             + "".join(
#                 [
#                     value
#                     for key, value in temp_dict.items()
#                     if key == "id"
#                 ]
#             )
#             + "".join(
#                 [
#                     value[-1]
#                     for key, value in temp_dict.items()
#                     if key == "name"
#                 ]
#             )
#         }
#     )
#     return temp_dict

# print(id_generator(temp_dict))

# def incorrect_input():
#     print("Incorrect input")


# list_type = [{"id": 1, "name": "", "price": ""}]
# menu_type = "product"

# if menu_type == "product":
#     temp_dict = {"id": (len(list_type)), "name": "", "price": ""}
# elif menu_type == "courier":
#     temp_dict = {"id": len(list_type), "name": "", "phone_number": ""}

# for key, _ in temp_dict.items():
#     if key == "id":
#         temp_dict[key] += 1
#         temp_dict[key] = str(temp_dict[key])
#     elif key == "price":
#         try:
#             input_info_int = float(input(f"Input {key.replace('_', ' ')}\n"))
#             temp_dict[key] = input_info_int
#             break
#         except ValueError:
#             incorrect_input()
#     else:
#         input_info_str = input(f"Input {key.replace('_', ' ')}\n")
#         if not input_info_str:
#             incorrect_input()
#         else:
#             temp_dict[key] = input_info_str

# print(temp_dict)

# import csv
# with open("products.csv") as csv_file:
#     print(csv.DictReader(csv_file))
#     products_list = [
#             {k: v for k, v in row.items()} for row in csv.DictReader(csv_file)]
            
# print(products_list)

# import csv

# # csv_file = 'products.csv'def is_csv_empty(csv_file):

# csv_file = open("products.csv")  

# print(csv_file)

# import pyinputplus as ip

# def user_choice():
# listing = [{'a': 'cat','b': 'dog', 'c': 'rabbit', 'd': 'fish', 'e': 'hamster'}, {'a': 'cow','b': 'dog', 'c': 'rabbit', 'd': 'fish', 'e': 'hamster'}]
# user_input = ip.inputChoice([''.join([(v) for k, v in record.items() if k == 'a']) for record in listing])
    # return user_input
# listing = ['a: 1','b', 'c', 'd', 'e']
# user_input = ip.inputMenu(listing, numbered=True)
# print(user_input)

# def test():
#     for i in range(4):
#         print(i)

list_type = [1,2,3,4,5,6,7,8,9,10]

def print_whole_list(list_type):
    whole_list = ""
    for item in list_type:
        whole_list += f"{item}\n"
    return whole_list

print(print_whole_list(list_type))

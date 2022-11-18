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

import csv

# csv_file = 'products.csv'def is_csv_empty(csv_file):

csv_file = open("products.csv")  

print(csv_file)

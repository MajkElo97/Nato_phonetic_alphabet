import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#Nato phonetic aplphabet:
def check_list():
    word = input("type a word: ").upper()
    try:
        new_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Please type only letters!")
        new_list = []
        check_list()
    else:
        print(new_list)


df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(new_dict)
check_list()

def my_code(a, b):
    calculate = a + b
    print(calculate)
my_code(20, 50)

def len_list():
    list1 = ["Muhaiminul", "islam", "Mahi", 1, 2, 3]
    result = len(list1)
    return result
    
result2 = len_list()
print(result2)


heros = ["Muhaiminul", "akib", "konok", "thor"]
def our_heros(our_heros):
    for heros2 in our_heros:
        print(heros2, end=" ")
    
our_heros(heros)
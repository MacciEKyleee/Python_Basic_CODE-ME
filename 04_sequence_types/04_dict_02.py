"""
2▹ Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe.
Przekształć ją w słownik dict_from_tuples.

"""
tuples_to_dict = [('wiosna','lato'),('jesień','zima')]
print(tuples_to_dict)

dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)
print(dict_from_tuples['wiosna'])
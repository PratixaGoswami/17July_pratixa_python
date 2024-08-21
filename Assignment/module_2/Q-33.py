"""Write a Python script to check if a given key already exists in a
dictionary"""

tops_student={'pratixa':'python','bansi':'android','pinal':'java'}
info = 'pinal'

if info  in tops_student:
    print(f"the key'{info}' exists in a dictionary")
else:
    print(f"the key'{info}' does not exists in a dictionary")    
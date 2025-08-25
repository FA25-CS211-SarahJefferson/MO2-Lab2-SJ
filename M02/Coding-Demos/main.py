# Imports array module
import array


#Array
def array_demo():
    print("Main Array")

    # Creates array on integers
    main_array = array.array('i', [10, 25, 30])
    # Prints array in order
    print("Initial array: ", main_array)

    main_array.append(35)
    print("Appended value 35: ", main_array)

    # Insert at the beginning (index 0)
    main_array.insert(0, 5)
    print("After inserting 5 at the beginning:", main_array)


    # Insert number in the middle of array
    main_array.insert(2, 20)
    print("Added 20 in middle of array: ", main_array)

    #Delete number from end of array
    main_array.pop()
    print("Popped from end of array: ", main_array)

    #Delete number from beginning of array
    main_array.pop(0)
    print("Popped integer from beginnig of array: ", main_array)

    # Deleted number from middle of array
    main_array.pop(1)
    print("Ppopped middle numer from array: ", main_array)

    #Find number in array
    search = 25
    if search in main_array:
        print(f"{search} found at index {main_array.index(search)}")
    else:
        print(f"{search} not found in array")

    #final array
    print("Final array: ", main_array)



# Dictionary
def dict():
    print("Dictionary: ")
    d = {}

     # Insert key-value pairs
    d["name"] = "Sarah"
    d["age"] = 20
    d["is_student"] = True
    print("Initial dictionary:", d)

    # Update the value for an existing key
    if "age" in d:
        d["age"] = 21
        print("After updating age:", d)
    else:
        print("Key not found.")

    # Delete key value pair
    if "age" in d:
        del d["age"]
        print("After deleting 'age':", d)
    else:
        print("Key not found")

    # Search for a value by key
    key = "age"
    if key in d:
        print(f"Value for '{key}':", d[key])
    else:
        print(f"Key '{key}' not found.")

    # Display the dictionary
    print("Final dictionary:", d)


# Main
if __name__ == "__main__":
    array_demo()
    dict()
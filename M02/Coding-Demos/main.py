# Imports array module
import array



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

    main_array.pop()
    print("Popped from end of array: ", main_array)

    main_array.pop(0)
    print("Popped integer from beginnig of array: ", main_array)

    main_array.pop(1)
    print("Ppopped middle numer from array: ", main_array)

    search = 25
    if search in main_array:
        print(f"{search} found at index {main_array.index(search)}")
    else:
        print(f"{search} not found in array")

    print("Final array: ", main_array)


if __name__ == "__main__":
    array_demo()
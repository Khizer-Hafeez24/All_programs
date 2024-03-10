class Pythonadvance:
    def __init__(self):
        pass
    # list method
    def my_list(self):
        my_list = [1, 2, 3, 4, 5]
        print("List:", my_list)
    # dictionary method
    def my_dictionary(self):
        my_dict = {"name": "John", "age": 30}
        print("Dictionary:", my_dict)
    # condition method
    def my_condition(self):
        x = 10
        if x > 15:
            print("x is greater than 5")
        else:
            print("x is smaller than 5")
    # loop method
    def my_loop(self):
        for i in range(5):
            print("Iteration:", i)
    # array method
    def my_array(self):
        import array
        my_array = array.array('i', [1, 2, 3, 4, 5])
        print("Array:", my_array)
    # inner method
    def inner_method(self):
        print("Inside inner method")
python_advance_obj = Pythonadvance()
# call each method
python_advance_obj.my_list()
python_advance_obj.my_dictionary()
python_advance_obj.my_condition()
python_advance_obj.my_loop()
python_advance_obj.my_array()
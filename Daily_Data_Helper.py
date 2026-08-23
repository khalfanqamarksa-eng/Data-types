class DailyDataHelper:

    def __init__(self, data_list=None):
        # Constructor setting default values
        if data_list is None:
            self.data = ["Read", "Workout", "Code", "Sleep"]
        else:
            self.data = data_list
        print("Daily Data Helper initialized.")

    def search_data(self, target):
        # Use enumerate to search index and value
        for index, value in enumerate(self.data):
            if value.lower() == target.lower():
                print(f"Found '{target}' at index {index}.")
                return index
        print(f"'{target}' not found.")
        return -1

    def __del__(self):
        # Destructor
        print("Daily Data Helper instance destroyed.")


# Test
helper = DailyDataHelper()
helper.search_data("Code")
del helper  # Triggers destructor
from utils import get_load, sort_state_data, sort_data, formatted_data

def main():
    data = get_load("operations.json")
    data_sort = sort_state_data(data)
    sort_data_ = sort_data(data_sort)
    form_date = formatted_data(sort_data_)
    print(*form_date)

if __name__ == "__main__":
    main()

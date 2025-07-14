types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(tickets):
    test = {}
    unique_tickets = []
    for key, values in tickets.items():
        unique_value = []
        for val in values:
            if val not in unique_tickets:
                unique_tickets.append(val)
                unique_value.append(val)
        test[key] = unique_value
    return test

def tickets_by_type(types, tickets):
    test = remove_duplicates(tickets)
    tickets_by_type = {}
    types_values = []
    test_values = []

    for key, values in test.items():
        test_values.append(values)
    for key, values in types.items():
        types_values.append(values)
    for i in range(len(test_values)):
        tickets_by_type[types_values[i]] = test_values[i]
    return tickets_by_type

unique_tickets = remove_duplicates(tickets)
print(unique_tickets)
tickets_type = tickets_by_type(types, tickets)
print(tickets_type)


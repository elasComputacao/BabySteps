def prepare_second_line(people_and_consume):
    second_line = ''
    for consume, people in people_and_consume:
        second_line += f'{people}-{consume} '
    second_line_without_last_space = second_line[:-1]
    return second_line_without_last_space


amount_of_properties = int(input())
amount_of_cities = 1

still_have_cities_to_count = amount_of_properties != 0

while still_have_cities_to_count:
    people_and_consume = []
    city_consume = 0
    city_people = 0

    for _ in range(amount_of_properties):
        property_people, property_consume = [
            int(x) for x in input().split(' ')]

        city_consume += property_consume
        city_people += property_people

        avg_property_consume = property_consume // property_people
        people_and_consume.append([avg_property_consume, property_people])

    people_and_consume.sort()

    second_line = prepare_second_line(people_and_consume)
    city_avg_consume = city_consume/city_people

    print(f'Cidade# {amount_of_cities}:')
    print(second_line)
    print('Consumo médio: {:.2f} m3.\n'.format(city_avg_consume))

    amount_of_cities += 1
    amount_of_properties = int(input())
    still_have_cities_to_count = amount_of_properties != 0

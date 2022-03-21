import shapes

def show_menu():
    print('Wybierz kształt pomieszczenia.')
    print('1 - kwadrat')
    print('2 - prostokąt')
    print('3 - trapez')

def square_room(flat_area):
    a = float(input('Podaj długość boku ->'))
    room_area = shapes.square(a)
    flat_area += room_area
    return flat_area

def rect_room(flat_area):
    a = float(input('Podaj długość krótszego boku ->'))
    b = float(input('Podaj długość dłuższego boku ->'))
    room_area = shapes.rectangle(a,b)
    flat_area += room_area
    return flat_area

def trapezoiz_room(flat_area):
    a = float(input('Podaj długość krótszego boku ->'))
    b = float(input('Podaj długość dłuższego boku ->'))
    h = float(input('Podaj wysokość trapezu ->'))
    room_area = shapes.trapezoid(a,b,h)
    flat_area += room_area
    return flat_area

def main():
    rooms_number = int(input('Podaj liczbę pokoi: \t'))
    flat_area = 0
    for r in range(rooms_number):
        show_menu()
        room_shape = input()

        if room_shape == '1':
            flat_area = square_room(flat_area)
            # a = float(input('Podaj długość boku -> \t'))
            # room_area = shapes.square(a)
            # #print(room_area)
            # flat_area = (room_area)

        elif room_shape == '2':
            flat_area = rect_room(flat_area)

            # a = float(input('Podaj długość boku krótszego-> \t'))
            # b = float(input('Podaj długość boku dłuższego-> \t'))
            # room_area = shapes.rectangle(a,b)
            # #print(room_area)
            # flat_area = (room_area)

        elif room_shape == '3':
            flat_area = trapezoiz_room(flat_area)

            # a = float(input('Podaj długość boku krótszego-> \t'))
            # b = float(input('Podaj długość boku dłuższego-> \t'))
            # h = float(input('Podaj szerokość pokoju pomiędzy bokami równoległymi -> \t'))
            # room_area = shapes.trapezoid(a,b,h)
            # #print(room_area)
            # flat_area = (room_area)

        else:
            print('Wybrałeś zły kształt pokoju')
    print(f'Powierzchnia całkowita mieszania wynosi {flat_area} m2.')
    
if __name__=='__main__':
    main()
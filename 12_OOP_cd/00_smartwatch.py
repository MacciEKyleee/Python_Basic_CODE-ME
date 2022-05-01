class ElectricThings():
    def get_electric(self):
        print('ElectricThings ----')

# class Electronics:
#     def __init__(self):
#         print('Electronics')
class Electronics:
    def get_electronic(self):
        print('Electronics ****')

class Watch(Electronics):
    def __init__(self):
        print('Watch function is presenting the time')

    def show_time(self):
        print('18:50')

class Phone(ElectricThings):
    def __init__(self):
        print('Phone is great invent')

    def make_call(self):
        print('Calling... best friend')


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('This smartwatch is great')


handband = SmartWatch()
handband.make_call()
handband.show_time()
handband.get_electronic()
handband.get_electric()
#
#
# class UsefulStuff:
#     def __init__(self, name):
#         print(name, 'is used to make life easier!')
#
#
# class Watch(UsefulStuff):
#     def __init__(self, watch_name):
#         print(watch_name, "is small and convenient")
#         super().__init__(watch_name)
#
#
# class Phone(UsefulStuff):
#     def __init__(self, phone_name):
#         print(phone_name, "can make a call")
#         super().__init__(phone_name)
#
#
# class SmartWatch(Watch, Phone):
#     def __init__(self):
#         print('Smartwatch is great!')
#         super().__init__('Smartwatch')
#
#
# sw = SmartWatch()
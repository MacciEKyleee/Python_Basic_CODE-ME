import datetime
from holidays import Poland

class Student:
  university = 'university'
  min_avg = 4.7

  def __init__(self, name, last,grades):
    self.name = name
    self.last = last
    self.grades = grades

  def __repr__(self):
    return self.name.capitalize() + " " + self.last.capitalize()

  def email(self):
    return f'{self.last}.{self.name}@{self.university}.com'

  @property
  def nickname(self):
    return self.name + '***'

  @property # getter
  def fullname(self):
    return f'{self.name.capitalize()}{self.last.capitalize()}'

  @fullname.setter
  def fullname(self,name_last):
    self.name, self.last = name_last.split() #['Anna','Snow']

  @fullname.deleter
  def fullname(self): #deleter
    self.name, self.last = None, None

  # def del_fullname(self);
    #self.name = None
    # self.last = None

  def grand_scholarship(self):
      if self.grades > self.min_avg:
        print('You get scholarship')
      else:
        print('Not this time')

 # def set_new_avg(self,new_value):
 #   self.min_avg = new_value

  @classmethod
  def set_new_avg(cls,new_value):
    cls.min_avg = new_value

  @classmethod
  def set_university_name(cls,new_name):
    cls.university = new_name

  @staticmethod
  def get_salary_net_under_26(salary_gross):
    """returns salary netto """
    if salary_gross < 85000: # pit 0%
      return salary_gross
    else: # wejście w próg podatkowy
      return 85000 + (salary_gross - 85000)*0,83

  @staticmethod
  def is_academic_day(day):
    is_weekend =  day.weekday() in [5,6]

    free_days_pl = Poland()
    is_free_day = day in free_days_pl

    return not is_weekend and not is_free_day

    # if day.weekday() == 5 or day.weekday() == 6:
    #   return False
    # else:
    #   return True

def main():
  obj_anna = Student('anna', 'kowalska', 4.72)
  obj_michal = Student('michal', 'nowak', 4.69)

  #today = datetime.date.today()
  #eg_date = datetime.datetime.strptime('2022-01-06','%Y-%m-%d')
  #print('Czy dzisiaj idziemy na uczelnię?', obj_michal.is_academic_day(today))

  obj_ann = Student('anna','smith',4.0)
  # obj_ann = Student('anna','smith',4.0)
  # print(obj_ann.nickname)
  obj_ann.name = 'ann'

  print('Zmiana stanu cywilnego')
  obj_ann.fullname = 'Anna Snow'
  print(obj_ann.name)
  print(obj_ann.last)

  print('USUWAM BO RODO!!!')
  # obj_ann.del_fullname()
  # print(obj_ann.name)
  # print(obj_ann.last)

  del obj_ann.fullname
  print(obj_ann.name)
  print(obj_ann.last)


if __name__ == "__main__":
  main()




# obj_michal.grand_scholarship()
#
# obj_michal.set_new_avg(4.5)
# obj_michal.grand_scholarship()
#
# print(obj_anna.min_avg)
# print(obj_michal.min_avg)
#
# print('******')
#
# Student.set_new_avg(4.1)
# print(obj_anna.min_avg)
# print(obj_michal.min_avg)

# print(obj_michal.email())
# Student.set_university_name('pg.edu')
# print(obj_anna.email())
# print(obj_michal.email())


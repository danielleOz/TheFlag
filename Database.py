import pandas
import MineField
import Soldier
from csv import writer


def create_csv():
    saved_data = {
        'mine_field': ["hi"],
        'solider': ["byse"],
    }
    df = pandas.DataFrame(saved_data)
    df.to_csv('data.csv')


def add_to_csv(index, mine_filed, solider):
    List = [mine_filed,solider]
    with open('data.csv', 'a', index = index) as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()


def read_cvs_index(index):
    df = pandas.read_csv('data.csv')
    print(df.loc[index])


create_csv()
add_to_csv(2, MineField.mine_field, Soldier.soldier_field)
read_cvs_index(1)
read_cvs_index(0)

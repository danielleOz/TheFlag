import pandas
import MineField
import Soldier
from csv import writer


def create_csv():
    saved_data = {'RRF': ['OOF']}
    df = pandas.DataFrame(saved_data)
    df.to_csv('data.csv')


create_csv()


def add_to_csv(index, mine_filed, solider):
    added_data = {'BGFX': ['HU']}
    df = pandas.DataFrame(added_data)
    df.to_csv('data.csv', mode='a', index=index, header=False)


def read_cvs_index(index):
    df = pandas.read_csv('data.csv')
    print(df.loc[index])


# create_csv()
add_to_csv(1, MineField.mine_field, Soldier.soldier_field)
read_cvs_index(1)
read_cvs_index(0)

import pandas
import MineField
import Soldier
from csv import writer


def create_csv():
    saved_data = {'mine': ["","","","","","","","",""],
                  'solider': ["","","","","","","","",""]}
    df = pandas.DataFrame(saved_data)
    df.to_csv('data.csv')


def add_to_csv(index, mine_filed, solider):
    # added_data = {'BGFX': ["89"]}
    # df = pandas.DataFrame(added_data)
    # df.to_csv('data.csv', mode='a',index=index)
    df = pandas.read_csv('data.csv')
    df.loc[index,'mine'] = mine_filed
    df.loc[index, 'solider'] = mine_filed
    df.to_csv('data.csv')


def read_cvs_index(index):
    df = pandas.read_csv('data.csv')
    print(df.loc[index])


create_csv()
add_to_csv(0, MineField.mine_field, Soldier.soldier_field)
print()

import pandas
import MineField
import Soldier
from csv import writer
import ast
import Consts

mine = [[Consts.EMPTY for i in range(Consts.FIELD_COLS)] for j in
                  range(Consts.FIELD_ROWS)]
soldier = [[Consts.EMPTY for i in range(Consts.FIELD_COLS)] for j in
                  range(Consts.FIELD_ROWS)]
def create_csv():
    saved_data = {'mine': mine,
                  'solider': soldier}
    df = pandas.DataFrame(saved_data)
    df.to_csv('data.csv')


def add_to_csv(index, mine_filed, solider):
    df = pandas.read_csv('data.csv')
    df.loc[index,'mine'] = str(mine_filed)
    df.loc[index, 'solider'] = str(solider)
    df.to_csv('data.csv')


def read_cvs_index(index):
    df = pandas.read_csv('data.csv')
    return df.loc[index]






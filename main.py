per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Money"))
deposit_TKB = int(money * per_cent['ТКБ'] / 100)
deposit_CKB = int(money * per_cent['СКБ'] / 100)
deposit_VTB = int(money * per_cent['ВТБ'] / 100)
deposit_SBER = int(money * per_cent['СБЕР'] / 100)
deposit_list = [deposit_TKB, deposit_CKB, deposit_VTB, deposit_SBER]
print(deposit_list)
max_deposit = max(deposit_list)
print('Максимальная сумма, которую вы можете заработать - ', max_deposit)
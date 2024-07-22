print('Неизменяемые и изменяемые объекты')
print('мои питомцы'.upper())
immutable_var_tuple = ['Карина', 'эль Джавара'], 'собака породы афганская борзая, съедает утром', [
    150], 'грамм сухого корма,вечером', [200], 'грамм сухого корма'
# immutable_var_tuple[3][0]='собака породы овчарка'недопустимая операция,кортеж не поддерживает назначение элементов
print(" ".join(map(str, immutable_var_tuple)))
suma_ = immutable_var_tuple[2][0] + immutable_var_tuple[4][0]
immutable_var_tuple[0][0] = 'Дарина'
immutable_var_tuple[2][0] = 155
immutable_var_tuple[4][0] = 210
print(" ".join(map (str, immutable_var_tuple)))
suma_ = suma_ + immutable_var_tuple[2][0] + immutable_var_tuple[4][0]
mutable_list = ['Лейла-', 'кошка,', 'породы бенгал,', 'возраст 1 год,съедает за день', '85', 'грамм сухого корма']
print(" ".join(mutable_list))
suma_1 = float(mutable_list[4])
mutable_list[0] = 'Ларрм-'
mutable_list[1] = 'кот'
mutable_list[4] = '110'
suma_1 = suma_1 + float(mutable_list[4])
print(" ".join (mutable_list))
suma = (suma_ * 421 / 1000 + suma_1 * 673 / 1000) * 365
print(
    "Собачий корм стоит 421 рубль за килограмм, кошачий корм-673 рубля, следовательно на пропитание своих питомцев за год я потрачу",
    suma, 'рублей')

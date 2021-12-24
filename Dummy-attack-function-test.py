#кубик 20 граней
import random
def dice(damage):
    dice = random.randint(1, 20)
    return dice

#attack_random25 = random.randint(-25, 25)
#характеристики игрока
player = {
    'name': '',
    'health': 100,
    'damage' : 20,
    'armor' : 5,
    'dodge' : 10,
    'hit' : 10
}
#характеристики врага
enemy = {
    'name': 'Dummy',
    'health': 999,
    'damage': 1,
    'armor' : 1,
    'dodge' : 25,
    'hit' : 2
    
}
player['name'] = input('Введите имя: ')
#функиця отображения здоровья 
def printhealth(person):
    print(' у теперь {} {} здоровья '.format(person['name'], person ['health']))
    
#функция атаки
def attack (attacker, attacked):
    if attacker['hit'] + dice(1)  > attacked['dodge']:
        attacked['health'] -= attacker['damage'] / attacked['armor']
        print('Попал!')
    elif dice(1) < attacked['dodge']:
        print('Промах')
combat = 0
while combat >= 0:
    if enemy['health'] <= 0:
        print('Победил ' + player['name'] + "!" )
        break
        
    elif enemy['health'] >= 0: 
        printhealth(enemy)
        attack(player, enemy)
        printhealth(enemy)
        combat = combat +1
    print('Ход: ', combat)
    if combat >= 500:
        print('Время вышло!')
        break





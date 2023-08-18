from random import choice

print("Привет, Игрок!")
print("Я генирирую карту, ты угадываешь цвет масти!")

CARD_NUMBER = ["2","3","4","5","6","7","8","9","10","J","Q","K","T"]
CARD_MAST = ['П', 'Ч','Б','Т']

raund = 1
score = 0
while raund <= 5:
  random_card_number = choice(CARD_NUMBER)
  random_card_mast = choice(CARD_MAST)
  random_card = random_card_number + " " + random_card_mast

  player_answer = input("Какого цвета карта: ")

  if player_answer == 'черный' and random_card_mast in ['П' , 'Т']:
    score = score+1  
    print("Поздравляем, это правильный ответ! Загаданная карта: " + random_card)


  elif player_answer == 'красный' and random_card_mast in ['Ч', 'Б']:
    score = score+1   
    print("Поздравляем, это правильный ответ!Загаданная карта: " + random_card)
   
  elif player_answer != 'красный' and player_answer != 'черный':
       print("Масти такого цвета нет. Загаданная карта: " + random_card)
    
  else:
        print("Это не правильный ответ! Правильный ответ: " + random_card)
  raund = raund+1
   
print('Твой результат', score)

print("Я генирирую карту, ты угадываешь ее масть! Варианты Ч, Б, Т, П.")

raund = 1
score = 0
while raund <= 5:
  random_card_number = choice(CARD_NUMBER)
  random_card_mast = choice(CARD_MAST)
  random_card = random_card_number + " " + random_card_mast
  
  player_answer = input("Какой масти карта: ")
  
  
  if player_answer == 'П' and random_card_mast == 'П':
    score = score+1  
    print("Поздравляем, это правильный ответ! Загаданная карта: " + random_card)
        
  elif player_answer == 'Ч' and random_card_mast == 'Ч':
    score = score+1  
    print("Поздравляем, это правильный ответ! Загаданная карта: " + random_card)
      
  elif player_answer == 'Т' and random_card_mast == 'Т':
    score = score+1  
    print("Поздравляем, это правильный ответ! Загаданная карта: " + random_card)
          
  elif player_answer == ['Б'] and random_card_mast == ['Б']:
    score = score+1  
    print("Поздравляем, это правильный ответ!Загаданная карта: " + random_card)
                     
  else:
    print("Это не правильный ответ! Правильный ответ: " + random_card)
    
  raund = raund+1

print('Твой результат', score)

print("Игра окончена")
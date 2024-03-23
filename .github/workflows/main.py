fav_food = {'Dheya':'Candy', 'Rithu':'Candy','Nivan':'Poori','Gowthami':'Poori','Ratna':'Briyani','Bala':'Poori','Karan':'Candy','KK':'Dosa','Bhu':'Briyani'}
fav_food_sorted = sorted(fav_food.values())
new_arr = {}
for i in fav_food_sorted:
   new_arr[i] = fav_food_sorted.count(i)

temp_arr = new_arr.copy()
tot_cnt = len(new_arr)
r = 0

while tot_cnt > 0:
  food_name = list(temp_arr.keys())[r]
  fav_likes = list(temp_arr.values())[r]
  
  
  max_val = max(list(temp_arr.values()))
  if fav_likes == max_val:
             print(food_name)
             del temp_arr[food_name]
             r = 0 
             tot_cnt = tot_cnt - 1
  else:
      r = r+1

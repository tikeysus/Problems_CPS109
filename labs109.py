# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

import tester109

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False  
    return True  

def only_odd_digits(n):
    if n // 10 == 0 and (n % 10) % 2 == 1:
        return True 
    if n % 2 == 0:
        return False 
    elif n % 2 == 1:
        return only_odd_digits(n // 10)
    
def domino_cycle(tiles):
    if not tiles:
        return True 
    for i in range(len(tiles) - 1):
        if tiles[i][1] != tiles[i + 1][0]:
            return False  
    return tiles[0][0] == tiles[-1][1] 

def is_cyclops(n):
    n = str(n)
    if len(n) % 2 == 0: 
        return False 
    for i in range(len(n) // 2):
        if n[i] == '0':
            return False
        continue 
    for j in range(len(n) // 2 + 1, len(n)):
        if n[j] == '0':
            return False 
    return n[len(n) // 2] == '0' 

def riffle(items, out = True):
    if not items:
        return []
    empty = [] 
    if out:
        for i in range(len(items) // 2):
            empty.append(items[:len(items) // 2][i])
            empty.append(items[len(items) // 2:][i])
    elif not out:
        for i in range(len(items) // 2):    
            empty.append(items[len(items) // 2:][i])
            empty.append(items[:len(items) // 2][i])
    return empty 
#Work on improving this, this code is very lazy (not in a good way lol).

def colour_trio(colours):
    colour_archive = {'rr': 'r', 'bb': 'b', 'yy': 'y', 
                      'ry': 'b', 'rb': 'y',
                      'br': 'y', 'by': 'r',
                      'yr': 'b', 'yb': 'r'} 
    colour_list = list(colours)
    if len(colour_list) == 1:
        return colour_list[0]
    for i in range(len(colour_list) - 1):
        colour_list[i] = colour_archive[colour_list[i] + colour_list[i + 1]]
    colour_list.pop()

    return colour_trio(colour_list)

def extract_increasing(nums):
    if len(nums) == 0:
        return [] 
    
    big = int(nums[0])
    empty = [int(nums[0])]

    start = 1
    end = 2

    while end < len(nums):

        if big < int(nums[start:end]):
            big = int(nums[start:end])
            empty.append(big)
            start = end
            end += 1
        
        else:
            end += 1
    
    if len(nums[start:end]) > 0 and big < int(nums[start:end]):
        empty.append(int(nums[start:end]))

    return empty 

def count_dominators(items):
	if not items:
		return 0 
	
	elif len(items) == 1:
		return 1

	items = items[::-1]
	biggest = items[0]
	count = 1
	
	i = 0
	while i < len(items) - 1:
		if items[i] < items[i + 1] and items[i + 1] > biggest:
			biggest = items[i + 1]
			count += 1
			i += 1
		else:
			i += 1

	return count 

def taxi_zum_zum(moves):
    position = [0,0]
    
    direction = "forward"
    
    for letter in moves:
        if direction == "forward":
            if letter == 'R':
                direction = "right"
            elif letter == 'L':
                direction = "left"
            elif letter == 'F':
                position[1] += 1
                direction = "forward"

        elif direction == "left":
            if letter == 'R':
                direction = "forward"
            elif letter == 'L':
                direction = "back"
            elif letter == 'F':
                position[0] -= 1
                direction = "left"
        
        elif direction == "right":
            if letter == 'R':
                direction = "back"
            elif letter == 'L':
                direction = "forward"
            elif letter == 'F':
                position[0] += 1
                direction = "right"

        elif direction == "back":
            if letter == 'R':
                direction = "left"
            elif letter == 'L':
                direction = "right"
            elif letter == 'F':
                position[1] -= 1
                direction = "back"

    return tuple(position)

def count_growlers(animals):
    growl_count = 0
    for i in range(len(animals)):
        if ((animals[i] == "tac" or animals[i] == "god") and (animals[i + 1:].count("dog") + animals[i + 1:].count("god") > animals[i + 1:].count("cat") + animals[i + 1:].count("tac"))):
            growl_count += 1
        if ((animals[i] == "cat" or animals[i] == "dog") and (animals[:i].count("dog") + animals[:i].count("god") > animals[:i].count("cat") + animals[:i].count("tac"))):
            growl_count += 1
    return growl_count

def words_with_given_shape(words, shape):
	array = [] 
	answer = [] 
	for word in words:
		for i in range(len(word) - 1):
			if (ord(word[i]) < ord(word[i + 1])):
				array.append(1)
			elif (ord(word[i]) > ord(word[i + 1])):
				array.append(-1)
			elif (ord(word[i]) == ord(word[i + 1])):
				array.append(0)
		if (array == shape):
			answer.append(word)
		array = [] 
	return answer



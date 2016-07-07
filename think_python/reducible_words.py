# this is exercise 12.6 from Think Python by Allen Downey
# find the input file here : https://raw.githubusercontent.com/gregorulm/think_python/master/extra/words.txt

words = ['a', 'ab', 'abs', 'abse', 'abse', 'absent']


def reduce(word):
	if word == '':
		return True 
	else:
	   if word in words:
		L = []
		for letter in word:
			L.append(letter)	

		i = 0
  
		while  i < len(word):
			left  = L[:i]
			right = L[i+1:]
			
			child = ''.join(left)+''.join(right)
			
			i += 1 
			if reduce(child):
				return True								
			 
		
	   else: 
		return False 

def string_rotation(string1, string2):
'''O(n) time and O(1) space. The intuition behind this is that a concatenation of string2string2 will have
string1 as a substring'''

	new_string = string2 + string2	
	return string1 in new_string
		
	
x ='waterbottle'
y = 'erbottlewat'

print(string_rotation(x, y))

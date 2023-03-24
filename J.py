s = 'the test string'
print(s.find('e'))
target = 't'
if target in s:
    print('it is in!')
if s.find(target):
    print('we found it!')

print(s.find('long'))
print(s.find('test'))
test_new_str = s.replace('the', 'THR').replace('t', 'U').replace('n', 'N')
print(test_new_str)
print(test_new_str.upper())
print(test_new_str.lower())
print(test_new_str.capitalize())
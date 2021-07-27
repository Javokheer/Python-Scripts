# =============================================================================
# Question 1
# Write a class called Time whose only attribute is a time in seconds. It should have a method called
# convert_to_minutes that returns a string of minutes and seconds formatted as in the following
# example: if seconds is 230, the method should return '5:50'. It should also have
# a method called convert_to_hours that returns a string of hours, minutes, and seconds
# formatted analogously to the previous method.
# 
# =============================================================================
'''Code here for question 1'''

class Time:
    """ Times class converts given input to hours or minute
     INPUT: integer"""

    def __init__(self, time):
        self.time = time

    def convert_to_minute(self):
        """returns input in minutes"""
        mins = self.time // 60
        remaining = self.time % 60
        return f'{mins}:{remaining}'

    def convert_to_hours(self):
        """returns input in hours"""
        time = self.time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return "%d:%d:%d" % (hour, minutes, seconds)


clock = Time(230)
print(clock.convert_to_minute())
print(clock.convert_to_hours())






# =============================================================================
# Question 2
# 
# Write a class called Wordplay. It should have a field that holds a list of words. The user
# of the class should pass the list of words they want to use to the class. There should be the
# following methods:
# 
# • words_with_length(length)— returns a list of all the words of length length
# 
# • starts_with(s)— returns a list of all the words that start with s
# 
# • ends_with(s)— returns a list of all the words that end with s
# 
# • palindromes()— returns a list of all the palindromes in the list
# 
# • only(L)— returns a list of the words that contain only those letters in L
# 
# • avoids(L)— returns a list of the words that contain none of the letters in L
# 
# 
# =============================================================================
'''Code here for question 2'''


from string import punctuation
class Wordplay:
    def __init__ (self, lst):
        self.lst = lst
        for c in punctuation:
            lst = lst.replace(c, '')
            self.list = lst.split()
   
        
    def words_with_length(self):
        return ([len(i) for i in self.list if len(i) > -1])

    def starts_with(self, s):
        return([i for i in self.list if i[:len(s)] == s])

    def  ends_with(self, s):
        return ([i for i in self.list if i[-1*len(s):]== s])
    
    def palindrome(self):
        return([i for i in self.list if i[::-1]==i] )
    
    def only(self, L):
        return([i for i in self.list if 'L' in i])
    
    def avoids(self, L):
        return([i for i in self.list if 'L' not in i])
    
    
z = 'This sis test malayalam is paLendrome'
wordplay = Wordplay(z)
print('List of words length: ', wordplay.words_with_length())
print('Number of words starting with s: ', wordplay.starts_with('s'))  
print('Number of words ending with s: ', wordplay.ends_with('s'))    
print('Palindrome: ', wordplay.palindrome())  
print('Words contains only L: ', wordplay.only('L'))
print('Words w/out L: ', wordplay.avoids('L'))


            

#Another example
from string import punctuation
class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '')
            s = s.lower()
            self.words = s.split()
            
    def number_of_words(self):
        return len(self.words)

    def starts_with(self, s):
        return len([i for i in self.words if i[:len(s)] == s])
    
    def ends_with(self, s):
        return len([i for i in self.words if i[-1*len(s):] == s])

    def number_with_length(self, n):
        return len([i for i in self.words if len(i) == n])
    
s = 'This is a test of the class.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "t":', analyzer.starts_with('t'))
print('Number of words ending with "s":', analyzer.ends_with('s'))
print('Number of 2-letter words:', analyzer.number_with_length(2))



import numpy as np


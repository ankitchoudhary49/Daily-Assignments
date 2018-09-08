'''
Question 1: Extract the user id, domain name and suffix from the following email addresses.
emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
 '''
import re

email1='zuck26@facebook.com'
email2='page33@google.com'
email3='jeff42@amazon.com'
p=re.split('\W',email1)
q=re.split('\W',email2)
r=re.split('\W',email3)
print(p)
print(q)
print(r)

#Question 2: Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
'''
 text = "Betty bought a bit of butter, But the butter was so bitter, So she bought"
 " some better butter, To make the bitter butter better."
 '''
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
findb=re.findall('[bB]\S*',text)
print(findb)

'''
Question 3: Split the following irregular sentence into words

sentence = "A, very very; irregular_sentence"

  desired_output = "A very very irregular sentence"
'''

sent = "A, very very; irregular_sentence"
words=re.sub('\W',' ',sent)
print(words)

'''
Question 4:Clean up the following tweet so that it contains only the user’s message.
That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

 tweet = 'Good advice! RT @TheNextWeb: What I would do differently if
 I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
 '''
tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'

t=re.sub('[@]\w*','',tweet)

t1=re.sub('[h][t][t][p]\S*',' ',t)
t2=re.sub('[c][c][:].*',' ',t1)
t3=re.sub('[R][T]','',t2)
t4=re.sub('[^a-zA-Z0-9]',' ',t3)
print(t4)

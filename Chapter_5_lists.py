musicians = ['Coldplay', 'U2', " Blink 182"]
where_i_lived = ('53.107804754483524,  18.032791856419408', '51.63076642410589, -0.7628566896331929', )
songs_by_musicians = {
  "Coldplay": ["Yellow", "The Scientist"],
  "DJ Hazel": "Rututu"
}


print(songs_by_musicians["Coldplay"])

me = {
  "height": 185,
  "favourite color": "green",
  "favourite game": "Warcraft 3"
}


question_text = '''
Here are the questions you can ask:

1. What is your height?
2. What is your favourite color?
3. What is your favourite game?

Choose the one you want to ask and type the question's number: 
'''

question_asked = input(question_text)

if question_asked == '1':
  print(me["height"])
elif question_asked == '2':
  print(me["favourite color"])
elif question_asked == '3':
  print(me["favourite game"])
else:
  print("This is wrong input...")
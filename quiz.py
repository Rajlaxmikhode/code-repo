
def quiz():
    amount=0
    prize=100
    li=[ {"question":"Which is the longest river in the world 🌎",
        'option':["a. Nile","b. Ganga" ,"c. Amazon", "d. Sharavati"],
        "answer":"a",
        },
        {"question":"Who is the first president of India? ",
         "option":["a. Draupadi Murmu","b. Rajendra Prasad","c.Jawahar Lal Nehru","d. Narendra Modi"],
         "answer":"b"},
         {
             "question":"Even number is a divisible by _ ",
             "option":["a. 3","b. 5","c. 2","d. none"],
             "answer":"c"
         },
          {
             "question":"Who discovered zero 0️⃣",
             "option":["a. Kautilya","b. Aryabhata","c. Kalidasa","d. Euclid"],
             "answer":"b"
         },
          {
             "question":"Who helped vyasa write mahabharata 🚩",
             "option":["a. Sarawati","b. Laxmi","c. Eshwar","d. Ganesh"],
             "answer":"d"
         },
          {
             "question":"What kinnd of mosquito spreads dengue 🦠",
             "option":["a. Aedes","b. Culex","c. Marsh","d. Manasonia"],
             "answer":"a"
         }
        ]
    for q in li:
        print('\n'+q["question"])
        for opt in q["option"]:
            print(opt)

        while True: 
            ans=input("Enter").strip().lower()
            if ans in ("a","b","c","d"):
                break
            else:
                print("Invalid option ❌")

        if ans==q["answer"]:
            print("Correct🥳")
            amount+=prize
        else:
            print("Better luck nxt time 🤞")
  
    print(f"The total amount you won is {amount}")

while True:
   quiz()
   play_again=input("If you want to play again type(yes/y)").strip().lower()
   if play_again!="yes" and play_again!="y":
      print("Thanks for playing ")
      break
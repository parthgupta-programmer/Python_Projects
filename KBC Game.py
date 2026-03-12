import time as t
def ans_finder(write_ans):
    if(write_ans=='A' or write_ans=='a'):
        tem=0
    elif(write_ans=='B' or write_ans=='b'):
        tem=1
    elif(write_ans=='C' or write_ans=='c'):
        tem=2
    elif(write_ans=='D' or write_ans=='d'):
        tem=3
    
    return tem
print("Let's Play,Kaun Banega Crorepati!!\n")
t.sleep(2)
print("I am Parth Gupta ,the host of the game...\n")
t.sleep(2)
print("Fine,let me know your name:",end=" ")
name=input()
print("\n")
print(f"I hope {name} ,you are well aware about the rules of the game...\n")
t.sleep(2)
print("Let me know if you know(Type :YES or NO):",end=" ")
rule=input()
greet_list=["Bravo!!","Well Done!!","Great Job!!","Nice Work!!","Good Answer!!","Well Answered!!","Perfect Response!!","You Nailed it.","Excellent work!","Smart answer!","Good thinking!","Great effort!","Outstanding","Very Very Well Done","You are truly a trivia master!!","Awesome Job!",""]
if((rule=="YES" or rule=="Yes" or rule=="yes")):
    print("\nGreat!!,Alright,Let's Play KAUN BANEGA CROREPATI\n")
    t.sleep(2)
else:
    print("\nJust read the Rules of the game written below properly.\n\n")
    t.sleep(2)
    print("1. Each question has four options. Select the correct one.")
    print("2. Questions get harder as the game progresses with higher rewards.")
    print("3. You are guaranteed a minimum prize amount after crossing specific milestone questions.")
    print("4. Once you confirm your answer, its final. No changes are allowed. However,You can choose to quit and take home your winnings only at any time.")
    print("5. Only your knowledge is allowed. No outside assistance during the game.")
    print("6. The prize money increases with each correct answer, based on the question's difficulty.\n")    
    print("Hopes,you have read the rules of the game properly..\n")
    print("Alright,Let's Play KAUN BANEGA CROREPATI\n")
questions = [
    # Level 1 (Rs. 1,000)
    [
        ["Which layer of the Earth's atmosphere is responsible for the majority of weather phenomena, including clouds and storms?",
        "options"],["Option A.Stratosphere", "Option B.Troposphere\n", "Option C.Mesosphere", "Option D.Exosphere"],
        ["Troposphere"],[1000]
    ],
    # Level 2 (Rs. 2,000)
    [
        ["Which famous Indian emperor, after witnessing the devastation of the Kalinga War, embraced Buddhism and adopted policies based on non-violence and Dharma?"],
        ["Option A.Ashoka", "Option B.Chandragupta Maurya\n", "Option C.Akbar", "Option D.Harsha"],
        ["Ashoka"],[2000]
    ],
    # Level 3 (Rs. 3,000)
    [
        ["The famous battle between Alexander the Great and King Porus took place near which river in modern-day Pakistan?"],
        ["Option A.Indus River", "Option B.Ganges River\n", "Option C.Yamuna River", "Option D.Sarasvati River"],
        ["Indus River"],[3000]
    ],
    # Level 4 (Rs. 5,000)
    [
        ["Which element is considered the foundation of all life on Earth, primarily because it is the key building block of organic molecules?"],
        ["Option A.Oxygen", "Option B.Carbon\n", "Option C.Nitrogen", "Option D.Hydrogen"],
        ["Carbon"],[5000]
    ],
    # Level 5 (Rs. 10,000)
    [
        ["Which physicist is best known for formulating the laws of motion and universal gravitation, which laid the foundation for classical mechanics?"],
        ["Option A.Albert Einstein", "Option B.Niels Bohr\n", "Option C.Isaac Newton", "Option D.Marie Curie"],
        ["Isaac Newton"],[10000]
    ],
    # Level 6 (Rs. 20,000)
    [
        ["Which ancient civilization, known for its impressive pyramids and advances in mathematics, is credited with creating the earliest known written language?"],
        ["Option A.Ancient Rome", "Option B.Ancient Egypt\n", "Option C.Mesopotamia", "Option D.Indus Valley Civilization"],
        ["Ancient Egypt"],[20000]
    ],
    # Level 7 (Rs. 40,000)
    [
        ["The 'Theory of General Relativity' revolutionized our understanding of gravity. Who developed this theory, fundamentally changing the way we view space and time?"],
        ["Option A.Isaac Newton", "Option B.Galileo Galilei\n", "Option C.Albert Einstein", "Option D.Niels Bohr"],
        ["Albert Einstein"],[40000]
    ],
    # Level 8 (Rs. 80,000)
    [
        ["The ancient Greeks introduced the concept of democracy. Which city-state is credited with the first known establishment of democracy?"],
        ["Option A.Athens", "Option B.Sparta\n", "Option C.Corinth", "Option D.Thebes"],
        ["Athens"],[80000]
    ],
    # Level 9 (Rs. 1,60,000)
    [
        ["The Indian epic Mahabharata features several complex moral dilemmas. Which warrior, often considered the greatest archer, was cursed never to fight on the side of righteousness?"],
        ["Option A.Arjuna", "Option B.Karna\n", "Option C.Bhima", "Option D.Duryodhana"],
        ["Karna"],[160000]
    ],
    # Level 10 (Rs. 3,20,000)
    [
        ["The concept of 'Survival of the Fittest' is closely associated with the theory of evolution. Which naturalist is credited with formulating this idea?"],
        ["Option A.Charles Darwin", "Option B.Gregor Mendel\n", "Option C.Louis Pasteur", "Option D.Jean-Baptiste Lamarck"],
        ["Charles Darwin"],[320000]
    ],
    # Level 11 (Rs. 6,40,000)
    [
        ["The Renaissance was a period of immense cultural and intellectual growth in Europe. Which artist is famous for painting the 'Mona Lisa' and 'The Last Supper'?"],
        ["Option A.Leonardo da Vinci", "Option B.Michelangelo\n", "Option C.Raphael", "Option D.Donatello"],
        ["Leonardo da Vinci"],[640000]
    ],
    # Level 12 (Rs. 12,50,000)
    [
        ["Which early 20th-century physicist is known for developing the theory of quantum mechanics and revolutionizing our understanding of atomic and subatomic particles?"],
        ["Option A.Max Planck", "Option B.Albert Einstein\n", "Option C.Niels Bohr", "Option D.Werner Heisenberg"],
        ["Niels Bohr"],[1250000]
    ],
    # Level 13 (Rs. 25,00,000)
    [
        ["The ancient Romans are famous for their engineering feats, such as the construction of aqueducts and roads. Which Roman emperor initiated the construction of the Roman Colosseum?"],
        ["Option A.Julius Caesar", "Option B.Augustus\n", "Option C.Nerva", "Option D.Vespasian"],
        ["Vespasian"],[2500000]
    ],
    # Level 14 (Rs. 50,00,000)
    [
        ["Which important event during the 20th century led to the creation of the United Nations in 1945, aiming to promote international peace and cooperation?"],
        ["Option A.World War I", "Option B.World War II\n", "Option C.Cold War", "Option D.The Korean War"],
        ["World War II"],[5000000]
    ],
    # Level 15 (Rs. 1 Crore)
    [
        ["Which philosopher, known for his work in epistemology and political philosophy, authored 'The Republic,' a work that explores justice, the ideal state, and the theory of Forms?"],
        ["Option A.Aristotle", "Option B.Socrates\n", "Option C.Plato", "Option D.Descartes"],
        ["Plato"],[10000000]
    ],
    # Level 16v (Rs. 7 Crore)
    [
        ["Following the Battle of Waterloo in 1815, which political and military leader was exiled to the island of Saint Helena by the British?"],
        ["Option A.Napoleon Bonaparte","Option B.Louis XVI\n","Option C.Alexander I" ,"Oprion D. Charles X"],
        ["Napolean Bonaparte"],[70000000]
    ]
]
for j in range(len(questions)):
    if(j==0):
        print("Please press ENTER key to get the 1st Question on your Computer screen.",end="")
        enter=input()
        if(enter==""):
            price_won=0
            print(f"Question {j+1} on your Computer screen for Rs.{questions[j][3][0]}:\n")
            print(f"{questions[j][0][0]}\n\n{questions[j][1][0]}   {questions[j][1][1]}{questions[j][1][2]}   {questions[j][1][3]}")
            print("Enter Answer:",end=" ")
            write_ans=input()
            print("\n")
            if(ord(write_ans)==32):
                print("You were playing mindblowing,but unfortunately you are not aware of this question,that's fine Don't Worry,WELL PLAYED!!")
                break
            print("Computer महाशय checking the answer",end="",flush=True)

            for k in range(5):
                print(".",end="",flush=True)
                t.sleep(1)
            f=ans_finder(write_ans)
            print("\n")
            answer=questions[j][1][f]
            correct_answer=questions[j][2][0]
            if( answer.strip().split('.')[1] == correct_answer.strip()):
                price_won=int(questions[j][3][0])
                print(f"{greet_list[j]},Correct Answer....\n")
                t.sleep(3)
                print(f"Won:Rs.{questions[j][3][0]}\n")
                
            else:
                if(j>4 and j<=9):
                    price_won=10000
                if(j>9 and j<=16):
                    price_won=320000
                print("Wrong Answer!!")
                print("Well Played....But,Unfortunately you have given wrong answer!!\n")
                break
    else:
        print(f"Press ENTER key to go to Question No.{j+1}")
        enter2=input()
        if(enter2==""):
            print(f"Question {j+1} on your Computer screen for Rs.{questions[j][3][0]}:\n")
            print(f"{questions[j][0][0]}\n\n{questions[j][1][0]}   {questions[j][1][1]}{questions[j][1][2]}   {questions[j][1][3]}")
            print("Enter Answer:",end=" ")
            write_ans=input()
            if(ord(write_ans)==32):
                print("You were playing mindblowing,but unfortunately you are not aware of this question,that's fine Don't Worry,WELL PLAYED!!")
                break
            print("\n")
            print("Computer महाशय checking the answer",end="",flush=True)
            for k in range(5):
                print(".",end="",flush=True)
                t.sleep(1)
            f=ans_finder(write_ans)
            print("\n")
            answer=questions[j][1][f]
            correct_answer=questions[j][2][0]
            if( answer.strip().split('.')[1] == correct_answer.strip()):
                price_won=int(questions[j][3][0])
                print(f"{greet_list[j]},Correct Answer....\n")
                t.sleep(3)
            else:
                if(j>4 and j<=9):
                    price_won=10000
                if(j>9 and j<=16):
                    price_won=320000
                print("Wrong Answer!!")
                print("Well Played....But,Unfortunately you have given wrong answer!!\n")
                break  
        else:
            print("Sorry ,You have entered wrong key...")
            break
if(price_won<10000000):
    print("You have won Rs.",price_won)
else:
    print("You have become the Crorepati")
    print("Money Won:Rs.",price_won)


print("Thank You....")
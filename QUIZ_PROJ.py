questions ={
    "capital of Andhra pradesh" : "Amaravathi",
    "3 + 3 = ?" : "6",
    "CEO OF GGOGLE" : "SUNDER PICHAI",   
}
def quiz():
    score=0
    for q,ans in questions.items():
        user_ans=input(q+" ")
        if user_ans.lower() == ans.lower():
           score +=1
    print(f"you got a score {score}")

quiz()
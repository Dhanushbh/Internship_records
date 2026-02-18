sample_space=[("Click","Click"),("Click","Scroll"),("Click","Exit"),("Scroll","Click"),("Scroll","Scroll"),("Scroll","Exit"),("Exit","Click"),("Exit","Scroll"),("Exit","Exit")]

print("Sample Space:")
print(sample_space)
print("Total Outcomes:", len(sample_space))

event_click=[]
for items in sample_space:
    if "Click" in items:
        event_click.append(items)
        
click_probability = len(event_click) / len(sample_space)

print("\nOutcomes with at least one Click:")
print(event_click)

print("\nProbability (at least one Click):",click_probability)

#Dice Rolling

import random

trials=1000
sum7_count=0

for item in range(trials):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    if dice1+dice2 == 7:
        sum7_count+=1
        
probability=sum7_count/trials
print("\n\nDice Rolling Experiment:\nTotal Trials:", trials)
print("Number of times sum = 7:", sum7_count)
print("Probability of sum = 7:", probability)




########
prob_head=1/2
prob_six=1/6
prob_head_six_independent=prob_head*prob_six
print(f"Probability of flipping Heads on a coin :{prob_head}\nProbability of rolling a 6 on a die :{prob_six}")
print("Probability of A ^ B :",prob_head_six_independent)

#Marbal Task
total_marbles=10
red=5
blue=5

prob_1st_red=red/total_marbles

red-=1
total_marbles-=1

prob_2nd_red=red/total_marbles
prob_red_red_dependent=prob_1st_red*prob_2nd_red

print(f"Probability of 1st marble being Red:{prob_1st_red}\nProbability of 2nd marble being Red:{prob_2nd_red}")
print("Probability of both marbles being Red (P(A ^ B)) :",prob_red_red_dependent)
#import random to make the question random
import random

#Question CLass
class Question:
    #__init__ method
    def __init__(self, question, ans_1, ans_2, ans_3, ans_4, correct_answer):
        self.question = question
        self.ans_1 = ans_1
        self.ans_2 = ans_2
        self.ans_3 = ans_3
        self.ans_4 = ans_4
        self.correct_answer = correct_answer

    #accessors method
    def get_question(self):
        return self.question
    def get_ans_1(self):
        return self.ans_1
    def get_ans_2(self):
        return self.ans_2
    def get_ans_3(self):
        return self.ans_3
    def get_ans_4(self):
        return self.ans_4
    def get_correct_answer(self):
        return self.correct_answer
        

#Add the trivia questions
q_1 = Question("Secure Shell (SSH)", 53, 25, 22, 548, 22) 
q_2 = Question("Service Location Protocol (SLP)", 427, 143, 23, 3389, 427)
q_3 = Question("Domain Name Server (DNS)", 25, 53, 3389, 143, 53)
q_4 = Question("Internet Message Access Protocol (IMAP)", 143, 53, 3389, 427, 143)
q_5 = Question("Hypertext Transfer Protocol (HTTP)", 22, 427, 80, 143, 80)
q_6 = Question("Remote Desktop Protocol (RDP)", 548, 3389, 25, 21, 3389)
q_7 = Question("Simple Mail Transfer Protocol (SMTP)", 25, 53, 23, 427, 25)
q_8 = Question("Apple Filing Protocol (AFP)", 53, 548, 3389, 143, 548)
q_9 = Question("File Transfer Protocol (FTP)", 21, 80 ,427, 23, 21)
q_10 = Question("Telnet", 548, 80, 427, 23, 23)


#Create the main function
def main():
    #Welcome the user
    print("Welcome to the A+ certification port quiz")

    #create a list of questions
    question_list = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]

    #create score variable
    player1_score = 0
    player2_score = 0
    
    #for loop to ask player 1 and player 2 questions
    for i in range(5):
        p1_question = random.choice(question_list)
        p2_question = random.choice(question_list)
        
        #player 1 questions
        p1_ans = int(input(
            f"Player 1, What port does {p1_question.get_question()} utilize?  {p1_question.get_ans_1()}, "
            f"{p1_question.get_ans_2()}, {p1_question.get_ans_3()} or {p1_question.get_ans_4()}?"))

        #Check for correct answer, add to score if correct and let user know they were correct
        if p1_ans == p1_question.get_correct_answer():
            print("Your answer was Correct")
            player1_score += 1

        #Let user know the answer is incorrect
        else:
            print ("your answer was incorrect")

        #player 2 questions
        p2_ans = int(input(
            f"Player 2, What port does {p2_question.get_question()} utilize?  {p2_question.get_ans_1()}, "
            f"{p2_question.get_ans_2()}, {p2_question.get_ans_3()} or {p2_question.get_ans_4()}?"))
        
        #Check for correct answer, add to score if correct and let user know they were correct
        if p2_ans == p2_question.get_correct_answer():
            print("Your answer was Correct")
            player2_score += 1

        #Let the user know answer is incorrect
        else:
            print("Your answer was incorrect")

    print(f"The Final Result is Player 1 Score: {player1_score} Player 2 Score: {player2_score}")

   
#Test correct answer
#print(q_1.get_correct_answer())

main()

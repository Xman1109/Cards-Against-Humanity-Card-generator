import PIL, os, json
from PIL import Image, ImageDraw, ImageFont
from os import listdir

path = os.path.dirname(os.path.abspath(__file__))+"/".replace("\\", "/")
answer_image = path+"src/answers.png"
question_image = path+"src/questions.png"

card_set_name = input("Card set name: ")
input_file = json.load(open(path+"input.json", "r"))
answers = input_file.get("answers")
questions = input_file.get("questions")

custom_packs = input("Custom pack background? (y/n): ")
if custom_packs == "n":
    blank_answers = Image.open(answer_image)
    blank_questions = Image.open(question_image)
else:
    for i in listdir(path+"src/Custom_Packs/"):
        # print only folders
        if os.path.isdir(path+"src/Custom_Packs/"+i):
            print(i)

pack_location = input("Pack location: (Case sensitive!) ")

if path+"src/Custom_Packs/"+pack_location+"/answers.png":
    blank_answers = Image.open(path+"src/Custom_Packs/"+pack_location+"/answers.png")
else:
    print("No answers.png found in pack location, using default")
    blank_answers = Image.open(answer_image)

if path+"src/Custom_Packs/"+pack_location+"/questions.png":
    blank_questions = Image.open(path+"src/Custom_Packs/"+pack_location+"/questions.png")
else:
    print("No questions.png found in pack location, using default")
    blank_questions = Image.open(question_image)

if path+"src/Custom_Packs/"+pack_location+"/font.ttf":
    given_font = path+"src/Custom_Packs/"+pack_location+"/font.ttf"
else:
    print("No font.ttf found in pack location, using default")
    given_font = path+"src/arial.ttf"

#Row 1
card1x = 55
card1y = 33
card2x = card1x+(300-55)+30
card2y = card1y
card3x = card2x+(300-55)+30
card3y = card1y

#Row 2
card4x = card1x
card4y = card1y+427
card5x = card1x+(300-55)+30
card5y = card4y
card6x = card2x+(300-55)+30
card6y = card4y

#Row 3
card7x = card1x
card7y = card4y+427
card8x = card1x+(300-55)+30
card8y = card7y
card9x = card2x+(300-55)+30
card9y = card7y


# Split into arrays with 9 each
split_answers = [answers[i:i+9] for i in range(0, len(answers), 9)]
split_questions = [questions[i:i+9] for i in range(0, len(questions), 9)]

Font = ImageFont.truetype(font=given_font, size=20)


def line_breaker(answer):
    """
    Breaks a string into multiple lines if its length exceeds 25 characters.
    
    Args:
        answer (str): The string to be broken into multiple lines.
        
    Returns:
        str: The modified string with line breaks.
    """
    if len(answer) > 25:
        for i in range(25, len(answer)):
            if i % 25 == 0:
                # check if the next character is a space, if not, add a hyphen
                if answer[i] != " ":
                    answer = answer[:i]+"-\n"+answer[i:]
                else:
                    answer = answer[:i]+"\n"+answer[i:]
    return answer


v = 0

for answer_set in split_answers:
    answer = answer_set
    with Image.new("RGBA", (blank_answers.width, blank_answers.height), (0, 0, 0, 0)) as img:
        # for i, answer in enumerate(answer_set):
        # after every 25 characters, start a new line to print the rest of the answer, check the answers even after the first line
        img.paste(blank_answers, (0, 0))
        # print answers on image coord 55 33 (card 1)
        draw = ImageDraw.Draw(img)


        # Card1
        answer = line_breaker(answer_set[0])
        draw.text((card1x, card1y), answer, (0, 0, 0), align="left", font=Font)

        if len(answer_set) > 1:
            # Card2
            answer = line_breaker(answer_set[1])
            draw.text((card2x, card2y), answer, (0, 0, 0), align="left", font=Font)

            if len(answer_set) > 2:
                # Card3
                answer = line_breaker(answer_set[2])
                draw.text((card3x, card3y), answer, (0, 0, 0), align="left", font=Font)

                if len(answer_set) > 3:
                    # Card4
                    answer = line_breaker(answer_set[3])
                    draw.text((card4x, card4y), answer, (0, 0, 0), align="left", font=Font)

                    if len(answer_set) > 4:
                        # Card5
                        answer = line_breaker(answer_set[4])
                        draw.text((card5x, card5y), answer, (0, 0, 0), align="left", font=Font)

                        if len(answer_set) > 5:
                            # Card6
                            answer = line_breaker(answer_set[5])
                            draw.text((card6x, card6y), answer, (0, 0, 0), align="left", font=Font)

                            if len(answer_set) > 6:
                                # Card7
                                answer = line_breaker(answer_set[6])
                                draw.text((card7x, card7y), answer, (0, 0, 0), align="left", font=Font)

                                if len(answer_set) > 7:
                                    # Card8
                                    answer = line_breaker(answer_set[7])
                                    draw.text((card8x, card8y), answer, (0, 0, 0), align="left", font=Font)

                                    if len(answer_set) > 8:
                                        # Card9
                                        answer = line_breaker(answer_set[8])
                                        draw.text((card9x, card9y), answer, (0, 0, 0), align="left", font=Font)
        
    img.save(path+"card-sets/"+card_set_name+"-answer-"+str(v)+".png", "PNG")
    v = v + 1

vv = 0

for questions_set in split_questions:
    question = questions_set
    with Image.new("RGBA", (blank_questions.width, blank_questions.height), (0, 0, 0, 0)) as img:
        # for i, question in enumerate(questions_set):
        # after every 25 characters, start a new line to print the rest of the question, check the questions even after the first line
        img.paste(blank_questions, (0, 0))
        # print questions on image coord 55 33 (card 1)
        draw = ImageDraw.Draw(img)

        # Card1
        question = line_breaker(questions_set[0])
        draw.text((card1x, card1y), question, (255, 255, 255), align="left", font=Font)

        if len(questions_set) > 1:
            # Card2
            question = line_breaker(questions_set[1])
            draw.text((card2x, card2y), question, (255, 255, 255), align="left", font=Font)

            if len(questions_set) > 2:
                # Card3
                question = line_breaker(questions_set[2])
                draw.text((card3x, card3y), question, (255, 255, 255), align="left", font=Font)

                if len(questions_set) > 3:
                    # Card4
                    question = line_breaker(questions_set[3])
                    draw.text((card4x, card4y), question, (255, 255, 255), align="left", font=Font)

                    if len(questions_set) > 4:
                        # Card5
                        question = line_breaker(questions_set[4])
                        draw.text((card5x, card5y), question, (255, 255, 255), align="left", font=Font)

                        if len(questions_set) > 5:
                            # Card6
                            question = line_breaker(questions_set[5])
                            draw.text((card6x, card6y), question, (255, 255, 255), align="left", font=Font)

                            if len(questions_set) > 6:
                                # Card7
                                question = line_breaker(questions_set[6])
                                draw.text((card7x, card7y), question, (255, 255, 255), align="left", font=Font)

                                if len(questions_set) > 7:
                                    # Card8
                                    question = line_breaker(questions_set[7])
                                    draw.text((card8x, card8y), question, (255, 255, 255), align="left", font=Font)

                                    if len(questions_set) > 8:
                                        # Card9
                                        question = line_breaker(questions_set[8])
                                        draw.text((card9x, card9y), question, (255, 255, 255), align="left", font=Font)

    img.save(path+"card-sets/"+card_set_name+"-question-"+str(vv)+".png", "PNG")
    vv = vv + 1
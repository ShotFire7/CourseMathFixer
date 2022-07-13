with open('data.txt') as f:
    data = f.read()
with open('data2.txt') as f:
    data2 = f.read()

count = 0
count2 = -1
count3 = 0
count4 = None
answerCount = 0
itemCount = 0
answer = ""
noanswer = False
answerList = []
answerList2 = []
finalList = []

for line in data.splitlines():
    count+=1
    if "radio\" checked" in line:
        count2 = count+2
        count4 = count2+1
    if count == count2:
        count2 = -1
        if "No answer text provided" not in line:
            for char in line:
                if char == "<":
                    count3 = 0
                if count3 == 1:
                    answer = answer+char
                if char == ">":
                    count3 = 1
            answerList.append(answer)
            answer = ""
            count3 = 0
        elif "No answer text provided" in line:
            noanswer = True

    if count == count4:
        if noanswer == True:
            noanswer = False
            count4 = None
            for char in line.split("script type=\"math/tex\" id=\"MathJax-Element-",1)[1]:
                if char == "<":
                    count3 = 0
                if count3 == 1:
                    answer = answer+char
                if char == ">":
                    count3 = 1
            answerList.append(answer)
            answer = ""
            count3 = 0
for i, s in enumerate(answerList):
    answerList[i] = s.strip()

for line in data2.splitlines():
    count+=1
    if "radio\"" in line:
        count4 = count+3


    if count == count4:
        count4 = None
        if "span" in line:
            for char in line.split("script type=\"math/tex\" id=\"MathJax-Element-",1)[1]:
                if char == "<":
                    count3 = 0
                if count3 == 1:
                    answer = answer+char
                if char == ">":
                    count3 = 1
            answerList2.append(answer)
            answer = ""
            count3 = 0
        else:
            answerList2.append(line)


for i, s in enumerate(answerList2):
    answerList2[i] = s.strip()
for item in answerList2:
    answerCount +=1
    if answerCount > 4:
        answerCount = 1
    for answer in answerList:
        if item == answer:
            finalList.append(answerCount)
            
print(finalList)
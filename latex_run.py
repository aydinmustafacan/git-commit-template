import os

latex_filename = "term-paper-cmpe475"
myCmd1 = ['pdflatex '+latex_filename+'.tex','bibtex '+latex_filename+'.aux','pdflatex '+latex_filename+'.tex','pdflatex '+latex_filename+'.tex']

commands = []
commands.append(myCmd1)

k =1
for j in commands:
    for i in j:
        print(i)
        os.system(i)

    print("step "+str(k)+" completed!")
    k = k+1


print("Program is completed")
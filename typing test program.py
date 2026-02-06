import time
import math
class TypingTest:
        def __init__(self):
            pass 
        def line1(self):
            l1="qwert poiuy qwert poiuy qwert poiuy qwert poiuy "
            print(l1)
            print("shown below type like that: ")
            start = time.time()
            typed=input("start typinhg : ")
            end= time.time() 
            time_diff=round(end-start,2)
            if(typed==l1):
                print("correct")
            else:
                print("incorrect")
            correct=0
            for ch1,ch2 in zip(l1,typed):
                if ch1==ch2:
                    correct +=1
            lilen=len(l1)
            accuracy=round((correct/lilen)*100,2)


            print("taken time is second",time_diff)
            print("accuracy is ",accuracy)   

        def line2(self):
            l2="asdfg';lkjh asdfg';lkjh asdfg';lkjh asdfg';lkjh"
            print(l2)
            print("shown below type like that: ")
            start = time.time()
            typed=input("start typing : ")
            end= time.time() 
            time_diff=round(end-start,2)
            if(typed==l2):
                print("correct")
            else:
                print("incorrect")
            correct=0
            for ch1,ch2 in zip(l2,typed):
                if ch1==ch2:
                    correct +=1
            lilen=len(l2)
            accuracy=round((correct/lilen)*100,2)

            print("taken time is second",time_diff)
            print("Accuracy is",accuracy)

        def line3(self):
            l3="abcdefghijklmnopqrstuvwxyz"
            print(l3)
            print("shown below type like that: ")
            start = time.time()
            typed=input("start typing : ")
            end= time.time() 
            time_diff=round(end-start,2)
            if(typed==l3):
                print("correct")
            else:
                print("incorrect")
            correct=0
            for ch1,ch2 in zip(l3,typed):
                if ch1==ch2:
                    correct +=1
            lilen=len(l3)
            accuracy=round((correct/lilen)*100,2)

            print("taken time is second",time_diff)
            print("Accuracy is",accuracy) 

        def line4(self):
            l4="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            print(l4)
            print("shown below type like that: ")
            start = time.time()
            typed=input("start typing : ")
            end= time.time() 
            time_diff=round(end-start,2)
            if(typed==l4):
                print("correct")
            else:
                print("incorrect")
            correct=0
            for ch1,ch2 in zip(l4,typed):
                if ch1==ch2:
                    correct +=1
            lilen=len(l4)
            accuracy=round((correct/lilen)*100,2)

            print("taken time is second",time_diff)
            print("Accuracy is",accuracy) 

        def line5(self):
            l5="The quick brown fox jumps over the lazy dog"
            print(l5)
            print("shown below type like that: ")
            start = time.time()
            typed=input("start typing : ")
            end= time.time() 
            time_diff=round(end-start,2)
            if(typed==l5):
                print("correct")
            else:
                print("incorrect")
            correct=0
            for ch1,ch2 in zip(l5,typed):
                if ch1==ch2:
                    correct +=1
            lilen=len(l5)
            accuracy=round((correct/lilen)*100,2)

            print("taken time is second",time_diff)
            print("Accuracy is",accuracy) 

  
        def line6(self):
            l6="There are many different ways to organize a paragraph. The organization you choose will depend on the controlling idea of the paragraph. Below are a few possibilities for organization, "
            print(l6)
            print("shown below type like that: ")
            start = time.time()
            typed=input("start typing : ")
            end= time.time() 
            time_diff=round(end-start,2)
            if(typed==l6):
                print("correct")
            else:
                print("incorrect")
            correct=0
            for ch1,ch2 in zip(l6,typed):
                if ch1==ch2:
                    correct +=1
            lilen=len(l6)
            accuracy=round((correct/lilen)*100,2)

            print("taken time is second",time_diff)
            print("Accuracy is",accuracy) 

          

        def showval(self):
              l1="qwert poiuy qwert poiuy qwert poiuy qwert poiuy "
              l2="asdfg';lkjh asdfg';lkjh asdfg';lkjh asdfg';lkjh"
              l3="abcdefghijklmnopqrstuvwxyz"
              l4="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
              l5="The quick brown fox jumps over the lazy dog"
              l6="There are many different ways to organize a paragraph. The organization you choose will depend on the controlling idea of the paragraph. Below are a few possibilities for organization, "            
              print("1. ",l1)
              print("2. ",l2)
              print("3. ",l3)
              print("4. ",l4)
              print("5. ",l5)
              print("6. ",l6)
              print("choose the option between 1 2 3 4 5 or 6")
              myline= input("option :-")
              if myline=="1":
                self.line1()
              elif myline=="2":
                self.line2()
              elif myline=="3":
                self.line3()
              elif myline=="4":
                self.line4()
              elif myline=="5":
                self.line5()
              elif myline=="6":
                self.line6()
              else:
                print("choose ans is invalid")

a="yes"
test = TypingTest()
while a == "yes" or a == "y":
      test.showval()
      a=input("continue? yes/no :- ")
progress = 0
progress_mt = 0
module_retriever = 0
exclude = 0
all_inputs = []
decision = "y"
total_outcomes = 0

inputs = open("inputs.txt","w")                             #part 4

while decision == "y":                                      #part 1
    
    while True:
        try:
            
            while True:
                try:
                   pass_ = int (input("Enter the pass credit: "))
                   if (pass_%20==0) and (pass_>=0) and (pass_<121):
                       break
                   else:
                       print ("out of range")
                   
                except ValueError :
                       print("integer required")
            while True:
                try:
                   defer_ = int (input("Enter the defer credit: "))
                   if (defer_%20==0) and (defer_>=0) and (defer_<121):
                      break
                   else:
                       print ("out of range")
                   
                except ValueError :
                       print("integer required")
            while True:
                try:
                   fail_ = int (input("Enter the fail credit: "))
                   if (fail_%20==0) and (fail_>=0) and (fail_<121):
                      break
                   else:
                       print ("out of range")
                   
                except ValueError :
                       print("integer required")
            if(120 == pass_ + defer_ + fail_ ):
                break
            else:
                raise Exception
        except Exception:
            print("total incorrect")

    total_outcomes = total_outcomes + 1

    if  (pass_ == 120):
        progression_outcome = "Progress"
        print ("progress")
        progress = progress + 1
        
    elif(pass_ == 100):
        progression_outcome = "Progress(Module trailer)"
        print ("progress(module trailer)")
        progress_mt = progress_mt + 1
        
    elif(fail_ >= 80):
        progression_outcome = "Exclude"
        print("exclude")
        exclude = exclude + 1

    else:
        progression_outcome = "Module retriever"
        print("module retriever")
        module_retriever = module_retriever + 1      


    all_inputs.append(progression_outcome + ' - ' + str(pass_) + ", " + str(defer_) + ", " + str(fail_) + '\n')


    while True:
        decision = input("Enter y to try again or q to exit: ")
        if (decision == "q" or decision == "y"):
            break
        else:
            print ("Enter either y or q")
                      
print ("------------------------------------------------------------------------")
print ("Horizontal histogram")            


print ("progress: " + str(progress) +"            :" , end="")
print (progress * '*')

print ("progress_mt: " + str(progress_mt) +"         :" , end="")
print (progress_mt * '*')

print ("module_retriever: " + str(module_retriever) + "    :" , end="")
print (module_retriever * '*')

print ("exclude: " + str(exclude) +"             :" , end="")
print (exclude * '*')

print (str(total_outcomes) + "  outcomes in total")
print ("------------------------------------------------------------------------")

print ("Verticle histogram")

histogram = [[],[],[],[]]                         #part 2

for i in range(progress):
    histogram[0].append('   *   ')
for i in range(progress_mt):
    histogram[1].append('   *   ')    
for i in range(module_retriever):
    histogram[2].append('   *   ')
for i in range(exclude):
    histogram[3].append('   *   ')
 
if progress>=progress_mt and progress>=module_retriever and progress>=exclude :
    largest = progress
elif progress_mt>=module_retriever and progress_mt>=exclude :
    largest = progress_mt
elif module_retriever>=exclude :
    largest = module_retriever
else:
    largest = exclude

print("progress trailing retriever exclude")
for i in range(largest):
    for j in histogram:
        try:
            print (j[i], end="  ")
        except:
            print ("        ", end=" ")
    print("")        
print (str(total_outcomes) + "  outcomes in total")
print("------------------------------------------------------------------------")            

for i in range (len(all_inputs)):                 #part 3
    print (all_inputs[i])

print("------------------------------------------------------------------------")
   
inputs.writelines(all_inputs)                     #part 4
inputs.close()

print ("Data in the text file:")
inputs = open('inputs.txt','r')
content = inputs.read()
print (content)
inputs.close










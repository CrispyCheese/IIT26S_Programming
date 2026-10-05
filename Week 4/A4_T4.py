print ("Program starting.\n")

Words = 0
Characters = 0

while True:
    Feed = input("Insert word (empty stops): ")
    if (len(Feed) == 0):
        break
    else:
        Words = Words + 1
        Characters = Characters + len(Feed)
print (f"\nYou inserted:\n- {Words} words\n- {Characters} characters\n")

print ("Program ending.")
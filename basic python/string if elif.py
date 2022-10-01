indian=["somucha","porota"]
bd=["chicken","beef"]
dish=input("enter a dish name:")
if dish in indian:
    print("indian food")
elif dish in bd:
    print("bangladeshi food")
else:
    print("not any cuisine",dish)
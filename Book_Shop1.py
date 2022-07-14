order = [[34587,'Learning Python','Mark Lutz',4,40.95],
         [98762,'Programming Python','Mark Lutz',5,56.80],
         [77226,'Head First Python','Paul Barry',3,32.95],
         [88112,'Einführung in Python3','Bernd Klein',3,24.99]
        ]

orderList = []
for product in order:
    if product[-1]*product[-1]<100:
        orderList.append((product[0],product[-1]*product[-2]+10))
    else:
        orderList.append((product[0],product[-1]*product[-2]))
print("Order Summary:",orderList) 

print("Order Summary: ", [(product[0],product[-1]*product[-2]+10) if product[-1]*product[-2]<100 else (product[0],product[-1]*product[-2]) for product in order])
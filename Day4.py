cpu_hours=int(input("Enter the number of cpu hours:"))
storage=int(input("Enter storage in gb:"))
data_transfer=int(input("Enter data transfer in gb:"))
cpu_cost=cpu_hours*5
storage_cost=storage*2
data_transfer_cost=data_transfer*1
total_amount=cpu_cost+storage_cost+data_transfer_cost
if cpu_hours>100:
    print(total_amount+500)
else:
    print(total_amount)
num_seats, num_group=input().split()

ns=int(num_seats)
ng=int(num_group)


seats=[False]*ns

for i in range(ng):
    num, init=input().split()

    num=int(num)
    init=int(init)
    if not True in seats[init-1:init+num-1]:
        seats[init-1:init+num-1]=[True]*num

print(seats.count(True))
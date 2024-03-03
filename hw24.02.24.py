def create_dict( * args):
    return dict(zip(args, args))

print(create_dict(1,2,3,5,6,7))
print(create_dict('grey', (2, 17), 3.11, -4))
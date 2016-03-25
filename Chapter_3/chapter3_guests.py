guests = ['amaz', 'kripp', 'trump', 'kibler', 'forsen', 'hafu']

print(guests)
noshow = 'hafu'

guests.remove(noshow)

print(guests)

print("\nIt seems that " + noshow.title() + " can't come!")

print("We are having a streamer party, " + guests[0].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[1].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[2].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[3].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[4].title() + "! I hope you can come!")

guests.insert(0, "bob")
guests.insert(4, "adwata")
guests.append("merps")
print(guests)

print("We are having a streamer party, " + guests[0].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[1].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[2].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[3].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[4].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[5].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[6].title() + "! I hope you can come!")
print("We are having a streamer party, " + guests[7].title() + "! I hope you can come!")

nomore = guests.pop()
print("Not having that party anymore, " + nomore.title() + "!")

nomore = guests.pop()
print("Not having that party anymore, " + nomore.title() + "!")

nomore = guests.pop()
print("Not having that party anymore, " + nomore.title() + "!")

nomore = guests.pop()
print("Not having that party anymore, " + nomore.title() + "!")

nomore = guests.pop()
print("Not having that party anymore, " + nomore.title() + "!")

nomore = guests.pop()
print("Not having that party anymore, " + nomore.title() + "!")

print(guests)

print("Still invited, " + guests[0].title() + "!")
print("Still invited, " + guests[1].title() + "!")

del guests[0]
del guests[0]

print(guests)
# base string demo

# strip " ",\t,\n, but not strip string inner
s = "   Hello,  world! \t\t\n";
print(s.strip())

# two blank
# split by blank
# print ['Hello,', 'world!']
s = "Hello,  world!"
print(s.split())

# two blank
# print ['Hello,', '', 'world!']
s = "Hello,  world!"
print(s.split(" "))

st = "Hello World! \t\t\n"
print(st.split())

# split by .
# print ['www', 'networksciencelab', 'com']
uri = "www.networksciencelab.com"
print(uri.split("."))

# alought , join
# print alpha,bravo,charlie,delta
s = ",".join(["alpha", "bravo", "charlie", "delta"])
print(s)

s = "-".join("1.617.305.1985".split("."))
print(s)


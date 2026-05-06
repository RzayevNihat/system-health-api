def gravitaion(g,m1,m2,r):
    return g*(m1*m2/r**2)
G = 6.674e-11
m1_a = 1.989e30 
m2_a = 5.972e24  
r_a = 149_597_870_000 
m1_b = 70 
m2_b = 0.5
r_b = 0.75 

f_a=gravitaion(G,m1_a,m2_a,r_a)
f_b=gravitaion(G,m1_b,m2_b,r_b)
print(f_a,f_b)
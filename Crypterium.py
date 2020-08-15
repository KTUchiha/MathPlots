""" This code solves a cryptarium puzzle send+more=money by trying all the possible solution and giving us about 10 solutions that work that we can choose from. I know 
for sure that s=9 m=1 and o=0 because money has five digits and it means that there has to be a carryover. Using that information, I was able to say for sure that s=9
m=1 and o=0. Then I just test every possible solution using a bunch of for loops. After all that i put an if statement to see if the solutions work and then print them out.
Lastly, once i have all the solutions i just look through them to see which ones have varibles that are repeats. If you want to avoid looking through
all the solutions you can use sets in your program.
c


"""


# S, E, N, D, M, O, R, Y 
s=9 
m=1
o=0
for e in range(2,9):
    for n in range(2,9):
        for d in range(2,9):
            for r in range(2,9):
                for y in range(2,9):
                    if ((s*1000 + e*100 +n*10 +d )+ (m*1000 +o*100 + r*10 + e ) == (m*10000+o*1000+n*100+e*10+y)):
                        print(f's={s},e={e},n={n},d={d},m={m},o={o},r={r},y={y}')
                    
                    
                    
    

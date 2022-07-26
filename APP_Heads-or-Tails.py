import random

random_num = random.randint(0,1)
print(random_num)
if random_num == 1:
    print("Heads!")
    print(r"""
                            __
     ,                    ," e`--o   <=====
    ((                   (  | __,'
     \\~----------------' \_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'

      """)
else:
    print ("Tails!")
    print(r"""
                            __
     ,                    ," e`--o
    ((   <=====          (  | __,'
     \\~----------------' \_;/
     (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'
     """)

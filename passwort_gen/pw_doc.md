# Password Generator Documentation

Correleated to the Python programm PW_Gen.py

- [x] Manipulate string couple times by using random integers inbetween user-string to add characters and therefore create a "better password"

- [ ] Add check where User input will not be visible in password, no duplicates!

- [ ] (Optional) Maybe add according to input instead of set integers in line 58. 'if list == result'

- [ ] Add back if statement for 3 duplicate letters behind each other / lenght is < 3.

- [ ] Make Each password look individual af.

- [ ] (Optional) Add numbers and more to the generator.

---
## Code

First Attempt for no duplicates.
```py

if u_input[::-1].lower() in result_str[-len_u_input::-1].lower() or u_input[-3::-1].lower() in result_str[-3::-1].lower():
                while rng_letter != result_str[-1:]:
                    rng_letter = random.choice(string.ascii_letters)
                    if rng_letter == result_str[-1:]:
                        break
                result_str = str(rng_letter)
                    
            elif rng_list_letter.lower() in result_str[-3::-1].lower() or rng_list_letter.lower() in result_str[-2:].lower(): 
                result_str = str(rng_letter)
            else:
                result_str = str(rng_list_letter) 
```
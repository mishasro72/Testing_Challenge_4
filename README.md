# Testing Challenge #4 - generate testing data

---

## Task:

### **What to do**
Create 5 valid data input for the specification below.

Enter them 1 at a time until you reach 5.

This challenges emphasizes the skill required to create your own test data.


**Specification**
Each person born in Romania receives a unique identification number.

The number has 13 digits, e.g. 1234567890123

What the digits represent:

First digit – the gender: male or female
1 or 2 – born between 1 January 1900 and 31 December 1999
3 or 4 - born between 1 January 1800 and 31 December 1899
5 or 6 - born between 1 January 2000 and 31 December 2099
7 or 8 – Foreign residents in Romania.
9 - For non-residents
Next 2 digits – last 2 digits of the year of birth (e.g. born in 1980 then it will 80 )
Next 2 digits – month of birth (01 to 12)
Next 2 digits - date of birth (01 to 31 depending on the month of birth)
Next 2 digits – area code (valid codes are 01 to 52)
Next 3 digits – order number
Last digit control number is created by:
Take the first 12 numbers of the CNP: 123456789012 and multiply each number with the corresponding position number from this string: 279146358279 like: 1 * 2 + 2 * 7 + 3 * 9 + 4 * 1+…..+ 12 * 9= X
You divide X by 11 the rest obtained if it is 10 then the last digit is 1 otherwise it equals the rest obtained

---
## **What does this code do?**
This code helps you create valid testing data. All you need to do is just run it and enter a date of birth (optional: foreign or non-resident status).

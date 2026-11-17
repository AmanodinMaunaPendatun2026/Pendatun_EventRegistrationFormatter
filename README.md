# Student Event Registration Formatter

## Description
This program formats student event registration details.

## Language Used
Python

## String Feature Used
strip(), title(), upper()

## Date/Time Feature Used
datetime, strftime()

## Version History
- Version 1: Basic input and output
- Version 2: Added string formatting
- Version 3: Added date formatting

## Sample Output
```text
Student Event Registration Summary
Name: Amanodin M. Pendatun
Name Code: AMANODIN M. PENDATUN
Section: ROSAL
Event: Cos(P)lay
Event Date: November 14, 2026
Language Used: Python
String Feature Used: strip(), title(), upper()
Date/Time Feature Used: datetime
Registration record created successfully.


Reflection
In my first version, my program could only accept raw user inputs and print them without cleaning spaces or formatting dates. I improved my program by adding string manipulation and date formatting in separate versions. The string methods I used were strip(), title(), and upper() because they remove extra spaces and standardize capitalization for names and sections. The date/time feature I used was the datetime module because it converts numeric year, month, and day inputs into a readable month name format. The biggest change in my program was turning messy raw text and numbers into a clean, organized registration summary.

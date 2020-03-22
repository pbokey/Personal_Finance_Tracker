# Personal Budget Tracker Backend

I wanted to make a personal budget tracker becuase, I felt as though all the budget tracking apps already out there did not offer the flexibility and simplicity that I was looking for. 

Currently, a lot of times I am actually spending more on my card then in reality, since I will buy for friends/split things and then they will pay me back through another app. 
These other apps do not really do a good job in keeping track of all these sources of income.

Another issue I face with these apps is that they try to do to much and have "algorithms" or "AI" that will categorize your purchases for you. In my case, I have found that they categorize around 40% of my purchases incorrectly which also messes up the budgeting tools for that application, meaning I need to go in and manually change some of the categories of the charges in order to fix my budget. This ends up being more work. Why not just get it right from the start?

This is a python backend that will have exposed endpoints that will allow any simple application that can make HTTP requests send data to this backend that will then store it in a local csv. Super simple, super easy. Each request will contain the pertinent information about the debit/credit: amount, type (food, travel, etc), and vendor/source. Thats it - no extra bells and whistles needed. From this .csv file I can then create vizulations using other python scripts or simply load it into an excel spreadsheet.

The motivation for this project is simply: KISS - keep it simple stupid 
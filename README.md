## Thank you for using Restrictive Pairs
Once you've given a list of names, this program will **generate a list of peers**. But that's not all: this one will **remember peers who have already fallen out**, so that they **don't get back together again**, before getting together with other people.

## How can it be useful?
I did this job because **a company needed it**. In fact, they had started an activity where, once a week, **random people from the company would get together to tell each other how their jobs works**, or even to improve team cohesion. This took place over a coffee break, and they didn't want people to meet again.

### More precisions on the functioning of the software.
**You can enter each person's first name, last name and team**. **If you put 2 people on the same team, they'll never get together**. This is to prevent people who already know each other from falling in with each other.

### Options.json
In this file, you can configure 2 things:

 - tolerance: If sometimes, peer calculations are difficult, then increasing the tolerance will increase the time allowed for these calculations. Leaving the tolerance above 100000 is often useless, and it's better to increase the destroyEverything instead.

 - destroyEverything: So, yes, the name may sound strange, but in fact, if the value is set to 1, it means that each person will meet another once. Once he's met them all, he'll be able to meet everyone again, and the list of people he's seen will be completely destroyed (you understand the name now). It's absolutely not advisable to set the variable above 0.9, as this would make the program run very poorly. It is often recommended to leave the variable between 0.7 and 0.8, depending on the number of people you have put.

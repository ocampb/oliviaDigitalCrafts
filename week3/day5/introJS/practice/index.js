/*
 * Exercise 0
 * Create an array of names; loop over the array and print each name to the console
 */


const names = ["Olivia", "Tyler", "Mary"]

for (let i = 0; i < names.length; i++) {
    console.log(names[i])
}


/*
 * Exercise 1
 * Create an array of names; loop over the array and print each name AND the index to the console
 * example output
 * 0. Tyler
 * 1. Olivia
 * 2. Winnie
 */

for (let i = 0; i < names.length; i++) {
    console.log(i + ". " + names[i])
}


// for (let i=0; )


/*
 * Exercise 2
 * Create a function that accepts an array of numbers as the parameter; the function should return the sum of all numbers in the array
 */

// def myfunction():
//     print ("Hi")

// function myfunction(){console.log("Hi")}

// myfunction()

let olivia = 0
function sumfunction(number1, number2) { return (number1 + number2)}
olivia = sumfunction(1, 2)
console.log(olivia)

/*
BONUS

Convert the python class to a javascript class


class Dog:
    def __init__(self, name, energy, attention, profile):
        self.name = name
        self.energy = energy
        self.attention = attention
        self.profile = profile
    def updateEnergy(self, updateAmount):
        self.energy = self.energy + updateAmount
    def listAttentionSpan(self):
        print ("Attention Span = " + str(self.attention))
    def listEnergy(self):
        print("Energy = " + str(self.energy))
    def listProfile(self):
        print (self.profile)

Winnie = Dog("Winnie", 10, 3, "Winnie is an energetic puppy who loves chewing on bones, digging holes and playing with friends. Winnie has never met a stranger - she's friendly to all new dogs and humans. Her birthday is on August 8th and she'll be one year old! She has a high energy level but a low attention span for completing tasks. ")
*/
class Cat {
    constructor (name, energy){
        this.name = name
        this.energy = energy
    }
    meow (){
        console.log("Meow, my name is " + this.name)
    }
}

const gus = new Cat("Gus", 10)
gus.meow()
const fs = require('fs');

class BreadFactory{
    makeBread(breadType, flour, water, sugar){
        return new Bread(breadType, flour, water, sugar);
    }

    makeBreadsFromJson(fileName){
        let breads=[];
        const result = fs.readFileSync(fileName,'utf-8')
        JSON.parse(result).map(bread=>{
            breads.push(this.makeBread(bread.breadType, bread.flour, bread.water, bread.sugar))
        })
        return breads;
    }
}

class Bread{
    breadType;
    flour;
    water;
    sugar;

    constructor(breadType, flour, water, sugar){
        this.breadType = breadType;
        this.flour = flour;
        this.water = water;
        this.sugar = sugar;
    }

    toString(){
        console.log(`breadType: ${this.breadType}`);
        console.log(`recipe`);
        console.log(`flour: ${this.flour}`);
        console.log(`water: ${this.water}`);
        console.log(`sugar: ${this.sugar}`);
        console.log('');
        
    }
}

const factory = new BreadFactory();
const breads = factory.makeBreadsFromJson('./bread.json')
breads.map(bread=>{
    bread.toString();
})

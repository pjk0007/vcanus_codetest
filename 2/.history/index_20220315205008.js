class Calculator{
    constructor(){
        this.num = 0;
    }

    add(num){
        this.num+=num;
        return this;
    }

    substract(num){
        this.num-=num;
        return this;
    }

    out(){
        return this.num;
    }
}

calculator = new Calculator();

result = calculator.add(4).add(5).substract(3).out();
console.log(result);

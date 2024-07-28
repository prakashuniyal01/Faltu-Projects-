
// public class constructors 
class Pendrive {
    public company: string;

    constructor( name: string){
        this.company = name
    }
}



const p1 = new Pendrive('company')
console.log(p1);
const p2 = new Pendrive('solo')
console.log(p2);

/* access modifier 
   private 
*/


class User {
    private balance = 100;

    getBalance ( n : number ){
        this.balance = n; 
    }
}


const bal = new User()

console.log(bal);

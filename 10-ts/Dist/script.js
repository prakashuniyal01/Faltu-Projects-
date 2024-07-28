"use strict";
// public class constructors 
class Pendrive {
    constructor(name) {
        this.company = name;
    }
}
const p1 = new Pendrive('company');
console.log(p1);
const p2 = new Pendrive('solo');
console.log(p2);
/* access modifier
   private
*/
class User {
    constructor() {
        this.balance = 100;
    }
    getBalance(n) {
        this.balance = n;
    }
}
const bal = new User();
console.log(bal);

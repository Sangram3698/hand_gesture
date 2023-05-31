// const arr=[
//   "Sangram",
//   42,
//   function(){console.log('Hi there')}
// ,]

// for(let i=0;i<arr.length;i++){
//   console.log(arr[i])
// }






// const x=42;
// console.log(typeof(x));
// console.log(typeof(null));





// const obj={
//   firstname:"sangram",
//   lastName:"Bhandari",
//   address:{
//     street:3,
//     ally:"banganga",
//   },
//   age:21,
// }
// console.log(obj.address.ally)













// function makeFunctionArray(){
//   const arr=[]

//   for(let i=0;i<5;i++){
//     arr.push(function(){console.log(i)})
//   }
//   return arr
// }

// const functionArr=makeFunctionArray();

// functionArr[0]()







// const sayHello=(function(){
//   var message='hello!'


//   function sayHello(){
//     console.log(message)
//   }
//   return sayHello
// })()


// let counter=(function(){
//   let count=0
//   return{
//     inc:function(){count=count+1},
//     get:function(){console.log(count)}
//   }
// })()

// counter.inc()
// counter.get()
// counter.get()






// const x=[0,1,2,3,4,5]

// function addOne(num){
//   return num + 1
// }

// function greater(num){
//   return num>1
// }

// function add(x,y){
//     return x+y
// }

// console.log(x.map(addOne))

// console.log(x.filter(greater))

// console.log(x.reduce(add))



function map(arr,fun){
  const newArr=[]

  for(let i=0;i<arr.length;i++){
    let val = arr[i]
    newArr.push(fun(val))
  }
  return newArr
}

function add(num){
  return num+2
}
const x=[0,1,2,3,4,5,6,7,8,9]

console.log(map(x,add))
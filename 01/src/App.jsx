import { useState } from 'react'

const App = () => {
  let [counter, setCounter  ]  = useState(0)
   
  // let counter = 5;
  const addValue = () =>{
    // counter = counter + 1;
  
    setCounter(prevCount => (prevCount < 20 ? prevCount + 1 : prevCount))
    console.log(counter);
  }

  const removeValue = () =>{
    // counter = counter -1;
    setCounter(prevCount => (prevCount > 0 ? prevCount - 1 : prevCount))
    console.log(counter);
  }
  
  return (
    <>
      <div className='text-center' >
        <h1>hello counter app</h1>

        <h2>Counter value {counter}</h2>

        <button className='rounded-md p-9 bg-slate-900 text-slate-100' onClick={addValue} > {counter} add Value</button>
        <br />
        <button onClick={removeValue} >remove Value {counter} </button> 
      </div>

    </>
  )
}

export default App
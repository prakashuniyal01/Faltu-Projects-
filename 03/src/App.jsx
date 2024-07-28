
import { useState } from 'react'

const App = () => {
  const [color, setColor] = useState("olive")
  return (
    <div className='w-full h-screen duration-200'
      style={{ backgroundColor: color }}
    >
      <div className='fixed flex flex-wrap justify-center  bottom-12 inset-x-0 px-2' >
        <div className='flex flex-wrap justify-center bg-white gap-3 shadow-lg px-3 py-2  rounded-3xl' >
          <button onClick={() =>{setColor("red")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "red" }}
          >red</button>
          <button onClick={() =>{setColor("Green")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "Green" }}
          >Green</button>
          <button onClick={() =>{setColor("yellow")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "yellow" }}
          >yellow</button>
          <button onClick={() =>{setColor("Blue")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "Blue" }}
          >Blue</button>
          <button onClick={() =>{setColor("Gray")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "Gray" }}
          >Gray</button>
          <button onClick={() =>{setColor("pink")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "pink" }}
          >pink</button>
          <button onClick={() =>{setColor("black")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "black" }}
          >black</button>
          <button onClick={() =>{setColor("magenta")}} className='outline-none px-4 py-1 rounded-full text-white shadow-lg'
            style={{ backgroundColor: "magenta" }}
          >magenta</button>

        </div>
      </div>
    </div>

  )
}

export default App
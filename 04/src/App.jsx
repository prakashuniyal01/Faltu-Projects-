import { useState, useCallback, useEffect, useRef } from 'react'

function App() {
  const [length, setLengths] = useState(8)
  const [numberAllowed, setNumberAllowed] = useState(false)
  const [charAllowed, setCharAllowes] = useState(false)
  const [password, setPassword] = useState("")

  // useRef hook

  const passworRef = useRef(null)

  const passwordGenerator = useCallback(() => {
    let pass = ""
    let str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz"

    if (numberAllowed) str += "0123456789"
    if (charAllowed) str += "~!@#$%^&*()_+={}|:,./"

    for (let i = 1; i <= length; i++) {
      let char = Math.floor(Math.random() * str.length + 1)
      pass += str.charAt(char)
    }
    setPassword(pass)
  }, [length, numberAllowed, charAllowed, setPassword])

  const copyPassworfToClipboard  = useCallback(() =>{
    passworRef.current?.select();
    // passworRef.current?.setSelectionRange(0,4)
    window.navigator.clipboard.writeText(password)
  },[password])
  
  useEffect(() =>{
    passwordGenerator()
  },[length, numberAllowed, charAllowed, passwordGenerator])


  return (
    <>
      <div className='w-full max-w-md px-4 py-3 mx-auto my-8 text-orange-600 bg-gray-500 rounded-lg shadow-md '>
        <h1 className='text-4xl text-center text-white ' > password generator </h1>
        <div className='flex my-3 mb-4 overflow-hidden rounded-lg shadow' >
          <input type="text"
            value={password}
            className='w-full px-3 py-1 outline-none'
            placeholder='passwor'
            readOnly
            ref={passworRef}
          />
          <button onClick={copyPassworfToClipboard} className='px-3 text-white bg-blue-700 outline-none py-0.5 shrink-0' >copy</button>
        </div>
        <div className='flex text-sm gap-x-2' >
          <div className="flex items-center gap-x-2">
            <input type="range"
              min={6}
              max={100}
              value={length}
              className='cursor-pointer'
              onChange={(e) => { setLengths(e.target.value) }}
            />
            <label >Lenght {length} </label>
          </div>
          <div className='flex items-center gap-x-1' >
            <input type="checkbox"
              defaultChecked={numberAllowed}
              id='numberInput'
              onChange={() => {
                setNumberAllowed((prev) => !prev);
              }}
            />
            <label htmlFor='numberInput' >Number Allowd </label>
          </div>
          <div className='flex items-center gap-x-1' >
            <input type="checkbox"
              defaultChecked={charAllowed}
              id='charAllowed'
              onChange={() => {
                setCharAllowes((prev) => !prev);
              }}
            />
            <label htmlFor='charAllowed' >Charactors Allowd </label>
          </div>
        </div>

      </div>

    </>
  )
}

export default App

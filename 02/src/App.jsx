import { Fragment } from "react";
import Cart from "./components/Cart";


const App = () => {
  // let myObj = {
  //   usename: "prakash",
  //   age: 21
  // }
  return (
    <Fragment>
      <h1 className="bg-green-400 text-black p-4 rounded-xl"> hello </h1>
      < Cart userNamee="prakash " textbtn="Click me " />
      < Cart userNamee="ajay " textbtn="checkOut" />
      < Cart userNamee="mukky " textbtn="Render" />
      < Cart userNamee="mahadev " textbtn="hare Me" />
      < Cart userNamee="shati " textbtn="Bio" />
    </Fragment  >
  )
}

export default App
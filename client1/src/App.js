import React,{createContext} from "react"
import NavBar from "./component/NavBar"
import "./App.css"
import {BrowserRouter,Route} from "react-router-dom"
import Count from "./component/screens/Count"
import List from "./component/screens/List"
import Stats from "./component/screens/Stats"
import Home from "./component/screens/Home"
import Search from "./component/screens/Search"

export const UserContext = createContext()

function App() {
  return (
    <BrowserRouter >
      <NavBar/>
      <Route exact path="/">
        <Home/>
        </Route>
        <Route path="/list">
        <List/>
        </Route>
        <Route path="/stats">
        <Stats/>
        </Route>
        <Route path="/count">
        <Count/>
        </Route>
        <Route path="/search">
        <Search/>
        </Route>
        
    </BrowserRouter>
    
  );
}

export default App;

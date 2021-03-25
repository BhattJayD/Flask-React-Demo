import React from "react"
import {Link} from "react-router-dom"

const NavBar=()=>{
    return(
        
    <nav>
    <div className="nav-wrapper #f06292 pink lighten-2 ">
        <Link to="/" className="brand-logo left">Home</Link>
        <ul id="nav-mobile" className="right">
        <li><Link to="list">List</Link></li>
        <li><Link to="count">count</Link></li>
        <li><Link to="stats">stats</Link></li>
        <li><Link to="search">Search</Link></li>
        </ul>
    </div>
    </nav>
        
    )
}
export default NavBar;
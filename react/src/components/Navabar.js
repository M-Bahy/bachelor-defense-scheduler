import React, { Component } from "react";
import {menuItems} from "./MenuItems"
import {Link} from "react-router-dom"
import "./Navbar.css"

class Navbar extends Component{
  render(){
    return(
      <nav className="NavbarItems">
        <h1 className="navbar-logo">Bachelor Defense Schedule</h1>
        <ul className="nav-menu">
          {
            menuItems.map((item , index) =>{return (<li key={index}><Link to={item.url}  className={item.cName}>{item.title}</Link></li>)} )}

        </ul>
      </nav>
    
      )
  }
}
export default Navbar;

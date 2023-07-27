import React from "react";
import Navbar from "./components/Navabar.js";
import Home from "./components/Home.js";
import MyConstraints from "./components/MyConstraints.js";
import About from "./components/about.js";
import Table from "./components/table.js";
import "./App.css";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
function App() {
  return (
    <Router>
      <div className="container">
        <div className="App">
          <Navbar />{" "}
        </div>
      </div>
      <Routes>
      <Route exact path="/" element={<Home />}></Route>
      <Route exact path='/myConst' element={< MyConstraints />}></Route>
      <Route exact path='/about' element={< About />}></Route>
      <Route exact path='/table' element={< Table />}></Route>
      </Routes>
    </Router>
  );
}
export default App;

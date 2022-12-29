import './App.css';
import React,{Container} from 'react';
import {Route} from 'react-router-dom'
import Home from "./pages/Home"
import Detail from "./pages/Detail"
function App() {
  return (
    <div>
        <Container>
          <Route path="/view" exact = {true} component ={Home}/>
          <Route path="/book/:seq" exact = {true} component ={Detail}/>
        </Container>
    </div>
  );
}

export default App;

import React from "react";
import { createRoot } from 'react-dom/client';

import "../static/css/App.scss"

const App = () => {
    
    return (
      <div id="app">
        <h1>Hello There welcome to your bucket list!</h1>
      </div>
    );
}
  
export default App;

const container = document.getElementById("app");
const root = createRoot(container);
root.render(<App />);
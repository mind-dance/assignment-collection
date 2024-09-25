import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Homework from './pages/Homework.jsx'
import Projects from './pages/Projects.jsx'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <Homework /> */}
    <Projects />
    </>
  )
}

export default App

import logo from './logo.svg'
import './App.css'
import { useState } from 'react'
import axios from 'axios'

function App () {
  const [message, setMessage] = useState(null)

  const handleClick = async () => {
    const resp = await axios.get('/api/v1')
    setMessage(resp.data.content)
  }

  return (
    <div className='App'>
      <header className='App-header'>
        <img src={logo} className='App-logo' alt='logo' />
        <button className='bg-black text-white p-2 rounded-xl' onClick={() => handleClick()}> Say Hi </button>
        {message &&
          <p className='my-2'>
            {message}
          </p>}
      </header>
    </div>
  )
}

export default App

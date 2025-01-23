import React from 'react'
import { useNavigate } from 'react-router-dom'

const Doctor = () => {
  const navigate = useNavigate()
  return (
    <div>
        <h1>Doctor Dashboard</h1>
        <button onClick={() => navigate('/')}>Logout</button>
      
    </div>
  )
}

export default Doctor

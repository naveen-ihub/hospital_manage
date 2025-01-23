import React from 'react'
import { useNavigate } from 'react-router-dom'

const Patient = () => {
  const navigate = useNavigate()
  return (
    <div>
        <h1>Patient Dashboard</h1>
        <button onClick={() => navigate('/')}>Logout</button>
      
    </div>
  )
}

export default Patient

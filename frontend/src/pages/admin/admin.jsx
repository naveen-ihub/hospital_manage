import React from 'react'
import { useNavigate } from 'react-router-dom'

const Admin = () => {
  const navigate = useNavigate()
  return (
    <div>
        <h1>Admin Dashboard</h1>
        <button onClick={() => navigate('/')}>Logout</button>
      
    </div>
  )
}

export default Admin

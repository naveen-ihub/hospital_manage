import React from 'react'
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom'
import Login from './pages/login'
import Signup from './pages/signup'
import Patient from './pages/patient/patient'
import Doctor from './pages/doctor/doctor'
import Admin from './pages/admin/admin'
import './App.css'

const HomePage = () => {
  const navigate = useNavigate()

  const handleRoleSelect = (role) => {
    navigate('/login', { state: { role } })
  }

  return (
    <div className="container">
      <h1>Welcome to the Hospital Management System</h1>
      <h2>Choose your role:</h2>
      
      <div className="button-container">
        <button 
          className="role-button"
          onClick={() => handleRoleSelect('patient')}
        >
          Patient
        </button>
        
        <button 
          className="role-button"
          onClick={() => handleRoleSelect('doctor')}
        >
          Doctor
        </button>
        
        <button 
          className="role-button"
          onClick={() => handleRoleSelect('admin')}
        >
          Admin
        </button>
      </div>
    </div>
  )
}

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/patient" element={<Patient />} />
        <Route path="/doctor" element={<Doctor />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </Router>
  )
}

export default App
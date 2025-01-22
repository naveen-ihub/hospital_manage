import React, { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

const Login = () => {
  const [credentials, setCredentials] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    role: ''
  })

  const navigate = useNavigate()
  const location = useLocation()
  const role = location.state?.role || 'guest'
  
  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Signup attempt for role:', role, 'with credentials:', credentials)
    // Add your signup logic here
    navigate('/login')
  }

  return (
    <div className="signup-container">
      <h2>Signup as {role}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            placeholder="Username"
            value={credentials.username}
            onChange={(e) => setCredentials({...credentials, username: e.target.value})}
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            placeholder="Email"
            value={credentials.email}
            onChange={(e) => setCredentials({...credentials, email: e.target.value})}
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            placeholder="Password"
            value={credentials.password}
            onChange={(e) => setCredentials({...credentials, password: e.target.value})}
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            placeholder="ConfirmPassword"
            value={credentials.confirmPassword}
            onChange={(e) => setCredentials({...credentials, confirmPassword: e.target.value})}
          />
        </div>
        <div className="form-group">
          <select value={credentials.role} onChange={(e) => setCredentials({...credentials, role: e.target.value})}>
            <option value="Patient">Patient</option>
            <option value="Doctor">Doctor</option>
            <option value="Admin">Admin</option>
          </select>
        </div>
        <button type="submit">Signup</button>
      </form>
      <div className="button-container">
        <button onClick={() => navigate('/')}>Back to Home</button>
        <p>Already have an account ?</p>
        <button onClick={() => navigate('/login')}>Login</button>
      </div>
    </div>
  )
}

export default Login
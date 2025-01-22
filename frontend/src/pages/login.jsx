import React, { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

const Login = () => {
  const [credentials, setCredentials] = useState({
    username: '',
    password: ''
  })

  const navigate = useNavigate()
  const location = useLocation()
  const role = location.state?.role || 'guest'
  
  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Login attempt for role:', role, 'with credentials:', credentials)
    // Add your login logic here
  }

  return (
    <div className="login-container">
      <h2>Login as {role}</h2>
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
            type="password"
            placeholder="Password"
            value={credentials.password}
            onChange={(e) => setCredentials({...credentials, password: e.target.value})}
          />
        </div>
        <button type="submit">Login</button>
      </form>
      <div className="button-container">
        <button onClick={() => navigate('/')}>Back to Home</button>
        <p>New user ?</p>
        <button onClick={() => navigate('/signup')}>Sign Up</button>
      </div>
    </div>
  )
}

export default Login
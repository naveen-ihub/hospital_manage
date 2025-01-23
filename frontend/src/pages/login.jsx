import React, { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

const Login = () => {
  const location = useLocation()
  const [credentials, setCredentials] = useState({
    username: '',
    password: '',
    role: location.state?.role
  })

  const navigate = useNavigate()

  const role = location.state?.role || 'patient'
  console.log(location.state?.role)


  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log('Login attempt for role:', role, 'with credentials:', credentials)
    const response = await fetch('http://localhost:8000/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });
    if (response.ok) {
      navigate(`/${role}`)
    } else {
      alert('Invalid credentials')
    }
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
        <button onClick={() => navigate('/signup', { state: {role}})}>Sign Up</button>
      </div>
    </div>
  )
}

export default Login